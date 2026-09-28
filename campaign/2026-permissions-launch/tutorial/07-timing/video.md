# Tutorial short 07 — Optional timed reading

Source chapter in [long video](../long-video/video.md): 07. Target 45–75 seconds; standalone vertical cut, 9:16.

**Title:** Optional timed reading | Android ApexFission Permissions
**Hook:** A swipeable permission story can advance at a readable pace.
**Problem:** Fixed timing can rush longer explanations.
**Solution:** Opt in with autoAdvance = true. The segmented bar shows page progress; touches and selections pause it. Set autoAdvanceDelayMillis directly or use estimateReadingDelayMillis for known copy. It pauses when the host is not resumed and is disabled with Android touch exploration.
**Demo / visual:** Show segmented-reading-progress fixture, then emulator recording of pause and resume. Put code.jpg over the last frame; avoid claiming it reads arbitrary Compose text.

## Spoken script and shot list

| Beat | Spoken words | What is shown |
| --- | --- | --- |
| 0–4 s · hook | “A swipeable permission story can advance at a readable pace.” | Title over actual Compose preview or sample app. |
| 4–13 s · problem | “Fixed timing can rush longer explanations.” | Mark the confusing point with a restrained label; no invented UI. |
| 13–38 s · solution | “Opt in with autoAdvance = true. The segmented bar shows page progress; touches and selections pause it. Set autoAdvanceDelayMillis directly or use estimateReadingDelayMillis for known copy. It pauses when the host is not resumed and is disabled with Android touch exploration.” | Show [code excerpt](assets/code.jpg) and the relevant app or docs view; reveal lines at readable scale. |
| 38–55 s · demo | “Here is the same behavior in the sample app. Watch the state change after the user acts.” | Show segmented-reading-progress fixture, then emulator recording of pause and resume. Put code.jpg over the last frame; avoid claiming it reads arbitrary Compose text. |
| 55–75 s · CTA | “If this helps, subscribe, comment with the permission flow you want covered next, star the GitHub repo, and share it with an Android developer. Contribute a fix or example through GitHub, or support the project at [SUPPORT_URL: Patreon or equivalent].” | Freeze on repo URL, license label, and [SUPPORT_URL]. |

**Recording source:** README.md Optional timed carousel; sites/compose/. The supplied [UI card](assets/ui-post.jpg) uses a repository Compose preview; record system prompts anew on an emulator. Add subtitles, cursor emphasis, and a visible ‘Android may show multiple prompts’ label where relevant.

**Caption:** Optional timed reading. Follow the full walkthrough on YouTube; code and docs at https://github.com/lambdawalker/android.apexfission.permissions. #AndroidDev #JetpackCompose #OpenSource #Kotlin #MobileDevelopment
**Cover:** Crop ui-post.jpg vertically, place a one-line title above the phone, and keep code out of the cover at small sizes.
