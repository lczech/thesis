
copied from /home/lucas/Projects/gappa_tests/normalization/dispersion
created using this script:


SAMPLES=/home/lucas/Projects/gappa_tests/03_epa/*/*.jplace
BASEDIR=/home/lucas/Projects/gappa_tests/normalization
GAPPA=/home/lucas/github/gappa/bin/gappa

#SAMPLES=${BASEDIR}/samples_jplace
SAMPLES="/home/lucas/Projects/bacardi/03_bv/03_epa/orig_queries_jplace_clean/"

#rm -rf ${BASEDIR}/dispersion/*

${GAPPA} analyze dispersion --jplace-path ${SAMPLES} --write-svg-tree --svg-tree-ladderize --out-dir ${BASEDIR}/dispersion/ --tree-file-prefix disp_rel_ --mass-norm relative
${GAPPA} analyze dispersion --jplace-path ${SAMPLES} --write-svg-tree --svg-tree-ladderize --out-dir ${BASEDIR}/dispersion/ --tree-file-prefix disp_abs_ --mass-norm absolute

