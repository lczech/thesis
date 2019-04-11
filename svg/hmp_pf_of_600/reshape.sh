#!/bin/bash

# Shitty python plot tool outputs some weird svg that really slows inkscape down, 
# to the point where editing the multi panel plot was not longer possible. Crashes and stuff.
# So here, we simply replace the weird plotting stuff by plain old circles.

reshaped=${1/.svg/}_reshaped.svg
echo "${1} --> ${reshaped}"
cp ${1} ${reshaped}

perl -0777 -i.bak -pe 's/ *<g clip-path="url\(#[a-z0-9]*\)">\n *<use style="fill:#([a-f0-9]*);" x="([0-9\.]*)" xlink:href="#[0-9A-Za-z_]*" y="([0-9\.]*)"\/>\n *<\/g>/    <circle style="display:inline;overflow:visible;visibility:visible;opacity:1;fill:#$1;fill-opacity:1;fill-rule:nonzero;stroke:none" cx="$2" cy="$3" r="0.6" \/>/igs' ${reshaped}

rm ${reshaped}.bak

# scale factor for the jitter plots to make them the same size as the scatter plots: 116%
