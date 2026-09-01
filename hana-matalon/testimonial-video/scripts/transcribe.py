"""Transcribe the testimonial clips (Hebrew) with faster-whisper.

Reads assets/<slug>.mp4, writes transcripts/<slug>.txt (plain) and
transcripts/<slug>.json (segments + word-level timestamps).
Skips any slug that already has a .json. Safe to re-run.

    pip install faster-whisper      # ffmpeg must be on PATH
    python scripts/transcribe.py
"""
import json, subprocess, sys, time
from pathlib import Path
from faster_whisper import WhisperModel

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
OUT = ROOT / "transcripts"
OUT.mkdir(exist_ok=True)

SLUGS = ["omer", "shlomi", "dan", "argov", "gian", "mvi-9782", "mvi-4099", "mvi-4480"]
MODEL = "medium"          # bump to "large-v3" for a final caption-grade pass

todo = [s for s in SLUGS if not (OUT / f"{s}.json").exists()]
if not todo:
    print("nothing to do — all transcripts present")
    sys.exit(0)
print(f"to transcribe: {', '.join(todo)}")

model = WhisperModel(MODEL, device="cpu", compute_type="int8")
print(f"model {MODEL} loaded", flush=True)

for slug in todo:
    src = ASSETS / f"{slug}.mp4"
    if not src.exists():
        print(f"!! missing {src}", flush=True)
        continue
    wav = OUT / f"{slug}.wav"
    subprocess.run(["ffmpeg", "-y", "-i", str(src), "-ac", "1", "-ar", "16000",
                    "-vn", str(wav)], check=True, capture_output=True)
    t0 = time.time()
    print(f"\n=== {slug} ===", flush=True)
    segments, info = model.transcribe(
        str(wav), language="he", word_timestamps=True,
        vad_filter=True, vad_parameters=dict(min_silence_duration_ms=500))
    segs, lines = [], []
    for s in segments:
        words = [{"w": w.word, "s": round(w.start, 2), "e": round(w.end, 2)}
                 for w in (s.words or [])]
        segs.append({"id": s.id, "start": round(s.start, 2), "end": round(s.end, 2),
                     "text": s.text.strip(), "words": words})
        lines.append(f"[{s.start:7.2f} -> {s.end:7.2f}] {s.text.strip()}")
        print(lines[-1], flush=True)
    (OUT / f"{slug}.txt").write_text("\n".join(lines), encoding="utf-8")
    (OUT / f"{slug}.json").write_text(json.dumps(
        {"slug": slug, "source": f"assets/{slug}.mp4", "duration": round(info.duration, 2),
         "language": info.language, "segments": segs}, ensure_ascii=False, indent=2),
        encoding="utf-8")
    wav.unlink(missing_ok=True)
    print(f"--- {slug} done in {time.time()-t0:.0f}s, {len(segs)} segments", flush=True)

print("\nALL DONE", flush=True)
