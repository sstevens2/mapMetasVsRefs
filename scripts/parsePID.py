# coding: utf-8
import os
__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

with open('resultingPIDs.txt') as f:
    pidfile = f.read().splitlines()

with open('parsedPID.txt','w') as outfile:
    for line in pidfile:
        filename=os.path.basename(line.split(':')[0])
        pid=line.split('YI:f:')[1]
        ref,_,meta=filename.split('-')
        outfile.write(filename+'\t'+ref+'\t'+meta+'\t'+pid+'\n')
