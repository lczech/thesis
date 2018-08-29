#!/usr/bin/Rscript

# Read pairwise emd dists mat and edge pca projection
kr_dists <- read.csv( file="emd.mat", sep=" ", head=FALSE )
proj <- read.csv( file="proj.csv", sep=",", head=FALSE )

# Read sample assignments
emd_ass <- read.csv( file="emd_assignments.csv", sep="\t", head=FALSE )
imb_ass <- read.csv( file="imbalance_assignments.csv", sep="\t", head=FALSE )

# Tests
#mds_mat <- cmdscale(kr_dists, add=TRUE)
#mds_mat <- wcmdscale(kr_dists)
#mds_mat <- monoMDS(kr_dists)

# Run PCA and MDS
pca_mat <- prcomp(kr_dists)
mds_mat <- cmdscale(kr_dists)

# Use gradient for nugent
nugent_col <- colorRampPalette(c('blue','red'))
nugent_pal <- nugent_col(6)[as.numeric(cut( proj$V4, breaks = 6))]
nugent_cuts <- c( "0", "2", "4", "6", "8", "10" )

# Use three colors for three clusters
rgb_pal <- colorRampPalette(c('#E41A1C', '#377EB8', '#4DAF4A'))
opb_pal <- colorRampPalette(c('#999999', '#984EA3', '#FF7F00'))
emd_pal <- rgb_pal(3)[as.numeric(cut( emd_ass$V2, breaks = 3))]
imb_pal <- opb_pal(3)[as.numeric(cut( imb_ass$V2, breaks = 3))]

# Make PCA graph
svg( "pca_emd.svg" )
plot( pca_mat$x[,1:2], pch=19, col=emd_pal )

svg( "pca_imb.svg" )
plot( pca_mat$x[,1:2], pch=19, col=imb_pal )

svg( "pca_nugent.svg" )
plot( pca_mat$x[,1:2], pch=19, col=nugent_pal )
legend("topright", nugent_cuts, col=nugent_col(6), pch=19 )

# Print MDS
MDS1 <- -mds_mat[, 1]
MDS2 <- mds_mat[, 2]

svg( "mds_emd.svg" )
plot( MDS1, MDS2, asp = 1, pch=19, col=emd_pal )

svg( "mds_imb.svg" )
plot( MDS1, MDS2, asp = 1, pch=19, col=imb_pal )

svg( "mds_nugent.svg" )
plot( MDS1, MDS2, asp = 1, pch=19, col=nugent_pal )
legend("topright", nugent_cuts, col=nugent_col(6), pch=19 )

# Print Edge PCA graph
EdgePC1 <- -proj$V2
EdgePC2 <- -proj$V3
svg( "epca_emd.svg" )
plot( EdgePC1, EdgePC2, pch=19, col=emd_pal )

svg( "epca_imb.svg" )
plot( EdgePC1, EdgePC2, pch=19, col=imb_pal )

svg( "epca_nugent.svg" )
plot( EdgePC1, EdgePC2, pch=19, col=nugent_pal )
legend("topright", nugent_cuts, col=nugent_col(6), pch=19 )
