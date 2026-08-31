#!/bin/bash
# Builds Icon.icns from logo.png using macOS's built-in sips/iconutil (no install needed).
# Run this ON YOUR MAC, from inside this folder: ./make_icon.sh
set -e

SRC="logo.png"
ICONSET="Icon.iconset"

if [ ! -f "$SRC" ]; then
  echo "logo.png not found in this folder." >&2
  exit 1
fi

rm -rf "$ICONSET"
mkdir "$ICONSET"

# logo.png is only 128x128, so sizes above that are upscaled by sips (a bit
# soft at 512/1024, but perfectly fine for a Dock/Finder icon).
sips -z 16 16     "$SRC" --out "$ICONSET/icon_16x16.png"      > /dev/null
sips -z 32 32     "$SRC" --out "$ICONSET/icon_16x16@2x.png"   > /dev/null
sips -z 32 32     "$SRC" --out "$ICONSET/icon_32x32.png"      > /dev/null
sips -z 64 64     "$SRC" --out "$ICONSET/icon_32x32@2x.png"   > /dev/null
sips -z 128 128   "$SRC" --out "$ICONSET/icon_128x128.png"    > /dev/null
sips -z 256 256   "$SRC" --out "$ICONSET/icon_128x128@2x.png" > /dev/null
sips -z 256 256   "$SRC" --out "$ICONSET/icon_256x256.png"    > /dev/null
sips -z 512 512   "$SRC" --out "$ICONSET/icon_256x256@2x.png" > /dev/null
sips -z 512 512   "$SRC" --out "$ICONSET/icon_512x512.png"    > /dev/null
sips -z 1024 1024 "$SRC" --out "$ICONSET/icon_512x512@2x.png" > /dev/null

iconutil -c icns "$ICONSET" -o Icon.icns
rm -rf "$ICONSET"
echo "Icon.icns creata."
