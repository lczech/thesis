#!/bin/bash

for filename in `ls *.svg` ; do
	inkscape -D -z --file=${filename} --export-pdf=${filename//svg/pdf}
done
