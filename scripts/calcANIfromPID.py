# coding: utf-8
import pandas as pd
import sys, os
__author__ = "Sarah Stevens"
__email__ = "sstevens2@wisc.edu"

def usage():
	print "Usage: calcANIfromPID.py PIDonlyFile"
	print "Calculates the ANI from a PIDonly file made by parsePID.py"

if len(sys.argv) != 2:
	usage()
	exit()

# Get argument
filename=sys.argv[1]
aniFileHeader='filename\tref\tmeta\thits\tANI\n'
regANILine='{}\t{}\t{}\t{}\t{}\n'
ref, _, meta=os.path.basename(filename).split('-')
meta=os.path.splitext(meta)[0]

if os.stat(filename).st_size == 0: #Checking to see if file is empty (which would happen if no reads recruited)
	if os.path.exists('ani.txt'):
		# Makes a ani file if none exists or writes line to existing one.
		with open('ani.txt','a') as outfile:
			outfile.write(regANILine.format(filename,ref,meta,'0', 'na')) #Records ani for 0 hits
	else:
		with open('ani.txt','a') as outfile:
			outfile.write(aniFileHeader)
			outfile.write(regANILine.format(filename,ref,meta,'0', 'na'))
else: #if file is not empty
	pid_df= pd.read_table(filename, header=None) #Read in file
	# Makes a ani file if none exists or writes line to existing one.
	if os.path.exists('ani.txt'):
		with open('ani.txt','a') as outfile:
			outfile.write(regANILine.format(filename,ref, meta, pid_df[3].count(), pid_df[3].mean()))
	else:
		with open('ani.txt','a') as outfile:
			outfile.write(aniFileHeader)
			outfile.write(regANILine.format(filename,ref, meta, pid_df[3].count(), pid_df[3].mean()))
