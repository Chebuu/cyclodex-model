#!/bin/bash

idir=$1
iref=$2

for imol in $(find $idir -type f -iname "*.mol2"); do
  obfit '*' $iref $imol > $imol
done
