#!/bin/bash

#runAll.py threads(default=10) memlimit(default=4g)

# Make list of all files ending in .f*a in refGenomes directory
ls refGenomes/*.f*a > refGenomeList.txt

# Make list of all files ending in .f*a metagenomes directory
ls metagenomes/*.f*a > metagenomeList.txt

# Python script that makes all of the combo's to map
python scripts/makeMappingCombos.py

# For every combination of reference and metagenome, if the output doesn't exist run the mapping
echo python scripts/runMapping.py mappingCombos.txt ${1-'10'} ${2-'4g'}
python scripts/runMapping.py mappingCombos.txt ${1-'10'} ${2-'4g'}
