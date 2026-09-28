# Tutorial short 02 — Request a group after one tap

Source chapter in [long video](../long-video/video.md): 02. Target 45–75 seconds; standalone vertical cut, 9:16.

**Title:** Request a group after one tap | Android ApexFission Permissions
**Hook:** Camera and microphone, one explanation flow: what happens at the request button?
**Problem:** Two separate entry screens can interrupt the user's task and leave partial results hard to explain.
**Solution:** Use HandlePermissions with two PermissionDescription pages. The button requests missing ordinary runtime permissions together after the user taps. Android can display several system dialogs and grant only some.
**Demo / visual:** Show bundle-overview to permission-detail, tap library button on real emulator, show actual Android prompts only in newly recorded footage, then return to a partial-grant screen.

## Spoken script and shot list

| Beat | Spoken words | What is shown |
| --- | --- | --- |
| 0–4 s · hook | “Camera and microphone, one explanation flow: what happens at the request button?” | Title over actual Compose preview or sample app. |
| 4–13 s · problem | “Two separate entry screens can interrupt the user's task and leave partial results hard to explain.” | Mark the confusing point with a restrained label; no invented UI. |
| 13–38 s · solution | “Use HandlePermissions with two PermissionDescription pages. The button requests missing ordinary runtime permissions together after the user taps. Android can display several system dialogs and grant only some.” | Show [code excerpt](assets/code.jpg) and the relevant app or docs view; reveal lines at readable scale. |
| 38–55 s · demo | “Here is the same behavior in the sample app. Watch the state change after the user acts.” | Show bundle-overview to permission-detail, tap library button on real emulator, show actual Android prompts only in newly recorded footage, then return to a partial-grant screen. |
| 55–75 s · CTA | “If this helps, subscribe, comment with the permission flow you want covered next, star the GitHub repo, and share it with an Android developer. Contribute a fix or example through GitHub, or support the project at [SUPPORT_URL: Patreon or equivalent].” | Freeze on repo URL, license label, and [SUPPORT_URL]. |

**Recording source:** README.md Request a group; docs/batch-request.md. The supplied [UI card](assets/ui-post.jpg) uses a repository Compose preview; record system prompts anew on an emulator. Add subtitles, cursor emphasis, and a visible ‘Android may show multiple prompts’ label where relevant.

**Caption:** Request a group after one tap. Follow the full walkthrough on YouTube; code and docs at https://github.com/lambdawalker/android.apexfission.permissions. #AndroidDev #JetpackCompose #OpenSource #Kotlin #MobileDevelopment
**Cover:** Crop ui-post.jpg vertically, place a one-line title above the phone, and keep code out of the cover at small sizes.
