#!/bin/sh

# Convert all arguments (assumed SVG) to a TIFF acceptable to PLOS
# Requires Inkscape and ImageMagick 6.8 (doesn't work with 6.6.9)

for i in $@; do
  BN=$(basename $i .svg)
  inkscape --without-gui --export-png="$BN.png" --export-dpi 600 $i
  convert -compress LZW -alpha remove $BN.png $BN.tiff
  mogrify -alpha off $BN.tiff
  rm $BN.png
done
