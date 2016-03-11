## Mapping Oligotrophic Metagenomes to Reference Genomes
Sarah Stevens  
2016-03-10  

This pipeline calculates the coverage and ANI for each metagenome included to each reference Genome

### Directory Structure:
| - metagenomes/ : directory to place (or link) all the metagenomes to include in analysis
| - refGenomes/ : directory to place (or link) all the reference genomes to include in analysis
| - scripts/ : directory that contains scripts for analysis
| - mappingResults/ : directory that holds the resulting sam files from mapping
| - runAll.sh : script that runs pipeline
| - resetFiles.sh : script that removed intermediate files to reset the repo
| - setup.sh : setups the directory structure to start with

### Requirements
- Samtools
- BBMap
- Python 2.7.

### Setup
To set up the directory structure run
```
./setup.sh
```
Then:
	- place all the metagenomes(fasta type files) you are want to map in `metagenomes/`
	- place all of the reference genomes you want to map to in `refGenomes/`

### Running all mapping
Run all analysis using the following command:
```
./runAll.py threads memlimit
```
Arguments (very naive and only use positionals):
	- threads = number of threads to use (default=10)
	- memlimit = java memory limit for each mapping job (default=4g)
Makes nice logfiles with dates like this...  
```
nohup bash runAll.sh thread memlimit > $(echo $(date +%Y%m%d_%H%M%S))_nohup.log 2> $(echo $(date +%Y%m%d_%H%M%S))_nohup.err &
```
Example w/ 20 threads and 4g memory each
```
nohup bash runAll.sh 20 4g > $(echo $(date +%Y%m%d_%H%M%S))_nohup.log 2> $(echo $(date +%Y%m%d_%H%M%S))_nohup.err &
```

### Resetting files
To reset repo use:
```
./resetFiles.sh [mappingtoo?]
```
Arguments (very naive and only use positionals):
	- Optional mapping too option ('True' if you want to delete all complete .sam files)
