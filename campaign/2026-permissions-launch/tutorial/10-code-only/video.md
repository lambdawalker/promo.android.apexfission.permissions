# Tutorial short 10 — Callbacks without library UI

Source chapter in [long video](../long-video/video.md): 10. Target 45–75 seconds; standalone vertical cut, 9:16.

**Title:** Callbacks without library UI | Android ApexFission Permissions
**Hook:** Already have your own permission screen?
**Problem:** You may need a check and request API without adopting a Compose flow.
**Solution:** runIfPermissionsGranted checks and reports missing names to otherwise; the host owns the launcher. Alternatively, create an Activity-owned PermissionRequester before STARTED; attaching onDenied starts the request. Recheck after results and retry user actions after recreation.
**Demo / visual:** Record both actions in Code-only demo; show code.jpg and brief callback flow annotation. Do not imply that a Context-only check can launch the request.

## Spoken script and shot list

| Beat | Spoken words | What is shown |
| --- | --- | --- |
| 0–4 s · hook | “Already have your own permission screen?” | Title over actual Compose preview or sample app. |
| 4–13 s · problem | “You may need a check and request API without adopting a Compose flow.” | Mark the confusing point with a restrained label; no invented UI. |
| 13–38 s · solution | “runIfPermissionsGranted checks and reports missing names to otherwise; the host owns the launcher. Alternatively, create an Activity-owned PermissionRequester before STARTED; attaching onDenied starts the request. Recheck after results and retry user actions after recreation.” | Show [code excerpt](assets/code.jpg) and the relevant app or docs view; reveal lines at readable scale. |
| 38–55 s · demo | “Here is the same behavior in the sample app. Watch the state change after the user acts.” | Record both actions in Code-only demo; show code.jpg and brief callback flow annotation. Do not imply that a Context-only check can launch the request. |
| 55–75 s · CTA | “If this helps, subscribe, comment with the permission flow you want covered next, star the GitHub repo, and share it with an Android developer. Contribute a fix or example through GitHub, or support the project at [SUPPORT_URL: Patreon or equivalent].” | Freeze on repo URL, license label, and [SUPPORT_URL]. |

**Recording source:** README.md Code-only request and check; sites/callbacks/. The supplied [UI card](assets/ui-post.jpg) uses a repository Compose preview; record system prompts anew on an emulator. Add subtitles, cursor emphasis, and a visible ‘Android may show multiple prompts’ label where relevant.

**Caption:** Callbacks without library UI. Follow the full walkthrough on YouTube; code and docs at https://github.com/lambdawalker/android.apexfission.permissions. #AndroidDev #JetpackCompose #OpenSource #Kotlin #MobileDevelopment
**Cover:** Crop ui-post.jpg vertically, place a one-line title above the phone, and keep code out of the cover at small sizes.
