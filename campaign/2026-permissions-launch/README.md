# Android ApexFission Permissions content campaign

## 1. Campaign summary

**Goal:** turn qualified Android interest into documentation visits, GitHub stars, trial integrations, issues/discussions, contributions, and voluntary support. **Audience:** Compose developers, mobile teams, indie developers, and open-source contributors.

**Core promise:** explain ordinary runtime permissions in context, request missing access after a user action, and adapt grant/recovery behavior. Open source and free to use under [Apache 2.0](https://github.com/lambdawalker/android.apexfission.permissions/blob/main/LICENSE). The first release is still described as forthcoming in the checked-in README; publication copy must verify Maven availability before claiming an install coordinate.

**Editorial tone:** direct, helpful, beginner-friendly, technically precise. Show real library UI and emulator recordings; use the checked-in static screenshots only as labeled Compose previews. Avoid “one Android dialog,” “permanent denial detected,” or “all permissions work in a batch.”

**Links:** library repo https://github.com/lambdawalker/android.apexfission.permissions; campaign repo https://github.com/lambdawalker/promo.android.apexfission.permissions; docs https://lambdawalker.github.io/android.apexfission.permissions/; [SUPPORT_URL: Patreon or other verified support page]; [VIDEO_URL: final upload]. Replace placeholders before scheduling. Do not invent a support destination.

**Measurement:** UTM-tagged docs visits by platform if approved; stars and forks relative to launch baseline; README-to-install traffic; demo opens; comments/questions, issues/PRs; support conversions. Review weekly and reply to technical questions within two working days.

## 2. Tutorial track plan

One [chaptered long video](tutorial/long-video/video.md) (16–20 minutes) with ten matching standalone shorts. Every chapter has one feature focus, an authentic demo, a source excerpt, and its own [post.md] companion. Release the long video first, then individual short clips. Shorts include local setup and a complete CTA.

| Section | Short | Primary proof |
| --- | --- | --- |
| 01 Install and run the sample | [video](tutorial/01-install/video.md) · [post](tutorial/01-install/post.md) | README.md install; sites/getting-started/ |
| 02 Request a group after one tap | [video](tutorial/02-batch/video.md) · [post](tutorial/02-batch/post.md) | README.md Request a group; docs/batch-request.md |
| 03 Overview and custom Compose pages | [video](tutorial/03-pages/video.md) · [post](tutorial/03-pages/post.md) | README.md Replace the default page; sites/compose/ |
| 04 Choose hero artwork | [video](tutorial/04-artwork/video.md) · [post](tutorial/04-artwork/post.md) | README.md DefaultPermissionPage(heroImage); sites/demos/ |
| 05 Required and optional grants | [video](tutorial/05-optional/video.md) · [post](tutorial/05-optional/post.md) | README.md Required and optional access; sites/demos/ |
| 06 All versus MissingOnly | [video](tutorial/06-display/video.md) · [post](tutorial/06-display/post.md) | README.md displayMode; sites/compose/ |
| 07 Optional timed reading | [video](tutorial/07-timing/video.md) · [post](tutorial/07-timing/post.md) | README.md Optional timed carousel; sites/compose/ |
| 08 Denial and Settings recovery | [video](tutorial/08-recovery/video.md) · [post](tutorial/08-recovery/post.md) | README.md recoveryContent; sites/compose/ |
| 09 Location, notifications, and photo picker | [video](tutorial/09-recipes/video.md) · [post](tutorial/09-recipes/post.md) | README.md Platform-aware recipes; sites/recipes/ |
| 10 Callbacks without library UI | [video](tutorial/10-code-only/video.md) · [post](tutorial/10-code-only/post.md) | README.md Code-only request and check; sites/callbacks/ |

## 3. Promo track plan

Eight [promo folders](promo/), each containing a 30–45 second six-beat script and platform-specific companion copy. Promo videos show UI and benefits only: **no code, no editor, no API declarations**. Each explicitly says open source and free under Apache 2.0 and ends with the complete CTA.

| Promo | Script and companion |
| --- | --- |
| Explain access before the dialog | [video](promo/01-explain-first/video.md) · [post](promo/01-explain-first/post.md) |
| One action for grouped access | [video](promo/02-one-action/video.md) · [post](promo/02-one-action/post.md) |
| A permission page that fits your app | [video](promo/03-make-it-yours/video.md) · [post](promo/03-make-it-yours/post.md) |
| Let optional access stay optional | [video](promo/04-optional-access/video.md) · [post](promo/04-optional-access/post.md) |
| Handle a partial grant | [video](promo/05-partial-grants/video.md) · [post](promo/05-partial-grants/post.md) |
| A carousel with reading time | [video](promo/06-reading-pace/video.md) · [post](promo/06-reading-pace/post.md) |
| Show a path through Settings | [video](promo/07-settings-recovery/video.md) · [post](promo/07-settings-recovery/post.md) |
| Use the right Android path | [video](promo/08-platform-rules/video.md) · [post](promo/08-platform-rules/post.md) |

## 4. Long video script

[Full script, spoken chapters, demo notes, thumbnail, and outro](tutorial/long-video/video.md).

## 5. Short video scripts

Each tutorial and promo folder linked above contains video.md with timed beats, what is said, what is shown, caption, cover, and CTA. The ten tutorial shorts map one-to-one to the ten long-video chapters.

## 6. Written post drafts

Each video folder has post.md with LinkedIn, Facebook, Instagram, and Shorts/TikTok copy, media references, alt text, and cover guidance. The long video has a companion post and YouTube description.

## 7. Asset checklist and recording brief

- [x] Real official site capture in long-video/assets/site-home.jpg and promo asset folders.
- [x] Repo Compose fixture in long-video/assets/bundle-preview.jpg.
- [x] 18 edited UI post cards derived from checked-in screenshot fixtures (JPEG, 1080×1350).
- [x] 10 code cards rendered into JPEG directly from current README excerpts (1600×900); see tools/render_campaign_assets.py.
- [ ] Record sample app walkthrough, real Android prompts and Settings state on emulator. Label API/device. Static fixtures cannot show system prompts.
- [ ] Capture hero artwork demo and code-only demo, which have no checked-in screenshots; UI cards for those episodes are illustrative *other* library UI and must be replaced by actual footage.
- [ ] Record voiceover and burn readable captions; get [SUPPORT_URL], [VIDEO_URL], and final brand review. Use the same readable GitHub end card on all shorts.
- [ ] Before publishing, check release version, screenshots versus current UI, license, and support destination.

**Asset provenance:** docs/screenshots/README.md identifies the Compose screenshot workflow. site-home.jpg is a live capture of the official docs homepage on 2026-09-28. The post card overlays add titles and a provenance footer but do not claim to be a phone capture of Android prompts.

## 8. Posting schedule (America/Ciudad_Juarez)

Four weeks, three tutorial and two promo releases weekly after the long video; 18 shorts in total. Start on the next chosen Monday after editing approval. Suggested slots: long video Monday 10:00, shorts Tuesday/Thursday/Saturday 12:00, promos Wednesday/Friday 12:00. Publish companion posts the same day, then a LinkedIn summary 24 hours later. Cross-post vertical masters to YouTube Shorts, Instagram Reels, and TikTok; use the matching post.md for LinkedIn/Facebook/Instagram.

| Week | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Long tutorial + companion | T01 install | P01 explain first | T02 batch | P02 one action | T03 pages |
| 2 | Community replies / metrics | T04 artwork | P03 make it yours | T05 optional | P04 optional access | T06 display |
| 3 | Community replies / metrics | T07 timing | P05 partial grants | T08 recovery | P06 reading pace | T09 recipes |
| 4 | Community replies / metrics | T10 code-only | P07 settings recovery | Best Q&A excerpt [record if warranted] | P08 platform rules | Campaign recap |

**Platform adaptations:** YouTube long 16:9, 16–20 min, chapter links, pinned comment with repo and docs. Shorts/Reels/TikTok 9:16, 45–75 sec, captions in center safe region, UI zoomed to legible text; Instagram/TikTok quick hook and short voice lines. LinkedIn 4:5 still or native vertical clip with a practical engineering takeaway; Facebook clearer context and direct repo link; Instagram 4:5 carousel cover and link-in-bio instruction. Avoid unverified length ceilings; cut each short for clarity, then check the upload limits of the account at publish time.

**Review loop:** after week 1, compare 3-second retention, completion, saves, repo visits, and question themes. Reorder the remaining topics if actual audience questions indicate a stronger need, preserving technical accuracy and the required CTAs.
