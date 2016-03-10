#!/usr/bin/python

import sys, os, subprocess
from multiprocessing import Pool

def usage():
	print "Usage: runmapping.py combolist threads(int) memlimitPerjob"

if len(sys.argv) != 4:
	usage()
	exit()

with open(sys.argv[1],'r') as f:
	combolist = f.read().splitlines()
threads=int(sys.argv[2])
memlimit=sys.argv[3]

def run_mapping(params):
	reffile, metafile, outfile = params.split('\t')
	if not os.path.exists(outfile):
		cmd = ["../bbmap/bbmap.sh", "ref="+reffile,"in="+metafile,"outm="+outfile,"idtag","minid=.8","threads=1","bandwidthratio=.8","nodisk","-Xmx"+memlimit]
		#print ' '.join(cmd), os.getpid()
		subprocess.call(cmd)
	else:
		print('Skipping {} as result file already exists, delete to rerun'.format(outfile))


if __name__ == '__main__':
	p=Pool(threads)
	p.map(run_mapping,combolist)
	p.close()