# -*- coding: utf-8 -*-
import zipfile
import shutil
import os
import re
import glob

base = r"c:\Users\a\Cowork.test"
pptx_path = os.path.join(base, "知的財産権とは.pptx")
extract_dir = os.path.join(base, "_pptx_temp")
output_path = pptx_path  # overwrite original

# Clean up and extract
if os.path.exists(extract_dir):
    shutil.rmtree(extract_dir)
with zipfile.ZipFile(pptx_path, 'r') as z:
    z.extractall(extract_dir)

TARGET_FONT = "ＭＳ Ｐゴシック"

# 1. Fix theme - change latin fonts and Japanese font
theme_path = os.path.join(extract_dir, "ppt", "theme", "theme1.xml")
with open(theme_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Change latin typeface from Calibri to MS Gothic
content = content.replace('typeface="Calibri"', f'typeface="{TARGET_FONT}"')
content = content.replace('typeface="MS ゴシック"', f'typeface="{TARGET_FONT}"')
content = content.replace('typeface="ＭＳ ゴシック"', f'typeface="{TARGET_FONT}"')

with open(theme_path, 'w', encoding='utf-8') as f:
    f.write(content)

# 2. Fix all slide XML files - add explicit font run properties
slide_dir = os.path.join(extract_dir, "ppt", "slides")
for slide_file in glob.glob(os.path.join(slide_dir, "slide*.xml")):
    with open(slide_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add rPr with font to every <a:r> text run that doesn't have one
    # Replace <a:r><a:t> with <a:r><a:rPr lang="ja-JP" dirty="0"><a:latin typeface="MS ゴシック"/><a:ea typeface="MS ゴシック"/></a:rPr><a:t>
    content = re.sub(
        r'<a:r><a:t>',
        f'<a:r><a:rPr lang="ja-JP" dirty="0"><a:latin typeface="{TARGET_FONT}"/><a:ea typeface="{TARGET_FONT}"/></a:rPr><a:t>',
        content
    )

    # Also update existing rPr that already have font specs
    # Add/replace latin and ea typeface in existing rPr elements
    content = re.sub(
        r'<a:latin typeface="[^"]*"',
        f'<a:latin typeface="{TARGET_FONT}"',
        content
    )
    content = re.sub(
        r'<a:ea typeface="[^"]*"',
        f'<a:ea typeface="{TARGET_FONT}"',
        content
    )

    with open(slide_file, 'w', encoding='utf-8') as f:
        f.write(content)

# 3. Fix slide layouts and slide master too
for xml_dir in ["ppt/slideLayouts", "ppt/slideMasters"]:
    full_dir = os.path.join(extract_dir, xml_dir.replace("/", os.sep))
    for xml_file in glob.glob(os.path.join(full_dir, "*.xml")):
        with open(xml_file, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r'<a:latin typeface="[^"]*"', f'<a:latin typeface="{TARGET_FONT}"', content)
        content = re.sub(r'<a:ea typeface="[^"]*"', f'<a:ea typeface="{TARGET_FONT}"', content)
        with open(xml_file, 'w', encoding='utf-8') as f:
            f.write(content)

# 4. Repackage as pptx
with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(extract_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, extract_dir)
            zf.write(file_path, arcname)

# Cleanup
shutil.rmtree(extract_dir)

print("Done! Font changed to ＭＳ Ｐゴシック")
