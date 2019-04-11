#!/bin/bash

# e41a1c red
# 377eb8 blue
# 4daf4a green
# 984ea3 purple
# e6ab02 yellow
# 17bbb3 cyan

sed -i '
s/#e41a1c;/#_____4daf4a_____;/g
s/#4daf4a;/#_____e41a1c_____;/g
s/#984ea3;/#_____17bbb3_____;/g
s/#17bbb3;/#_____984ea3_____;/g
s/_____//g
' multi_factors_tree.svg
