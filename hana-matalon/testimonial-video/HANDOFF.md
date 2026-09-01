# Handoff — hana-matalon/testimonial-video

State as of the terminal switch. Everything below is on local disk in this repo.

## Where things are

| what | path |
|---|---|
| Repo clone | `C:\Users\ILANM\בדיקות קלוד קוד\landing-page-assets` |
| Branch | `claude/video-editing-uploads-48bf9l` |
| Raw footage (8, Git LFS) | `hana-matalon/testimonial-video/assets/*.mp4` |
| Transcripts (faster-whisper `medium`) | `hana-matalon/testimonial-video/transcripts/<slug>.{txt,json}` |
| Selects / draft spine | `hana-matalon/testimonial-video/SELECTS.md` |
| Re-runnable transcribe script | `hana-matalon/testimonial-video/scripts/transcribe.py` |
| Confirmed brief | `hana-matalon/testimonial-video/BRIEF.md` |

## Clip specs (differ from BRIEF.md)

| slug | speaker | res | orientation | dur |
|---|---|---|---|---|
| omer | עומר נוראי | 464×832 | portrait (soft) | 2:05 |
| shlomi | שלומי | 848×480 | landscape SD (soft) | 2:12 |
| dan | דן | 478×850 | portrait (soft) | 2:31 |
| argov | ארגוב | 1920×1080 | landscape | 0:46 |
| gian | ג'יאן | 1920×1080 | landscape | 0:41 |
| mvi-9782 | ? | 1920×1080 | landscape | 0:35 |
| mvi-4099 | ? | 1920×1080 | landscape | 0:42 |
| mvi-4480 | ? | 1920×1080 | landscape | 0:58 |

Topic is **real-estate investment coaching**, not matchmaking.

## Done in this session

- All **8 transcripts** in `transcripts/` (faster-whisper `medium`).
- `SELECTS.md` — all 8 clips ranked (tiers 🟢/🔵/⚪) with timecoded lines.
- `STORYBOARD.md` — draft v1, 12-scene ~1:30 cut, for review.

## Open items

1. **Push may be incomplete.** Commit `0302f45` (the 8 LFS videos) was still uploading
   in the background at switch time (slow uplink, ~187 MB LFS). Check:
   ```
   git -C "C:\Users\ILANM\בדיקות קלוד קוד\landing-page-assets" log origin/claude/video-editing-uploads-48bf9l..HEAD --oneline
   ```
   If it prints `0302f45`, re-run (GitHub token from repo-root CLAUDE.md as the HTTPS
   password; LFS resumes / skips finished objects):
   ```
   cd "C:\Users\ILANM\בדיקות קלוד קוד\landing-page-assets"
   git push origin claude/video-editing-uploads-48bf9l
   ```
2. **Caption cleanup** — `medium` transcripts have name/word errors (see SELECTS.md
   notes). Hand-fix the ~8 selected spans, or re-run `scripts/transcribe.py` after
   editing it to `MODEL = "large-v3"`.
3. **Storyboard review** — see the 6 "Open items" at the bottom of `STORYBOARD.md`
   (logo assets, CTA copy, lower-third names, visual identity, runtime cap, consent).
4. Next after sign-off: build with the `general-video` hyperframes skill → storyboard
   review → render.

## Commit the working files when ready
```
cd "C:\Users\ILANM\בדיקות קלוד קוד\landing-page-assets"
git add hana-matalon/testimonial-video/{transcripts,scripts,SELECTS.md,STORYBOARD.md,HANDOFF.md}
git commit -m "Add transcripts, selects, storyboard draft for testimonial-video"
git push origin claude/video-editing-uploads-48bf9l
```

## Transcripts + SELECTS.md are not committed yet

They're in the working tree, uncommitted, to avoid racing the in-flight push. Commit when ready:
```
git add hana-matalon/testimonial-video/{transcripts,scripts,SELECTS.md,HANDOFF.md}
git commit -m "Add transcripts, selects, transcribe script for testimonial-video"
```
