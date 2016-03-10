#!/bin/bash

rm refGenomeList.txt
rm metagenomeList.txt
rm mappingCombos.txt
if [ "$1" = "True" ]
then
	rm mappingResults/*.sam
fi
rm resultingPIDs.txt