#!/usr/bin/env python3
"""Build the editorial package; run render_campaign_assets.py afterward."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "campaign" / "2026-permissions-launch"
REPO = "https://github.com/lambdawalker/android.apexfission.permissions"
CAMPAIGN_REPO = "https://github.com/lambdawalker/promo.android.apexfission.permissions"
SITE = "https://lambdawalker.github.io/android.apexfission.permissions/"
CTA = ("If this helps, subscribe, comment with the permission flow you want covered next, "
       "star the GitHub repo, and share it with an Android developer. Contribute a fix or example "
       "through GitHub, or support the project at [SUPPORT_URL: Patreon or equivalent].")
TAGS = "#AndroidDev #JetpackCompose #OpenSource #Kotlin #MobileDevelopment"

# Section, title, hook, problem, solution and precise visual direction.
TUTORIALS = [
("01-install","Install and run the sample",
 "Want to try a permission flow without wiring every state yourself?",
 "The README shows a future Maven Central coordinate, but the first release is not guaranteed yet.",
 "Clone the repository, include the :permission module, add implementation(project(\":permission\")), declare the requested permissions in the app manifest, and run the sample app. Check the release page before using any Maven coordinate.",
 "Show terminal clone, settings.gradle.kts module include, the code.jpg source card, manifest CAMERA line, and the sample app home. Use the site screenshot as a cutaway; do not say Maven 0.2.0 is published.",
 "README.md install; sites/getting-started/"),
("02-batch","Request a group after one tap",
 "Camera and microphone, one explanation flow: what happens at the request button?",
 "Two separate entry screens can interrupt the user's task and leave partial results hard to explain.",
 "Use HandlePermissions with two PermissionDescription pages. The button requests missing ordinary runtime permissions together after the user taps. Android can display several system dialogs and grant only some.",
 "Show bundle-overview to permission-detail, tap library button on real emulator, show actual Android prompts only in newly recorded footage, then return to a partial-grant screen.",
 "README.md Request a group; docs/batch-request.md"),
("03-pages","Overview and custom Compose pages",
 "Your permission explanation can look like your app.",
 "A generic rationale may not explain why this specific feature needs access.",
 "The default overview appears when more than one permission is visible. Supply PermissionOverview with a full composable, or Hide it. Each PermissionDescription takes a complete page; mix DefaultPermissionPage with a custom Compose page.",
 "Swipe overview, camera, microphone in the carousel demo; freeze on the custom microphone page; show code.jpg and label that the host owns the page content.",
 "README.md Replace the default page; sites/compose/"),
("04-artwork","Choose hero artwork",
 "A hero image and a navigation icon are two different jobs.",
 "Reusing one tiny icon for a large explanation can weaken the page design.",
 "DefaultPermissionPage accepts ImageVector, Bitmap, Drawable, or drawable resource ID through heroImage. PermissionDescription.icon controls the separate small icon strip. Keep an owned bitmap valid while composed.",
 "Record all four cards in the hero artwork demo, then zoom the small strip icon separately. Show the actual R.drawable example from code.jpg.",
 "README.md DefaultPermissionPage(heroImage); sites/demos/"),
("05-optional","Required and optional grants",
 "What if scanning needs camera but narration is optional?",
 "Blocking the entire feature on a nice-to-have permission can stop a valid task.",
 "Set required = false for microphone; the content receives PermissionGrants. Gate on required access and choose narration behavior using grants.isGranted(RECORD_AUDIO). If required access was already granted, content appears immediately and optional access is not requested automatically.",
 "Show the optional microphone label, grant camera and deny microphone on a real emulator, then show a narration-disabled success state from the sample demo. Show code.jpg.",
 "README.md Required and optional access; sites/demos/"),
("06-display","All versus MissingOnly",
 "Should a granted permission stay visible?",
 "As the granted set changes, the explanation carousel can feel cluttered.",
 "PermissionDisplayMode.All keeps granted pages and green check badges. MissingOnly hides granted pages from the carousel and strip. Both still gate on the original required set and request missing access.",
 "Use the documented screenshot of multiple permissions without overview, then an emulator take of a grant transition in both modes. Clearly label any side-by-side mock sequencing as an edit, not a captured single screen.",
 "README.md displayMode; sites/compose/"),
("07-timing","Optional timed reading",
 "A swipeable permission story can advance at a readable pace.",
 "Fixed timing can rush longer explanations.",
 "Opt in with autoAdvance = true. The segmented bar shows page progress; touches and selections pause it. Set autoAdvanceDelayMillis directly or use estimateReadingDelayMillis for known copy. It pauses when the host is not resumed and is disabled with Android touch exploration.",
 "Show segmented-reading-progress fixture, then emulator recording of pause and resume. Put code.jpg over the last frame; avoid claiming it reads arbitrary Compose text.",
 "README.md Optional timed carousel; sites/compose/"),
("08-recovery","Denial and Settings recovery",
 "What happens after Android stops showing a permission prompt?",
 "A blocked feature needs a helpful path forward, and a denial signal is not a definitive permanent-denial flag.",
 "The UI can offer app settings when missing access cannot be prompted. Customize recoveryContent, settingsActionLabel, and onOpenSettings. Phrase the state as inferred; the user taps before Settings opens.",
 "Show settings-recovery fixture, then record a real deny and Settings return on emulator. Show code.jpg with onOpenSettings; do not promise a definitive permanent-denial detection.",
 "README.md recoveryContent; sites/compose/"),
("09-recipes","Location, notifications, and photo picker",
 "Some Android access flows need more than a batch request.",
 "Background location, version-specific notifications, and photo selection follow different platform behavior.",
 "PermissionRecipes returns the host's next step for foreground location, staged background location, and notifications. For user-selected media, rememberVisualMediaPicker avoids asking for broad storage access. The host explains and acts on a user gesture.",
 "Record Platform recipes demo: approximate/precise, background step, notifications, photo picker. Split into chapter labels; never depict all of them as one atomic batch. Show code.jpg.",
 "README.md Platform-aware recipes; sites/recipes/"),
("10-code-only","Callbacks without library UI",
 "Already have your own permission screen?",
 "You may need a check and request API without adopting a Compose flow.",
 "runIfPermissionsGranted checks and reports missing names to otherwise; the host owns the launcher. Alternatively, create an Activity-owned PermissionRequester before STARTED; attaching onDenied starts the request. Recheck after results and retry user actions after recreation.",
 "Record both actions in Code-only demo; show code.jpg and brief callback flow annotation. Do not imply that a Context-only check can launch the request.",
 "README.md Code-only request and check; sites/callbacks/"),
]

PROMOS = [
("01-explain-first","Explain access before the dialog","A permission prompt with no context?","People may not know why camera access is needed.","A rushed explanation can break the flow.","Show the library's overview and a camera page before the request button.","Your feature explains access in its own words, then the user chooses to continue.","bundle-overview"),
("02-one-action","One action for grouped access","One feature, two permissions?","Separate explanations can fragment a single task.","Partial grants still need handling.","Show the carousel's camera and microphone pages with the one request action.","A single library action starts a batch of missing ordinary runtime requests; Android may show multiple prompts.","permission-detail"),
("03-make-it-yours","A permission page that fits your app","Does your rationale feel generic?","Generic copy may not explain your actual feature.","Context helps users decide.","Show the custom microphone Compose page and the default camera page in the demo.","You can provide a complete Compose page or a DefaultPermissionPage with your own hero artwork.","permission-detail"),
("04-optional-access","Let optional access stay optional","Does an optional mic block the camera?","A user might say yes to scanning and no to narration.","They should still be able to scan.","Show the optional microphone label and the sample app's narration-disabled success state.","Mark microphone optional, then use the current grant snapshot to adjust the feature.","permission-detail"),
("05-partial-grants","Handle a partial grant","What if only one permission is granted?","Android can grant part of a group.","The feature needs a clear next step.","Show granted and missing states, then the existing explanation screen.","The library checks required grants and requests the missing permissions from the same flow.","settings-recovery"),
("06-reading-pace","A carousel with reading time","Ever seen an explanation advance too quickly?","Different pages take different time to read.","Users need control over the pace.","Show segmented progress and a visible pause/resume button.","The optional timed carousel supports per-page delays and pauses on interaction.","segmented-reading-progress"),
("07-settings-recovery","Show a path through Settings","No dialog appears after another tap?","Android may stop prompting, and the app still needs a recovery path.","A dead end can abandon the feature.","Show the cautious recovery note and Open App Settings action; record the real Settings transition.","The library can show a Settings route and lets your app customize its explanation.","settings-recovery"),
("08-platform-rules","Use the right Android path","Can every permission go into one batch?","Location stages, notifications, and selected media differ by Android version.","The wrong request flow confuses users.","Show the Platform recipes demo switching between location, notification, and picker choices.","Recipes suggest the host's next step; the media picker chooses files without broad storage access.","bundle-overview"),
]

def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip()+"\n")

def post(kind, slug, title, hook, solution, screenshot, n):
    link = f"{CAMPAIGN_REPO}/tree/main/campaign/2026-permissions-launch/{kind}/{slug}"
    source = f"assets/ui-post.jpg"
    intro = "Open source and free to use under Apache 2.0, Android ApexFission Permissions"
    core = f"{hook} {solution}"
    code_asset = "- For tutorial: [actual source excerpt](assets/code.jpg). Crop to a readable excerpt rather than showing 15 lines on a phone.\n" if kind == "tutorial" else ""
    return f"""# Companion post — {title}

## Media and cover

- Primary image: [{source}]({source}), a campaign card built from the repository's Compose screenshot fixture. This depicts library UI, not the Android system permission dialog.
{code_asset.rstrip()}
- Screenshot description / alt text: {screenshot}. Include “Compose preview” in alt text.
- Cover text: “{title}” over the UI card; keep title inside the center 80% for vertical crops.

## LinkedIn

{intro} helps Android teams show why a feature needs access.

{core}

The walkthrough and assets: {link}
Docs: {SITE}

Which permission flow takes the most time in your app? Comment, star the repo, share the example, or contribute a fix. Optional project support: [SUPPORT_URL: Patreon or equivalent].

{TAGS}

## Facebook

{hook} {solution}

This is {intro.lower()}. See the demo and source at {REPO}. If it helps, share it, leave a question, or star the project. Support development: [SUPPORT_URL: Patreon or equivalent].

## Instagram caption

{hook}

{solution}

{intro}. Full docs and source at the link in bio: {SITE}

Save this for your next Android feature. Comment with your edge case, share, star the repo, and support if you can: [SUPPORT_URL: Patreon or equivalent].

{TAGS} #AndroidPermissions

## YouTube Shorts / TikTok caption

{title}. {solution} Open source under Apache 2.0. Docs and GitHub: {SITE} {REPO} #AndroidDev #Kotlin #OpenSource

## Publishing note

Use a trackable campaign URL only after supplying an approved analytics link. Instagram's nonclickable caption URL belongs in the bio/link hub; no link hub is assumed here.
"""

for n, (slug, title, hook, problem, solution, visual, source) in enumerate(TUTORIALS, 1):
    directory = OUT/"tutorial"/slug
    write(directory/"video.md", f"""# Tutorial short {n:02d} — {title}

Source chapter in [long video](../long-video/video.md): {n:02d}. Target 45–75 seconds; standalone vertical cut, 9:16.

**Title:** {title} | Android ApexFission Permissions
**Hook:** {hook}
**Problem:** {problem}
**Solution:** {solution}
**Demo / visual:** {visual}

## Spoken script and shot list

| Beat | Spoken words | What is shown |
| --- | --- | --- |
| 0–4 s · hook | “{hook}” | Title over actual Compose preview or sample app. |
| 4–13 s · problem | “{problem}” | Mark the confusing point with a restrained label; no invented UI. |
| 13–38 s · solution | “{solution}” | Show [code excerpt](assets/code.jpg) and the relevant app or docs view; reveal lines at readable scale. |
| 38–55 s · demo | “Here is the same behavior in the sample app. Watch the state change after the user acts.” | {visual} |
| 55–75 s · CTA | “{CTA}” | Freeze on repo URL, license label, and [SUPPORT_URL]. |

**Recording source:** {source}. The supplied [UI card](assets/ui-post.jpg) uses a repository Compose preview; record system prompts anew on an emulator. Add subtitles, cursor emphasis, and a visible ‘Android may show multiple prompts’ label where relevant.

**Caption:** {title}. Follow the full walkthrough on YouTube; code and docs at {REPO}. {TAGS}
**Cover:** Crop ui-post.jpg vertically, place a one-line title above the phone, and keep code out of the cover at small sizes.
""")
    write(directory/"post.md", post("tutorial",slug,title,hook,solution,visual,n))

for n, (slug,title,hook,pain,why,show,benefit,fixture) in enumerate(PROMOS, 1):
    directory = OUT/"promo"/slug
    write(directory/"video.md", f"""# Promo short {n:02d} — {title}

Target 45–60 seconds; 9:16 master. **No code on screen or in spoken narration.**

**Title:** {title} | Open-source Android permissions
**Hook:** {hook}
**Problem:** {pain}
**Solution:** {benefit}
**Demo / visual:** {show}

## Spoken script and shot list

| Beat | Spoken words | What is shown |
| --- | --- | --- |
| Hook · 0–3 s | “{hook}” | Close crop of real library UI; bold subtitle. |
| Pain · 3–8 s | “{pain}” | Hold on the relevant explanation or state, without fabricated dialogs. |
| Why · 8–13 s | “{why}” | Highlight the decision point in the recorded app. |
| Solve · 13–24 s | “Android ApexFission Permissions is open source and free to use under Apache 2.0. {benefit}” | {show} |
| Benefit · 24–29 s | “Make the next step clearer for your users and save time building the flow.” | [Compose UI card](assets/ui-post.jpg) plus site home capture. |
| Outro / CTA · 29–60 s | “{CTA}” | Repo address, Subscribe · Comment · Star · Share · Contribute · Support; [SUPPORT_URL]. |

**Recording direction:** {show} Existing fixture: docs/screenshots/{fixture}.png. The card is a Compose preview, not a system dialog. Show system UI only from an actual newly captured emulator session. Never show a code editor, syntax, or API declarations in this track.

**Caption:** {hook} Open source and free under Apache 2.0. {benefit} {REPO} {TAGS}
**Cover:** {title}; real UI crop from assets/ui-post.jpg, no code.
""")
    write(directory/"post.md", post("promo",slug,title,hook,benefit,show,n))

long = OUT/"tutorial"/"long-video"
chapters = "\n".join(f"| {i:02d} | {t[1]} | [{t[0]}](../{t[0]}/video.md) |" for i,t in enumerate(TUTORIALS,1))
script = "\n\n".join(
    f"### Chapter {i:02d}: {title} (about 90 seconds)\n\n"
    f"**Hook / problem, spoken:** “{hook} {problem}”\n\n"
    f"**Solution, spoken:** “{solution}”\n\n"
    f"**Demo / screen recording:** {visual}\n\n"
    f"**Transition, spoken:** “Next, let's look at {TUTORIALS[i][1].lower() if i < len(TUTORIALS) else 'the resources and ways to help the project'}.” "
    f"**Source:** {source}. **Short cut:** [{slug}](../{slug}/video.md)."
    for i,(slug,title,hook,problem,solution,visual,source) in enumerate(TUTORIALS,1))
write(long/"video.md",f"""# Complete tutorial — Android ApexFission Permissions

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
{chapters}

## Full spoken chapter script / visual direction

{script}

## Outro (about 45 seconds, once)

**Spoken:** “That is the path from explanation to grant and recovery. The repo has the sample app, full API declarations, platform recipes, and tests. If this saved you time, subscribe, comment with your hardest Android permission edge case, star the repo, and share this with your team. Contributions and examples are welcome on GitHub. If you want to fund maintenance, use [SUPPORT_URL: Patreon or equivalent] in the description. The code is open source and free to use under Apache 2.0.”

**Visual:** Repo/docs homepage capture, LICENSE link, a real sample screen, end card with GitHub / docs / [SUPPORT_URL]. Keep addresses on screen long enough to read.

## Production checks

- Re-record current sample app, Android prompts, and Settings route on a known API level. Clearly mark device/API level on screen. Repo screenshots are static Compose previews.
- Use [site-home.jpg](assets/site-home.jpg) and [bundle-preview.jpg](assets/bundle-preview.jpg) as cutaways. Record readable code at 16:9; short code cards are in each chapter's assets.
- Show a source checkout install. Verify a released Maven coordinate immediately before publication; the README describes a future release and a replaceable 0.2.0 example.
- Avoid claims of atomic grants, definitive permanent denial, automatic optional requests after required grants, or broad media access for picker flows.
""")
write(long/"post.md", f"""# Companion post — Complete Android permissions tutorial

## Screenshots

- [Documentation homepage](assets/site-home.jpg): live capture of the official library site, showing “Permissions, with context.”
- [Bundle preview](assets/bundle-preview.jpg): repository Compose screenshot fixture with overview and camera/microphone icon strip; not an Android system dialog.

## LinkedIn

Android ApexFission Permissions is open source and free to use under Apache 2.0. I put together a full tour of its Compose permission flow: installing from source, group requests, custom pages, optional grants, recovery, platform recipes, and callback-only use.

Watch the chaptered tutorial, then browse the runnable demos and documentation: {SITE}
Repository: {REPO}

Which Android permission edge case should the next demo cover? Subscribe, comment, star, share, or contribute. Optional support: [SUPPORT_URL: Patreon or equivalent].

{TAGS}

## Facebook

New tutorial: a practical tour of Android ApexFission Permissions. The library is open source and free under Apache 2.0. See how the Compose UI explains requests and handles grant states, then explore platform-specific recipes. Watch here: [VIDEO_URL]. Code and docs: {REPO} {SITE}

## Instagram

Permission flows deserve context. 📱 A full walkthrough of the open-source Android ApexFission Permissions library is up: group requests, custom Compose pages, optional access, recovery, and more. Free to use under Apache 2.0. Watch from the link in bio: [VIDEO_URL]. Star, share, comment, and support: [SUPPORT_URL].

{TAGS}

## YouTube description

Android ApexFission Permissions: an open-source, Apache 2.0 Compose library for explaining ordinary runtime permissions, requesting a group after a user action, and handling grant/recovery states.

Repo: {REPO}
Docs: {SITE}
Support: [SUPPORT_URL: Patreon or equivalent]

Chapters: replace with actual edit timestamps for intro, install, batch, pages, hero artwork, optional grants, display mode, timed carousel, recovery, recipes, callbacks, outro. Source checkout installation is shown; verify published Maven coordinates before production use.

Subscribe, comment with your edge case, star, share, contribute, or support ongoing work.
""")

write(OUT/"README.md",f"""# Android ApexFission Permissions content campaign

## 1. Campaign summary

**Goal:** turn qualified Android interest into documentation visits, GitHub stars, trial integrations, issues/discussions, contributions, and voluntary support. **Audience:** Compose developers, mobile teams, indie developers, and open-source contributors.

**Core promise:** explain ordinary runtime permissions in context, request missing access after a user action, and adapt grant/recovery behavior. Open source and free to use under [Apache 2.0]({REPO}/blob/main/LICENSE). The first release is still described as forthcoming in the checked-in README; publication copy must verify Maven availability before claiming an install coordinate.

**Editorial tone:** direct, helpful, beginner-friendly, technically precise. Show real library UI and emulator recordings; use the checked-in static screenshots only as labeled Compose previews. Avoid “one Android dialog,” “permanent denial detected,” or “all permissions work in a batch.”

**Links:** library repo {REPO}; campaign repo {CAMPAIGN_REPO}; docs {SITE}; [SUPPORT_URL: Patreon or other verified support page]; [VIDEO_URL: final upload]. Replace placeholders before scheduling. Do not invent a support destination.

**Measurement:** UTM-tagged docs visits by platform if approved; stars and forks relative to launch baseline; README-to-install traffic; demo opens; comments/questions, issues/PRs; support conversions. Review weekly and reply to technical questions within two working days.

## 2. Tutorial track plan

One [chaptered long video](tutorial/long-video/video.md) (16–20 minutes) with ten matching standalone shorts. Every chapter has one feature focus, an authentic demo, a source excerpt, and its own [post.md] companion. Release the long video first, then individual short clips. Shorts include local setup and a complete CTA.

| Section | Short | Primary proof |
| --- | --- | --- |
""" + "\n".join(f"| {i:02d} {t[1]} | [video](tutorial/{t[0]}/video.md) · [post](tutorial/{t[0]}/post.md) | {t[6]} |" for i,t in enumerate(TUTORIALS,1)) + f"""

## 3. Promo track plan

Eight [promo folders](promo/), each containing a 30–45 second six-beat script and platform-specific companion copy. Promo videos show UI and benefits only: **no code, no editor, no API declarations**. Each explicitly says open source and free under Apache 2.0 and ends with the complete CTA.

| Promo | Script and companion |
| --- | --- |
""" + "\n".join(f"| {p[1]} | [video](promo/{p[0]}/video.md) · [post](promo/{p[0]}/post.md) |" for p in PROMOS) + f"""

## 4. Long video script

[Full script, spoken chapters, demo notes, thumbnail, and outro](tutorial/long-video/video.md).

## 5. Short video scripts

Each tutorial and promo folder linked above contains video.md with timed beats, what is said, what is shown, caption, cover, and CTA. The ten tutorial shorts map one-to-one to the ten long-video chapters.

## 6. Written post drafts

Each video folder has post.md with LinkedIn, Facebook, Instagram, and Shorts/TikTok copy, media references, alt text, and cover guidance. The long video has a companion post and YouTube description.

## 7. Asset checklist and recording brief

- [x] Real official site capture in long-video/assets/site-home.jpg and promo asset folders.
- [x] Repo Compose fixture in long-video/assets/bundle-preview.jpg.
- [x] 18 edited UI post cards derived from checked-in screenshot fixtures (JPEG, 1080×1350).
- [x] 10 code cards rendered into JPEG directly from current README excerpts (1600×900); see tools/render_campaign_assets.py.
- [ ] Record sample app walkthrough, real Android prompts and Settings state on emulator. Label API/device. Static fixtures cannot show system prompts.
- [ ] Capture hero artwork demo and code-only demo, which have no checked-in screenshots; UI cards for those episodes are illustrative *other* library UI and must be replaced by actual footage.
- [ ] Record voiceover and burn readable captions; get [SUPPORT_URL], [VIDEO_URL], and final brand review. Use the same readable GitHub end card on all shorts.
- [ ] Before publishing, check release version, screenshots versus current UI, license, and support destination.

**Asset provenance:** docs/screenshots/README.md identifies the Compose screenshot workflow. site-home.jpg is a live capture of the official docs homepage on 2026-09-28. The post card overlays add titles and a provenance footer but do not claim to be a phone capture of Android prompts.

## 8. Posting schedule (America/Ciudad_Juarez)

Four weeks, three tutorial and two promo releases weekly after the long video; 18 shorts in total. Start on the next chosen Monday after editing approval. Suggested slots: long video Monday 10:00, shorts Tuesday/Thursday/Saturday 12:00, promos Wednesday/Friday 12:00. Publish companion posts the same day, then a LinkedIn summary 24 hours later. Cross-post vertical masters to YouTube Shorts, Instagram Reels, and TikTok; use the matching post.md for LinkedIn/Facebook/Instagram.

| Week | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Long tutorial + companion | T01 install | P01 explain first | T02 batch | P02 one action | T03 pages |
| 2 | Community replies / metrics | T04 artwork | P03 make it yours | T05 optional | P04 optional access | T06 display |
| 3 | Community replies / metrics | T07 timing | P05 partial grants | T08 recovery | P06 reading pace | T09 recipes |
| 4 | Community replies / metrics | T10 code-only | P07 settings recovery | Best Q&A excerpt [record if warranted] | P08 platform rules | Campaign recap |

**Platform adaptations:** YouTube long 16:9, 16–20 min, chapter links, pinned comment with repo and docs. Shorts/Reels/TikTok 9:16, 45–75 sec, captions in center safe region, UI zoomed to legible text; Instagram/TikTok quick hook and short voice lines. LinkedIn 4:5 still or native vertical clip with a practical engineering takeaway; Facebook clearer context and direct repo link; Instagram 4:5 carousel cover and link-in-bio instruction. Avoid unverified length ceilings; cut each short for clarity, then check the upload limits of the account at publish time.

**Review loop:** after week 1, compare 3-second retention, completion, saves, repo visits, and question themes. Reorder the remaining topics if actual audience questions indicate a stronger need, preserving technical accuracy and the required CTAs.
""")
print(f"Built {len(TUTORIALS)+len(PROMOS)+1} video folders in {OUT}")
