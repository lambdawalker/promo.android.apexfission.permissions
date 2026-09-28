# Tutorial short 08 — Denial and Settings recovery

Source chapter in [long video](../long-video/video.md): 08. Target 45–75 seconds; standalone vertical cut, 9:16.

**Title:** Denial and Settings recovery | Android ApexFission Permissions
**Hook:** What happens after Android stops showing a permission prompt?
**Problem:** A blocked feature needs a helpful path forward, and a denial signal is not a definitive permanent-denial flag.
**Solution:** The UI can offer app settings when missing access cannot be prompted. Customize recoveryContent, settingsActionLabel, and onOpenSettings. Phrase the state as inferred; the user taps before Settings opens.
**Demo / visual:** Show settings-recovery fixture, then record a real deny and Settings return on emulator. Show code.jpg with onOpenSettings; do not promise a definitive permanent-denial detection.

## Spoken script and shot list

| Beat | Spoken words | What is shown |
| --- | --- | --- |
| 0–4 s · hook | “What happens after Android stops showing a permission prompt?” | Title over actual Compose preview or sample app. |
| 4–13 s · problem | “A blocked feature needs a helpful path forward, and a denial signal is not a definitive permanent-denial flag.” | Mark the confusing point with a restrained label; no invented UI. |
| 13–38 s · solution | “The UI can offer app settings when missing access cannot be prompted. Customize recoveryContent, settingsActionLabel, and onOpenSettings. Phrase the state as inferred; the user taps before Settings opens.” | Show [code excerpt](assets/code.jpg) and the relevant app or docs view; reveal lines at readable scale. |
| 38–55 s · demo | “Here is the same behavior in the sample app. Watch the state change after the user acts.” | Show settings-recovery fixture, then record a real deny and Settings return on emulator. Show code.jpg with onOpenSettings; do not promise a definitive permanent-denial detection. |
| 55–75 s · CTA | “If this helps, subscribe, comment with the permission flow you want covered next, star the GitHub repo, and share it with an Android developer. Contribute a fix or example through GitHub, or support the project at [SUPPORT_URL: Patreon or equivalent].” | Freeze on repo URL, license label, and [SUPPORT_URL]. |

**Recording source:** README.md recoveryContent; sites/compose/. The supplied [UI card](assets/ui-post.jpg) uses a repository Compose preview; record system prompts anew on an emulator. Add subtitles, cursor emphasis, and a visible ‘Android may show multiple prompts’ label where relevant.

**Caption:** Denial and Settings recovery. Follow the full walkthrough on YouTube; code and docs at https://github.com/lambdawalker/android.apexfission.permissions. #AndroidDev #JetpackCompose #OpenSource #Kotlin #MobileDevelopment
**Cover:** Crop ui-post.jpg vertically, place a one-line title above the phone, and keep code out of the cover at small sizes.
