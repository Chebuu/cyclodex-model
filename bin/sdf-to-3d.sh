#!/bin/bash

for isdf in $(find $1 -type f -iname "*.sdf"); do
  # $(obconformer 25 100 $isdf) > $isdf
  babel --gen3d -isdf $isdf -osdf $isdf # --partialcharge eem
done
