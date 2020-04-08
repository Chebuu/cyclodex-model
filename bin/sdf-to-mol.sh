#!/bin/bash

# This scrip uses Open Babel to convert all .sdf files in a directory to 3D .mol2 files (single conformer)
# # The computed 3D coordinates are determined by bond order 
# # Description of flags:
# # -t Input is a single molecule
# # -c Center at (0,0,0)

idir=$1
odir=$2

for isdf in $(find $idir -type f -iname "*.sdf"); do
  omol="$odir/$(basename $isdf .sdf).mol2"
  babel --gen3d -isdf $isdf -omol2 $omol
done
