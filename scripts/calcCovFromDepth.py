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

# Get argument
filename=sys.argv[1]
covFileHeader='filename\ref\meta\tbaseCovSum\tAvgCov\n'
regCovLine='{}\t{}\t{}\t{}\t{}\n'
ref, _, meta=os.path.basename(filename).split('-')
meta=os.path.splitext(meta)[0]

if os.stat(filename).st_size == 0: #Checking to see if file is empty (which would happen if no reads recruited)
	if os.path.exists('coverage.txt'):
		# Makes a coverage file if none exists or writes line to existing one.
		with open('coverage.txt','a') as outfile:
			outfile.write(regCovLine.format(filename,ref,meta,'0', '0')) #Records coverage 0
	else:
		with open('coverage.txt','a') as outfile:
			outfile.write(covFileHeader)
			outfile.write(regCovLine.format(filename,ref,meta,'0', '0'))
else: #if file is not empty
	depth_df= pd.read_table(filename, header=None) #Read in file
	covCol = len(depth_df.columns)-1 #Get last column number
	# Makes a coverage file if none exists or writes line to existing one.
	if os.path.exists('coverage.txt'):
		with open('coverage.txt','a') as outfile:
			outfile.write(regCovLine.format(filename,ref, meta, depth_df[covCol].sum(), depth_df[covCol].mean()))
	else:
		with open('coverage.txt','a') as outfile:
			outfile.write(covFileHeader)
			outfile.write(regCovLine.format(filename,ref, meta, depth_df[covCol].sum(), depth_df[covCol].mean()))
