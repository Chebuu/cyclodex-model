#!/bin/bash

idir=$1
odir=$2

for isdf in $(find $idir -type f -iname "*.cif"); do
  omol="$odir/$(basename $isdf .cif).mol2"
  babel -icif $icif -omol2 $omol
done