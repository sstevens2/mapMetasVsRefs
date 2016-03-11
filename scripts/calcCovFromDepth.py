# coding: utf-8
import pandas as pd
import sys, os
__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: calcCovFromDepth depthfile"
	print "Calculates the coverage from a depthfile made by samtools"

if len(sys.argv) != 2:
	usage()
	exit()

# Read in depth file
filename=sys.argv[1]
depth_df= pd.read_table(filename, header=None)
covCol = len(depth_df.columns)-1 #Get last column number

# Makes a coverage file if none exists or writes line to existing one.
if os.path.exists('coverage.txt'):
	with open('coverage.txt','a') as outfile:
		outfile.write('{}\t{}\t{}\n'.format(filename,depth_df[covCol].sum(), depth_df[covCol].mean()))
else:
	with open('coverage.txt','a') as outfile:
		outfile.write('filename\tbaseCovSum\tAvgCov\n')
		outfile.write('{}\t{}\t{}\n'.format(filename,depth_df[covCol].sum(), depth_df[covCol].mean()))
