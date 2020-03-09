#!/bin/bash

cd $1

for pdb in $(find . -type f -iname "*.pdb" -d 1); do
  pdbio=$(basename $pdb)
  pdbfixer $pdbio --ph=5.0 --add-atoms=all
  cat output.pdb > $pdbio && rm -rf output.pdb
  pdb4amber $pdbio -o $pdbio
done