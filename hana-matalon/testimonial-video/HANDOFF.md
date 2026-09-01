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

## Open items

1. **Push may be incomplete.** Commit `0302f45` (the 8 LFS videos) was pushing in the
   background at switch time. Check:
   ```
   git -C "C:\Users\ILANM\בדיקות קלוד קוד\landing-page-assets" log origin/claude/video-editing-uploads-48bf9l..HEAD --oneline
   ```
   If it prints `0302f45`, the push didn't finish — re-run (needs the GitHub token from
   the repo-root CLAUDE.md as the HTTPS password):
   ```
   cd "C:\Users\ILANM\בדיקות קלוד קוד\landing-page-assets"
   git push origin claude/video-editing-uploads-48bf9l
   ```
2. **Transcription** — `omer, shlomi, dan, argov, gian` done. If `mvi-9782 / mvi-4099 /
   mvi-4480` are missing from `transcripts/`, finish them:
   ```
   cd "C:\Users\ILANM\בדיקות קלוד קוד\landing-page-assets\hana-matalon\testimonial-video"
   python scripts/transcribe.py
   ```
   (skips whatever's already done)
3. Whisper `medium` spellings need a cleanup pass before final captions (name lands as
   "חן/חנה מטלון"). Consider a `large-v3` re-run for caption-grade text.
4. Next: finish selects for the 5 remaining clips → full STORYBOARD.md → build with the
   `general-video` hyperframes skill → storyboard review → render.

## Transcripts + SELECTS.md are not committed yet

They're in the working tree, uncommitted, to avoid racing the in-flight push. Commit when ready:
```
git add hana-matalon/testimonial-video/{transcripts,scripts,SELECTS.md,HANDOFF.md}
git commit -m "Add transcripts, selects, transcribe script for testimonial-video"
```
