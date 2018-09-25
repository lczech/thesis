#!/bin/bash

rm -f dna.phy.dat.svg

/home/lucas/Software/pixel2svg-0.3.0/pixel2svg.py --overlap dna.phy.dat.bmp

sed -i 's/rgb(255,0,0)/#ff5789/g' dna.phy.dat.svg
sed -i 's/rgb(0,255,0)/#58a2ff/g' dna.phy.dat.svg
sed -i 's/rgb(255,255,0)/#94d87b/g' dna.phy.dat.svg
sed -i 's/rgb(0,0,255/#ffe558/g' dna.phy.dat.svg

# A red		ff5789ff
# C blue	58a2ffff
# G green	94d87bff
# T yellow	ffe558ff

