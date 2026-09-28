# Tutorial short 03 — Overview and custom Compose pages

Source chapter in [long video](../long-video/video.md): 03. Target 45–75 seconds; standalone vertical cut, 9:16.

**Title:** Overview and custom Compose pages | Android ApexFission Permissions
**Hook:** Your permission explanation can look like your app.
**Problem:** A generic rationale may not explain why this specific feature needs access.
**Solution:** The default overview appears when more than one permission is visible. Supply PermissionOverview with a full composable, or Hide it. Each PermissionDescription takes a complete page; mix DefaultPermissionPage with a custom Compose page.
**Demo / visual:** Swipe overview, camera, microphone in the carousel demo; freeze on the custom microphone page; show code.jpg and label that the host owns the page content.

## Spoken script and shot list

| Beat | Spoken words | What is shown |
| --- | --- | --- |
| 0–4 s · hook | “Your permission explanation can look like your app.” | Title over actual Compose preview or sample app. |
| 4–13 s · problem | “A generic rationale may not explain why this specific feature needs access.” | Mark the confusing point with a restrained label; no invented UI. |
| 13–38 s · solution | “The default overview appears when more than one permission is visible. Supply PermissionOverview with a full composable, or Hide it. Each PermissionDescription takes a complete page; mix DefaultPermissionPage with a custom Compose page.” | Show [code excerpt](assets/code.jpg) and the relevant app or docs view; reveal lines at readable scale. |
| 38–55 s · demo | “Here is the same behavior in the sample app. Watch the state change after the user acts.” | Swipe overview, camera, microphone in the carousel demo; freeze on the custom microphone page; show code.jpg and label that the host owns the page content. |
| 55–75 s · CTA | “If this helps, subscribe, comment with the permission flow you want covered next, star the GitHub repo, and share it with an Android developer. Contribute a fix or example through GitHub, or support the project at [SUPPORT_URL: Patreon or equivalent].” | Freeze on repo URL, license label, and [SUPPORT_URL]. |

**Recording source:** README.md Replace the default page; sites/compose/. The supplied [UI card](assets/ui-post.jpg) uses a repository Compose preview; record system prompts anew on an emulator. Add subtitles, cursor emphasis, and a visible ‘Android may show multiple prompts’ label where relevant.

**Caption:** Overview and custom Compose pages. Follow the full walkthrough on YouTube; code and docs at https://github.com/lambdawalker/android.apexfission.permissions. #AndroidDev #JetpackCompose #OpenSource #Kotlin #MobileDevelopment
**Cover:** Crop ui-post.jpg vertically, place a one-line title above the phone, and keep code out of the cover at small sizes.
