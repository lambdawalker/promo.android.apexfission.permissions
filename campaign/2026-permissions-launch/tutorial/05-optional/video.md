# Tutorial short 05 — Required and optional grants

Source chapter in [long video](../long-video/video.md): 05. Target 45–75 seconds; standalone vertical cut, 9:16.

**Title:** Required and optional grants | Android ApexFission Permissions
**Hook:** What if scanning needs camera but narration is optional?
**Problem:** Blocking the entire feature on a nice-to-have permission can stop a valid task.
**Solution:** Set required = false for microphone; the content receives PermissionGrants. Gate on required access and choose narration behavior using grants.isGranted(RECORD_AUDIO). If required access was already granted, content appears immediately and optional access is not requested automatically.
**Demo / visual:** Show the optional microphone label, grant camera and deny microphone on a real emulator, then show a narration-disabled success state from the sample demo. Show code.jpg.

## Spoken script and shot list

| Beat | Spoken words | What is shown |
| --- | --- | --- |
| 0–4 s · hook | “What if scanning needs camera but narration is optional?” | Title over actual Compose preview or sample app. |
| 4–13 s · problem | “Blocking the entire feature on a nice-to-have permission can stop a valid task.” | Mark the confusing point with a restrained label; no invented UI. |
| 13–38 s · solution | “Set required = false for microphone; the content receives PermissionGrants. Gate on required access and choose narration behavior using grants.isGranted(RECORD_AUDIO). If required access was already granted, content appears immediately and optional access is not requested automatically.” | Show [code excerpt](assets/code.jpg) and the relevant app or docs view; reveal lines at readable scale. |
| 38–55 s · demo | “Here is the same behavior in the sample app. Watch the state change after the user acts.” | Show the optional microphone label, grant camera and deny microphone on a real emulator, then show a narration-disabled success state from the sample demo. Show code.jpg. |
| 55–75 s · CTA | “If this helps, subscribe, comment with the permission flow you want covered next, star the GitHub repo, and share it with an Android developer. Contribute a fix or example through GitHub, or support the project at [SUPPORT_URL: Patreon or equivalent].” | Freeze on repo URL, license label, and [SUPPORT_URL]. |

**Recording source:** README.md Required and optional access; sites/demos/. The supplied [UI card](assets/ui-post.jpg) uses a repository Compose preview; record system prompts anew on an emulator. Add subtitles, cursor emphasis, and a visible ‘Android may show multiple prompts’ label where relevant.

**Caption:** Required and optional grants. Follow the full walkthrough on YouTube; code and docs at https://github.com/lambdawalker/android.apexfission.permissions. #AndroidDev #JetpackCompose #OpenSource #Kotlin #MobileDevelopment
**Cover:** Crop ui-post.jpg vertically, place a one-line title above the phone, and keep code out of the cover at small sizes.
