# Tutorial short 06 — All versus MissingOnly

Source chapter in [long video](../long-video/video.md): 06. Target 45–75 seconds; standalone vertical cut, 9:16.

**Title:** All versus MissingOnly | Android ApexFission Permissions
**Hook:** Should a granted permission stay visible?
**Problem:** As the granted set changes, the explanation carousel can feel cluttered.
**Solution:** PermissionDisplayMode.All keeps granted pages and green check badges. MissingOnly hides granted pages from the carousel and strip. Both still gate on the original required set and request missing access.
**Demo / visual:** Use the documented screenshot of multiple permissions without overview, then an emulator take of a grant transition in both modes. Clearly label any side-by-side mock sequencing as an edit, not a captured single screen.

## Spoken script and shot list

| Beat | Spoken words | What is shown |
| --- | --- | --- |
| 0–4 s · hook | “Should a granted permission stay visible?” | Title over actual Compose preview or sample app. |
| 4–13 s · problem | “As the granted set changes, the explanation carousel can feel cluttered.” | Mark the confusing point with a restrained label; no invented UI. |
| 13–38 s · solution | “PermissionDisplayMode.All keeps granted pages and green check badges. MissingOnly hides granted pages from the carousel and strip. Both still gate on the original required set and request missing access.” | Show [code excerpt](assets/code.jpg) and the relevant app or docs view; reveal lines at readable scale. |
| 38–55 s · demo | “Here is the same behavior in the sample app. Watch the state change after the user acts.” | Use the documented screenshot of multiple permissions without overview, then an emulator take of a grant transition in both modes. Clearly label any side-by-side mock sequencing as an edit, not a captured single screen. |
| 55–75 s · CTA | “If this helps, subscribe, comment with the permission flow you want covered next, star the GitHub repo, and share it with an Android developer. Contribute a fix or example through GitHub, or support the project at [SUPPORT_URL: Patreon or equivalent].” | Freeze on repo URL, license label, and [SUPPORT_URL]. |

**Recording source:** README.md displayMode; sites/compose/. The supplied [UI card](assets/ui-post.jpg) uses a repository Compose preview; record system prompts anew on an emulator. Add subtitles, cursor emphasis, and a visible ‘Android may show multiple prompts’ label where relevant.

**Caption:** All versus MissingOnly. Follow the full walkthrough on YouTube; code and docs at https://github.com/lambdawalker/android.apexfission.permissions. #AndroidDev #JetpackCompose #OpenSource #Kotlin #MobileDevelopment
**Cover:** Crop ui-post.jpg vertically, place a one-line title above the phone, and keep code out of the cover at small sizes.
