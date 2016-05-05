#!/usr/bin/python

import sys, os, subprocess
from multiprocessing import Pool

__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: runmapping.py combolist bbpath threads(int) memlimitPerjob minID(ex:.8=80%)"

if len(sys.argv) != 6:
	usage()
	exit()

with open(sys.argv[1],'r') as f:
	combolist = f.read().splitlines()
bbpath=sys.argv[2]
threads=int(sys.argv[3])
memlimit=sys.argv[4]
minID=sys.argv[5]


def run_mapping(params):
	reffile, metafile, outfile = params.split('\t')
	if not os.path.exists(outfile):
		cmd = [bbpath, "ref="+reffile,"in="+metafile,"outm="+outfile,"idtag","minid="+minID,"threads=1","nodisk","-Xmx"+memlimit]
		#print ' '.join(cmd), os.getpid()
		subprocess.call(cmd)


if __name__ == '__main__':
	p=Pool(threads)
	p.map(run_mapping,combolist)
	p.close()
