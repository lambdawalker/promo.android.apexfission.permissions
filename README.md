# Android ApexFission Permissions — content campaign

Production scripts, companion posts, and image assets for promoting the open-source [Android ApexFission Permissions library](https://github.com/lambdawalker/android.apexfission.permissions). The library is free to use under Apache 2.0. Its [documentation site](https://lambdawalker.github.io/android.apexfission.permissions/) covers integration and the public API.

**Start with the [campaign overview](campaign/2026-permissions-launch/README.md).** It contains the four-week schedule, platform adaptations, asset checklist, and links to each episode.

| Track | Deliverables |
| --- | --- |
| [Long tutorial](campaign/2026-permissions-launch/tutorial/long-video/video.md) | Chaptered 16–20 minute script, [companion post](campaign/2026-permissions-launch/tutorial/long-video/post.md), official site capture, and a Compose preview |
| [Tutorial shorts](campaign/2026-permissions-launch/tutorial/) | Ten standalone shorts, one per feature section; each folder has `video.md`, `post.md`, and `assets/` |
| [Promo shorts](campaign/2026-permissions-launch/promo/) | Eight benefit-led, no-code scripts with matching posts and UI assets |

The screenshots in `assets/` come from the library's checked-in **Compose previews**. They do not depict Android's system permission dialogs. Shoot real emulator footage for permission prompts, the sample app transitions, and the Settings route before publishing video. Some episode cards use a related library screen until that specific demo has been recorded; the [asset checklist](campaign/2026-permissions-launch/README.md#7-asset-checklist-and-recording-brief) identifies those cases.

Before publishing, replace `[SUPPORT_URL]` and `[VIDEO_URL]`, confirm the current Maven release coordinate, and review the final brand tone. The scripts currently use a practical developer-advocate voice.

## Regenerating the campaign

The checked-in Markdown is the editable deliverable. `tools/build_campaign.py` regenerates it from the campaign copy data. It overwrites edits to generated Markdown, so change the script or back up hand edits first. `tools/render_campaign_assets.py` renders code cards and UI cards from a sibling checkout of the library; install Pillow in your Python environment and run it from the repo root:

```bash
git clone https://github.com/lambdawalker/android.apexfission.permissions.git ../android.apexfission.permissions
python3 tools/build_campaign.py
python3 tools/render_campaign_assets.py
```

The original cards were rendered against library commit `534136a` and the official documentation homepage was captured on 2026-09-28. The asset renderer reads the sibling checkout's current state; check it out to `534136a` to reproduce those source excerpts exactly. It does not recapture the site homepage.
