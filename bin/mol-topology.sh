#!/bin/bash
idir=$1
odir=$2

for imol in $(find $idir -type f -iname "*.mol2"); do
  omol=$odir/$(basename $isdf)
  cp $imol $omol
  antechamber -i $imol -o $omol.ac.mol2 -fi mol2 -fo mol2 -c bcc -pf yes -eq 2 -at gaff2 -j 4
  parmchk2 -i $imol.ac.mol2 -f mol2 -o $omol.frcmod -s 2
done
