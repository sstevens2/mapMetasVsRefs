# coding: utf-8
import os, sys
__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

#Usage check
def usage():
        print "Usage: parsePID.py rawPIDfile"
        print "rawPID file is the output of piping the sam file into grep for YI:f field"

if len(sys.argv) != 2:
        usage()
        exit()

#Read in input
filename=sys.argv[1]
outname=os.splitext(filename)[0]+".pidOnly"

with open(filename) as f:
    pidfile = f.read().splitlines()

with open(outname,'w') as outfile:
    for line in pidfile:
        pid=line.split('YI:f:')[1]
        ref,_,meta=filename.split('-')
        meta=os.path.splitext(meta)[0]
        outfile.write(filename+'\t'+ref+'\t'+meta+'\t'+pid+'\n')
