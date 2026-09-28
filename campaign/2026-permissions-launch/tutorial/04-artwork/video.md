# Tutorial short 04 — Choose hero artwork

Source chapter in [long video](../long-video/video.md): 04. Target 45–75 seconds; standalone vertical cut, 9:16.

**Title:** Choose hero artwork | Android ApexFission Permissions
**Hook:** A hero image and a navigation icon are two different jobs.
**Problem:** Reusing one tiny icon for a large explanation can weaken the page design.
**Solution:** DefaultPermissionPage accepts ImageVector, Bitmap, Drawable, or drawable resource ID through heroImage. PermissionDescription.icon controls the separate small icon strip. Keep an owned bitmap valid while composed.
**Demo / visual:** Record all four cards in the hero artwork demo, then zoom the small strip icon separately. Show the actual R.drawable example from code.jpg.

## Spoken script and shot list

| Beat | Spoken words | What is shown |
| --- | --- | --- |
| 0–4 s · hook | “A hero image and a navigation icon are two different jobs.” | Title over actual Compose preview or sample app. |
| 4–13 s · problem | “Reusing one tiny icon for a large explanation can weaken the page design.” | Mark the confusing point with a restrained label; no invented UI. |
| 13–38 s · solution | “DefaultPermissionPage accepts ImageVector, Bitmap, Drawable, or drawable resource ID through heroImage. PermissionDescription.icon controls the separate small icon strip. Keep an owned bitmap valid while composed.” | Show [code excerpt](assets/code.jpg) and the relevant app or docs view; reveal lines at readable scale. |
| 38–55 s · demo | “Here is the same behavior in the sample app. Watch the state change after the user acts.” | Record all four cards in the hero artwork demo, then zoom the small strip icon separately. Show the actual R.drawable example from code.jpg. |
| 55–75 s · CTA | “If this helps, subscribe, comment with the permission flow you want covered next, star the GitHub repo, and share it with an Android developer. Contribute a fix or example through GitHub, or support the project at [SUPPORT_URL: Patreon or equivalent].” | Freeze on repo URL, license label, and [SUPPORT_URL]. |

**Recording source:** README.md DefaultPermissionPage(heroImage); sites/demos/. The supplied [UI card](assets/ui-post.jpg) uses a repository Compose preview; record system prompts anew on an emulator. Add subtitles, cursor emphasis, and a visible ‘Android may show multiple prompts’ label where relevant.

**Caption:** Choose hero artwork. Follow the full walkthrough on YouTube; code and docs at https://github.com/lambdawalker/android.apexfission.permissions. #AndroidDev #JetpackCompose #OpenSource #Kotlin #MobileDevelopment
**Cover:** Crop ui-post.jpg vertically, place a one-line title above the phone, and keep code out of the cover at small sizes.
