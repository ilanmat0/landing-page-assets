# STORYBOARD — hana-matalon/testimonial-video (draft v1, for review)

9:16 · 1080×1920 · ~82s · Hebrew rail captions · no BGM · logo sting open/close.
Cut order chosen for a **pain → guide → fast result → why her → warm close** arc.
Timecodes are the target timeline; `src` = clip + in–out (source seconds) from SELECTS.md.

| # | t (s) | dur | src | on-screen caption (verbatim, RTL) | visual / treatment |
|---|-------|-----|-----|----------------------------------|--------------------|
| 0 | 0:00–0:03 | 3.0 | — | — | **Logo sting in.** Hana identity lockup on solid ground; quick settle. *(asset TBD — see open items)* |
| 1 | 0:03–0:13 | 10.0 | shlomi 9.5–19.5 | "הסתבכנו… לקח לנו כמה שנים. המחירים רק עלו ועלו — הרגשנו ממש אבודים" | 480p src → tight centered crop, slight push-in. Desaturate a touch to sell "the before". |
| 2 | 0:13–0:19 | 6.0 | shlomi 40.5–46.5 | "לא ידענו איפה משקיעים, איך עושים עם המשכנתא — לא ידענו שום דבר" | same treatment; hard-ish cut on "שום דבר". |
| 3 | 0:19–0:28 | 9.0 | shlomi 49.0–58.0 | "מישהו הפנה אותנו לחנה מטלון… לקחה אותנו עם האוטו והמליצה בדיוק איפה כדאי להשקיע" | color returns to normal at this cut (the "turn"). |
| 4 | 0:28–0:37 | 9.0 | shlomi 70.5–80.0 | "תוך שבוע מאז שהכרנו אותה — קנינו דירה. ממש שבוע. זה היה ממש הצלה" | hold on "ממש שבוע"; small scale-up emphasis on the caption. |
| 5 | 0:37–0:43 | 6.0 | mvi-9782 1.0–7.0 | "אם לא חנה מטלון — היינו עד היום יושבים על הגדר ומחכים למשהו שאולי לעולם לא יקרה" | **HD**, full-frame. New face = new energy. |
| 6 | 0:43–0:49 | 6.0 | mvi-9782 13.2–19.2 | "ליוותה אותנו בכל כך הרבה סבלנות שזה הרגיש כאילו היא קונה דירה לבן שלה" | HD full-frame; let the line land, no motion. |
| 7 | 0:49–0:58 | 9.0 | omer 12.0–21.0 | "אתמול חתמתי על חוזה לרכוש את הדירה הראשונה שלי להשקעה" | portrait soft → ~85% frame with soft inset bg; lower-third "עומר". |
| 8 | 0:58–1:06 | 8.0 | omer 98.0–106.0 | "מדברת עם כרישי נדל״ן ונותנת להם בראש — מומחית ברמה הכי גבוהה שיש" | same framing; caption emphasis on "מומחית ברמה הכי גבוהה". |
| 9 | 1:06–1:15 | 9.0 | dan 49.0–58.0 | "היא הצילה אותי מכמה עסקאות כושלות — עסקה אחת כזאת יכולה להרוס חיים של משפחה שלמה" | portrait soft, inset; lower-third "דן". Slight vignette for gravity. |
| 10 | 1:15–1:20 | 5.0 | argov 8.0–13.5 | "אין דבר כזה לקנות דירה לפני שהולכים למטלון" | **HD**; punchy, quick in/out; biggest caption weight of the film. |
| 11 | 1:20–1:26 | 6.0 | mvi-4480 47.1–53.4 | "מובטח לכם הטוב ביותר — מניסיון אישי שלי" | HD full-frame; warm, calm. |
| 12 | 1:26–1:30 | 4.0 | — | **CTA card** (text TBD) | Logo sting out → end card: headline + contact. Hold ~2s. |

**Runtime:** ~1:30. If the brief's 75–90s ceiling is firm this fits; to reach ~78s,
drop #2 and tighten #7/#9 by ~1s each.

## Alternates / bench (swap-ins if a cut doesn't hold on screen)
- Replace #6 with **mvi-9782 19.8–27.4** ("בעלים של נכס שמניב הרבה יותר ממה שיכולנו לדמיין").
- Replace #9 with **dan 0.3–13.4** (the "married off my kids / income properties" parent angle) if a softer beat is wanted.
- Add **omer 74.0–88.0** ("באה איתי לסיור… לא משנה איפה היא גרה בארץ") as a 6s dedication beat before #12 if runtime allows.
- **gian / mvi-4099** currently unused — weak/generic; keep on bench only.

## Caption spec
- Rail / verbatim, bottom band ~14–18% up from the safe area, RTL, 2 lines max.
- Cleanup pass required first — `medium` transcripts have name/word errors. Either
  hand-fix the ~8 selected spans, or re-run `scripts/transcribe.py` with `large-v3`.
- Punctuation: keep it minimal (spoken feel); no full stops mid-thought.

## Visual identity (proposal — needs sign-off)
Independent from yitzhak-matalon. Proposed direction: **grounded / trustworthy**, not
flashy — warm neutral base (bone / warm grey), one confident accent (deep teal or
brick), a strong Hebrew grotesk for captions (e.g. Heebo / Assistant / Rubik),
generous margins, minimal motion (the cuts do the work). Confirm or redirect before build.

## Open items (need input before render)
1. **Logo assets** — the animated logo (`סרטון וידאו מ-אילן`, mp4) and static logo
   (`לוגו`, jpg) are still only on Drive, not in the repo. Drop them into
   `assets/logo-anim.mp4` / `assets/logo.jpg` (or tell me and I'll fetch if reachable).
2. **CTA end-card copy** — exact headline + contact line (phone / site / "לפרטים בכפתור").
3. **Lower-third names** — confirm: show "עומר", "דן" (first names only?) + surnames?
   The 3 MVI speakers are unidentified — names, or leave uncredited?
4. **Visual identity** — approve the proposal above or give a direction.
5. **Runtime** — hard 90s cap, or is ~1:30 acceptable for the landing page?
6. **Consent** — these are named real people on a public repo → public landing page.
   Assumed OK (that's the destination), but confirm each speaker approved use.
