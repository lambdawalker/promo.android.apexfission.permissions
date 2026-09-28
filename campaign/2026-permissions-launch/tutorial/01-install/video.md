# Tutorial short 01 — Install and run the sample

Source chapter in [long video](../long-video/video.md): 01. Target 45–75 seconds; standalone vertical cut, 9:16.

**Title:** Install and run the sample | Android ApexFission Permissions
**Hook:** Want to try a permission flow without wiring every state yourself?
**Problem:** The README shows a future Maven Central coordinate, but the first release is not guaranteed yet.
**Solution:** Clone the repository, include the :permission module, add implementation(project(":permission")), declare the requested permissions in the app manifest, and run the sample app. Check the release page before using any Maven coordinate.
**Demo / visual:** Show terminal clone, settings.gradle.kts module include, the code.jpg source card, manifest CAMERA line, and the sample app home. Use the site screenshot as a cutaway; do not say Maven 0.2.0 is published.

## Spoken script and shot list

| Beat | Spoken words | What is shown |
| --- | --- | --- |
| 0–4 s · hook | “Want to try a permission flow without wiring every state yourself?” | Title over actual Compose preview or sample app. |
| 4–13 s · problem | “The README shows a future Maven Central coordinate, but the first release is not guaranteed yet.” | Mark the confusing point with a restrained label; no invented UI. |
| 13–38 s · solution | “Clone the repository, include the :permission module, add implementation(project(":permission")), declare the requested permissions in the app manifest, and run the sample app. Check the release page before using any Maven coordinate.” | Show [code excerpt](assets/code.jpg) and the relevant app or docs view; reveal lines at readable scale. |
| 38–55 s · demo | “Here is the same behavior in the sample app. Watch the state change after the user acts.” | Show terminal clone, settings.gradle.kts module include, the code.jpg source card, manifest CAMERA line, and the sample app home. Use the site screenshot as a cutaway; do not say Maven 0.2.0 is published. |
| 55–75 s · CTA | “If this helps, subscribe, comment with the permission flow you want covered next, star the GitHub repo, and share it with an Android developer. Contribute a fix or example through GitHub, or support the project at [SUPPORT_URL: Patreon or equivalent].” | Freeze on repo URL, license label, and [SUPPORT_URL]. |

**Recording source:** README.md install; sites/getting-started/. The supplied [UI card](assets/ui-post.jpg) uses a repository Compose preview; record system prompts anew on an emulator. Add subtitles, cursor emphasis, and a visible ‘Android may show multiple prompts’ label where relevant.

**Caption:** Install and run the sample. Follow the full walkthrough on YouTube; code and docs at https://github.com/lambdawalker/android.apexfission.permissions. #AndroidDev #JetpackCompose #OpenSource #Kotlin #MobileDevelopment
**Cover:** Crop ui-post.jpg vertically, place a one-line title above the phone, and keep code out of the cover at small sizes.
