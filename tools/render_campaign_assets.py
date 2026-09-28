#!/usr/bin/env python3
"""Render campaign code cards from a sibling library checkout and authentic post images.

Usage: clone the library beside this promo repo, then python3 tools/render_campaign_assets.py
Requires Pillow. All inputs are local, and output is deterministic JPEG.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / "android.apexfission.permissions"
CAMPAIGN = ROOT / "campaign" / "2026-permissions-launch"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

def font(size, mono=False):
    return ImageFont.truetype(MONO if mono else FONT, size)

def card(title, source, needle, output, lines=13):
    raw = (SOURCE / source).read_text().splitlines()
    start = next(i for i, line in enumerate(raw) if needle in line)
    # Keep each excerpt inside the original Kotlin fence when reading the README.
    left = max((i for i in range(start+1) if raw[i].startswith('```')), default=-1)
    right = next((i for i in range(start+1, len(raw)) if raw[i].startswith('```')), len(raw))
    in_fence = left >= 0 and raw[left].startswith('```kotlin') and start < right
    first = max(left+1 if in_fence else 0, start-2)
    last = min(right if in_fence else len(raw), first+lines)
    excerpt = raw[first:last]
    # Trim indent while keeping relative indentation in the actual repository.
    indent = min((len(s)-len(s.lstrip()) for s in excerpt if s.strip()), default=0)
    excerpt = [s[indent:].expandtabs(4) for s in excerpt]
    width, height = 1600, 900
    image = Image.new("RGB", (width, height), "#111c20")
    d = ImageDraw.Draw(image)
    d.rounded_rectangle((74, 70, 1526, 822), radius=34, fill="#1d3033", outline="#446660", width=3)
    d.text((126, 112), "APEXFISSION  /  SOURCE", font=font(25), fill="#80d8bd")
    d.text((126, 166), title, font=font(45), fill="white")
    d.line((126, 236, 1474, 236), fill="#426d65", width=2)
    for index, row in enumerate(excerpt):
        if index >= 14: break
        row = row[:78]
        color = "#93e0ca" if re.search(r"\b(fun|val|class|implementation|HandlePermissions|PermissionDescription)\b", row) else "#e7eeee"
        d.text((130, 264+index*37), f"{first+index+1:>3}  {row}", font=font(24, True), fill=color)
    d.text((126, 776), source, font=font(20, True), fill="#bdd0ce")
    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output, "JPEG", quality=91, optimize=True)

def ui_card(title, source, output, subtitle):
    original = Image.open(source).convert("RGB")
    canvas = Image.new("RGB", (1080, 1350), "#12312c")
    d = ImageDraw.Draw(canvas)
    d.text((70, 55), "APEXFISSION PERMISSIONS", font=font(29), fill="#a7ebd4")
    d.text((70, 105), title, font=font(47), fill="white")
    fitted = ImageOps.contain(original, (610, 1000))
    canvas.paste(fitted, ((1080-fitted.width)//2, 200))
    d.text((70, 1245), subtitle[:55], font=font(24), fill="#c3ded7")
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output, "JPEG", quality=90, optimize=True)

CODE = {
  "01-install": ("Install from a source checkout", "README.md", "implementation(project(\":permission\"))"),
  "02-batch": ("One action, a group of requests", "README.md", "HandlePermissions("),
  "03-pages": ("Overview and custom pages", "README.md", "NarrationPermissionPage(narrationTitle"),
  "04-artwork": ("Hero artwork is independent", "README.md", "heroImage = R.drawable.scan_hero"),
  "05-optional": ("Required and optional access", "README.md", "required = false)"),
  "06-display": ("Choose visible permission pages", "README.md", "displayMode = PermissionDisplayMode.All"),
  "07-timing": ("Opt-in timed carousel", "app/src/main/java/com/apexfission/android/permissions/demo/PermissionCarouselDemo.kt", "autoAdvance = true"),
  "08-recovery": ("Settings recovery", "README.md", "recoveryContent = { inferredPermissions"),
  "09-recipes": ("Platform-aware steps", "README.md", "PermissionRecipes.foregroundLocation"),
  "10-code-only": ("Request without library UI", "README.md", "private val permissionRequester = PermissionRequester(this)"),
}
for slug, (title, src, needle) in CODE.items():
    card(title, src, needle, CAMPAIGN / "tutorial" / slug / "assets" / "code.jpg")

VISUALS = {
    "01-install": "bundle-overview", "02-batch": "bundle-overview",
    "03-pages": "permission-detail", "04-artwork": "permission-detail",
    "05-optional": "permission-detail", "06-display": "multiple-without-overview",
    "07-timing": "segmented-reading-progress", "08-recovery": "settings-recovery",
    "09-recipes": "bundle-overview", "10-code-only": "single-permission-overview",
}
PROMOS = {
    "01-explain-first": ("Explain before asking", "bundle-overview"),
    "02-one-action": ("One action for a group", "permission-detail"),
    "03-make-it-yours": ("Make the page yours", "permission-detail"),
    "04-optional-access": ("Optional means optional", "permission-detail"),
    "05-partial-grants": ("A partial grant is normal", "settings-recovery"),
    "06-reading-pace": ("Give people reading time", "segmented-reading-progress"),
    "07-settings-recovery": ("A recovery path", "settings-recovery"),
    "08-platform-rules": ("Respect platform rules", "bundle-overview"),
}
for slug, screenshot in VISUALS.items():
    ui_card(CODE[slug][0], SOURCE / "docs" / "screenshots" / (screenshot+".png"),
            CAMPAIGN / "tutorial" / slug / "assets" / "ui-post.jpg", "Library Compose preview · system prompts differ")
for slug, (title, screenshot) in PROMOS.items():
    ui_card(title, SOURCE / "docs" / "screenshots" / (screenshot+".png"),
            CAMPAIGN / "promo" / slug / "assets" / "ui-post.jpg", "Library Compose preview · system prompts differ")
