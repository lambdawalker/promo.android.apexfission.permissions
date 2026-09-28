# Complete tutorial — Android ApexFission Permissions

**Working title:** Android Runtime Permissions with Compose: install, explain, request, recover
**Target:** 16–20 minutes, 16:9 YouTube master, 1080p; captions and chapter markers. Shorts are self-contained rewrites of these chapters, not raw mid-sentence crops.
**Thumbnail:** Real bundle overview beside the repo name; text “Permissions with context”; no Android system dialog pasted from a static preview.

## Intro (0:00–0:55)

**Hook / problem, spoken:** “Permission prompts are easy to trigger and harder to explain. What happens when a feature needs camera and microphone, a user grants only one, or the app must lead them to Settings?”

**Solution, spoken:** “Android ApexFission Permissions is an open-source Jetpack Compose library, free to use under Apache 2.0. It gives you explanation pages, an action to request missing ordinary runtime permissions, and recovery options. We’ll run the sample, customize the pages, and handle Android-specific paths. Android owns the system prompts, so a batch may still produce more than one dialog.”

**Visual:** Repo README and LICENSE, captured documentation homepage, then actual bundle overview preview. Show a title card with site and GitHub addresses. No installation claim yet.

## Chapter map

| # | Feature section | Standalone tutorial short |
| --- | --- | --- |
| 01 | Install and run the sample | [01-install](../01-install/video.md) |
| 02 | Request a group after one tap | [02-batch](../02-batch/video.md) |
| 03 | Overview and custom Compose pages | [03-pages](../03-pages/video.md) |
| 04 | Choose hero artwork | [04-artwork](../04-artwork/video.md) |
| 05 | Required and optional grants | [05-optional](../05-optional/video.md) |
| 06 | All versus MissingOnly | [06-display](../06-display/video.md) |
| 07 | Optional timed reading | [07-timing](../07-timing/video.md) |
| 08 | Denial and Settings recovery | [08-recovery](../08-recovery/video.md) |
| 09 | Location, notifications, and photo picker | [09-recipes](../09-recipes/video.md) |
| 10 | Callbacks without library UI | [10-code-only](../10-code-only/video.md) |

## Full spoken chapter script / visual direction

### Chapter 01: Install and run the sample (about 90 seconds)

**Hook / problem, spoken:** “Want to try a permission flow without wiring every state yourself? The README shows a future Maven Central coordinate, but the first release is not guaranteed yet.”

**Solution, spoken:** “Clone the repository, include the :permission module, add implementation(project(":permission")), declare the requested permissions in the app manifest, and run the sample app. Check the release page before using any Maven coordinate.”

**Demo / screen recording:** Show terminal clone, settings.gradle.kts module include, the code.jpg source card, manifest CAMERA line, and the sample app home. Use the site screenshot as a cutaway; do not say Maven 0.2.0 is published.

**Transition, spoken:** “Next, let's look at request a group after one tap.” **Source:** README.md install; sites/getting-started/. **Short cut:** [01-install](../01-install/video.md).

### Chapter 02: Request a group after one tap (about 90 seconds)

**Hook / problem, spoken:** “Camera and microphone, one explanation flow: what happens at the request button? Two separate entry screens can interrupt the user's task and leave partial results hard to explain.”

**Solution, spoken:** “Use HandlePermissions with two PermissionDescription pages. The button requests missing ordinary runtime permissions together after the user taps. Android can display several system dialogs and grant only some.”

**Demo / screen recording:** Show bundle-overview to permission-detail, tap library button on real emulator, show actual Android prompts only in newly recorded footage, then return to a partial-grant screen.

**Transition, spoken:** “Next, let's look at overview and custom compose pages.” **Source:** README.md Request a group; docs/batch-request.md. **Short cut:** [02-batch](../02-batch/video.md).

### Chapter 03: Overview and custom Compose pages (about 90 seconds)

**Hook / problem, spoken:** “Your permission explanation can look like your app. A generic rationale may not explain why this specific feature needs access.”

**Solution, spoken:** “The default overview appears when more than one permission is visible. Supply PermissionOverview with a full composable, or Hide it. Each PermissionDescription takes a complete page; mix DefaultPermissionPage with a custom Compose page.”

**Demo / screen recording:** Swipe overview, camera, microphone in the carousel demo; freeze on the custom microphone page; show code.jpg and label that the host owns the page content.

**Transition, spoken:** “Next, let's look at choose hero artwork.” **Source:** README.md Replace the default page; sites/compose/. **Short cut:** [03-pages](../03-pages/video.md).

### Chapter 04: Choose hero artwork (about 90 seconds)

**Hook / problem, spoken:** “A hero image and a navigation icon are two different jobs. Reusing one tiny icon for a large explanation can weaken the page design.”

**Solution, spoken:** “DefaultPermissionPage accepts ImageVector, Bitmap, Drawable, or drawable resource ID through heroImage. PermissionDescription.icon controls the separate small icon strip. Keep an owned bitmap valid while composed.”

**Demo / screen recording:** Record all four cards in the hero artwork demo, then zoom the small strip icon separately. Show the actual R.drawable example from code.jpg.

**Transition, spoken:** “Next, let's look at required and optional grants.” **Source:** README.md DefaultPermissionPage(heroImage); sites/demos/. **Short cut:** [04-artwork](../04-artwork/video.md).

### Chapter 05: Required and optional grants (about 90 seconds)

**Hook / problem, spoken:** “What if scanning needs camera but narration is optional? Blocking the entire feature on a nice-to-have permission can stop a valid task.”

**Solution, spoken:** “Set required = false for microphone; the content receives PermissionGrants. Gate on required access and choose narration behavior using grants.isGranted(RECORD_AUDIO). If required access was already granted, content appears immediately and optional access is not requested automatically.”

**Demo / screen recording:** Show the optional microphone label, grant camera and deny microphone on a real emulator, then show a narration-disabled success state from the sample demo. Show code.jpg.

**Transition, spoken:** “Next, let's look at all versus missingonly.” **Source:** README.md Required and optional access; sites/demos/. **Short cut:** [05-optional](../05-optional/video.md).

### Chapter 06: All versus MissingOnly (about 90 seconds)

**Hook / problem, spoken:** “Should a granted permission stay visible? As the granted set changes, the explanation carousel can feel cluttered.”

**Solution, spoken:** “PermissionDisplayMode.All keeps granted pages and green check badges. MissingOnly hides granted pages from the carousel and strip. Both still gate on the original required set and request missing access.”

**Demo / screen recording:** Use the documented screenshot of multiple permissions without overview, then an emulator take of a grant transition in both modes. Clearly label any side-by-side mock sequencing as an edit, not a captured single screen.

**Transition, spoken:** “Next, let's look at optional timed reading.” **Source:** README.md displayMode; sites/compose/. **Short cut:** [06-display](../06-display/video.md).

### Chapter 07: Optional timed reading (about 90 seconds)

**Hook / problem, spoken:** “A swipeable permission story can advance at a readable pace. Fixed timing can rush longer explanations.”

**Solution, spoken:** “Opt in with autoAdvance = true. The segmented bar shows page progress; touches and selections pause it. Set autoAdvanceDelayMillis directly or use estimateReadingDelayMillis for known copy. It pauses when the host is not resumed and is disabled with Android touch exploration.”

**Demo / screen recording:** Show segmented-reading-progress fixture, then emulator recording of pause and resume. Put code.jpg over the last frame; avoid claiming it reads arbitrary Compose text.

**Transition, spoken:** “Next, let's look at denial and settings recovery.” **Source:** README.md Optional timed carousel; sites/compose/. **Short cut:** [07-timing](../07-timing/video.md).

### Chapter 08: Denial and Settings recovery (about 90 seconds)

**Hook / problem, spoken:** “What happens after Android stops showing a permission prompt? A blocked feature needs a helpful path forward, and a denial signal is not a definitive permanent-denial flag.”

**Solution, spoken:** “The UI can offer app settings when missing access cannot be prompted. Customize recoveryContent, settingsActionLabel, and onOpenSettings. Phrase the state as inferred; the user taps before Settings opens.”

**Demo / screen recording:** Show settings-recovery fixture, then record a real deny and Settings return on emulator. Show code.jpg with onOpenSettings; do not promise a definitive permanent-denial detection.

**Transition, spoken:** “Next, let's look at location, notifications, and photo picker.” **Source:** README.md recoveryContent; sites/compose/. **Short cut:** [08-recovery](../08-recovery/video.md).

### Chapter 09: Location, notifications, and photo picker (about 90 seconds)

**Hook / problem, spoken:** “Some Android access flows need more than a batch request. Background location, version-specific notifications, and photo selection follow different platform behavior.”

**Solution, spoken:** “PermissionRecipes returns the host's next step for foreground location, staged background location, and notifications. For user-selected media, rememberVisualMediaPicker avoids asking for broad storage access. The host explains and acts on a user gesture.”

**Demo / screen recording:** Record Platform recipes demo: approximate/precise, background step, notifications, photo picker. Split into chapter labels; never depict all of them as one atomic batch. Show code.jpg.

**Transition, spoken:** “Next, let's look at callbacks without library ui.” **Source:** README.md Platform-aware recipes; sites/recipes/. **Short cut:** [09-recipes](../09-recipes/video.md).

### Chapter 10: Callbacks without library UI (about 90 seconds)

**Hook / problem, spoken:** “Already have your own permission screen? You may need a check and request API without adopting a Compose flow.”

**Solution, spoken:** “runIfPermissionsGranted checks and reports missing names to otherwise; the host owns the launcher. Alternatively, create an Activity-owned PermissionRequester before STARTED; attaching onDenied starts the request. Recheck after results and retry user actions after recreation.”

**Demo / screen recording:** Record both actions in Code-only demo; show code.jpg and brief callback flow annotation. Do not imply that a Context-only check can launch the request.

**Transition, spoken:** “Next, let's look at the resources and ways to help the project.” **Source:** README.md Code-only request and check; sites/callbacks/. **Short cut:** [10-code-only](../10-code-only/video.md).

## Outro (about 45 seconds, once)

**Spoken:** “That is the path from explanation to grant and recovery. The repo has the sample app, full API declarations, platform recipes, and tests. If this saved you time, subscribe, comment with your hardest Android permission edge case, star the repo, and share this with your team. Contributions and examples are welcome on GitHub. If you want to fund maintenance, use [SUPPORT_URL: Patreon or equivalent] in the description. The code is open source and free to use under Apache 2.0.”

**Visual:** Repo/docs homepage capture, LICENSE link, a real sample screen, end card with GitHub / docs / [SUPPORT_URL]. Keep addresses on screen long enough to read.

## Production checks

- Re-record current sample app, Android prompts, and Settings route on a known API level. Clearly mark device/API level on screen. Repo screenshots are static Compose previews.
- Use [site-home.jpg](assets/site-home.jpg) and [bundle-preview.jpg](assets/bundle-preview.jpg) as cutaways. Record readable code at 16:9; short code cards are in each chapter's assets.
- Show a source checkout install. Verify a released Maven coordinate immediately before publication; the README describes a future release and a replaceable 0.2.0 example.
- Avoid claims of atomic grants, definitive permanent denial, automatic optional requests after required grants, or broad media access for picker flows.
