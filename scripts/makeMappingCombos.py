#!/usr/bin/python
# coding: utf-8

import os

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

if __name__ == "__main__":

    # Reading in lists of reference genomes and metagenomes
    with open("refGenomeList.txt", "r") as f:
        refGenList = f.read().splitlines()

    with open("metagenomeList.txt", "r") as f:
        metaList = f.read().splitlines()

    # Making file with all possible combos
    with open("mappingCombos.txt", "w") as outfile:
        for ref in refGenList:
            for meta in metaList:
                refbase = os.path.splitext(os.path.basename(ref))[0]
                metabase = os.path.splitext(os.path.basename(meta))[0]
                outname = "mappingResults/{}-vs-{}.bam".format(refbase, metabase)
                outfile.write("{}\t{}\t{}\n".format(ref, meta, outname))
