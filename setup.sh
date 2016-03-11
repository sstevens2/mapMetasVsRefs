#!/bin/bash

[ -d "metagenomes" ] && echo "metagenome directory already exists" || mkdir metagenomes
[ -d "refGenomes" ] && echo "refGenome directory already exists" || mkdir refGenomes
[ -d "mappingResults" ] && echo "mappingResults directory already exists" || mkdir mappingResults