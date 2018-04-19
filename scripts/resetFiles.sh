#!/bin/bash
# remove data
rm refGenomeList.txt metagenomeList.txt mappingCombos.txt 2> /dev/null # throwaway error output
# conditionally empty mapping results
[ "$1" = "True" ] && rm mappingResults/* 2> /dev/null
# remove metadata
rm resultingPIDs.txt parsedPID.txt coverage.txt ani.txt refGenomes.len metaReads* 2> /dev/null
rm ani_* # don't know why these are being generated where they are
