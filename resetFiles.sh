#!/bin/bash

rm refGenomeList.txt
rm metagenomeList.txt
rm mappingCombos.txt
if [ "$1" = "True" ]
then
	rm mappingResults/*
fi
rm resultingPIDs.txt
rm parsedPID.txt
rm coverage.txt
rm ani.txt
rm refGenomes.len
