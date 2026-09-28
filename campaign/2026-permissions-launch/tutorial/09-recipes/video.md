# Tutorial short 09 — Location, notifications, and photo picker

Source chapter in [long video](../long-video/video.md): 09. Target 45–75 seconds; standalone vertical cut, 9:16.

**Title:** Location, notifications, and photo picker | Android ApexFission Permissions
**Hook:** Some Android access flows need more than a batch request.
**Problem:** Background location, version-specific notifications, and photo selection follow different platform behavior.
**Solution:** PermissionRecipes returns the host's next step for foreground location, staged background location, and notifications. For user-selected media, rememberVisualMediaPicker avoids asking for broad storage access. The host explains and acts on a user gesture.
**Demo / visual:** Record Platform recipes demo: approximate/precise, background step, notifications, photo picker. Split into chapter labels; never depict all of them as one atomic batch. Show code.jpg.

## Spoken script and shot list

| Beat | Spoken words | What is shown |
| --- | --- | --- |
| 0–4 s · hook | “Some Android access flows need more than a batch request.” | Title over actual Compose preview or sample app. |
| 4–13 s · problem | “Background location, version-specific notifications, and photo selection follow different platform behavior.” | Mark the confusing point with a restrained label; no invented UI. |
| 13–38 s · solution | “PermissionRecipes returns the host's next step for foreground location, staged background location, and notifications. For user-selected media, rememberVisualMediaPicker avoids asking for broad storage access. The host explains and acts on a user gesture.” | Show [code excerpt](assets/code.jpg) and the relevant app or docs view; reveal lines at readable scale. |
| 38–55 s · demo | “Here is the same behavior in the sample app. Watch the state change after the user acts.” | Record Platform recipes demo: approximate/precise, background step, notifications, photo picker. Split into chapter labels; never depict all of them as one atomic batch. Show code.jpg. |
| 55–75 s · CTA | “If this helps, subscribe, comment with the permission flow you want covered next, star the GitHub repo, and share it with an Android developer. Contribute a fix or example through GitHub, or support the project at [SUPPORT_URL: Patreon or equivalent].” | Freeze on repo URL, license label, and [SUPPORT_URL]. |

**Recording source:** README.md Platform-aware recipes; sites/recipes/. The supplied [UI card](assets/ui-post.jpg) uses a repository Compose preview; record system prompts anew on an emulator. Add subtitles, cursor emphasis, and a visible ‘Android may show multiple prompts’ label where relevant.

**Caption:** Location, notifications, and photo picker. Follow the full walkthrough on YouTube; code and docs at https://github.com/lambdawalker/android.apexfission.permissions. #AndroidDev #JetpackCompose #OpenSource #Kotlin #MobileDevelopment
**Cover:** Crop ui-post.jpg vertically, place a one-line title above the phone, and keep code out of the cover at small sizes.
