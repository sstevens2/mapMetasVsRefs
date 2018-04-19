## Mapping Oligotrophic Metagenomes to Reference Genomes
Sarah Stevens, Elizabeth McDaniel, Matthew Wolff   

This pipeline calculates the coverage and ANI for each metagenome included to each reference genome  

### Directory Structure:
| - metagenomes/ : directory to place (or link) all the metagenomes to include in analysis  
| - refGenomes/ : directory to place (or link) all the reference genomes to include in analysis  
| - scripts/ : directory that contains scripts for analysis  
| - mappingResults/ : directory that holds the resulting sam files from mapping  
| - runAll.sh : script that runs pipeline  
| - resetFiles.sh : script that removed intermediate files to reset the repo  
| - setup.sh : setups the directory structure to start with  
| - Readme.md : this helpful file

### Requirements
- Samtools
- BBMap
- Python 2.7
- Python Modules:
	- multiprocessing
	- pandas

### Setup
To set up the directory structure run
```
./setup.sh
```
Then:
 - place all the metagenomes(fasta type files) you are want to map in `metagenomes/`
 - place all of the reference genomes you want to map to in `refGenomes/`

### Running all mapping
To start you may need to open runAll.sh and set the `bbpath` variable to where the bbmap software is located (relative to this repo)  
Default it thinks that the bbmap directory is one above this and that the bbmap.sh is within that directory.  
Run all analysis using the following command:  
```
./runAll.py threads memlimit
```
Arguments (very naive and only use positionals):
 - threads = number of threads to use (default=10)
 - memlimit = java memory limit for each mapping job (default=4g)  

Makes nice logfiles with dates like this:  
```
nohup bash runAll.sh thread memlimit > $(echo $(date +%Y%m%d_%H%M%S))_nohup.log 2> $(echo $(date +%Y%m%d_%H%M%S))_nohup.err &
```
Example w/ 20 threads and 4g memory each:
```
nohup bash runAll.sh 20 4g > $(echo $(date +%Y%m%d_%H%M%S))_nohup.log 2> $(echo $(date +%Y%m%d_%H%M%S))_nohup.err &
```
Mapping default arguments (see [bbmap](https://wiki.gacrc.uga.edu/wiki/BBMap) for details):
 - idtag
 - minid=.8
 - threads=1 - **WARNING** this does **not** seem to limit it to 1 CPU.  If using shared resource, be the only one using it at that time.
 - nodisk
 - -Xmx4g (unless changed with runAll.sh argument)
To change these settings (change 'cmd=...' line in runMapping.py)

### Output files
- refGenomeList.txt - List of all the reference genomes runAll.sh last ran on  
- metagenomeList.txt - List of all the metagenomes runAll.sh last ran on  
- mappingCombos.txt - All of the combinations of mapping metagenomes to reference genomes that runAll.sh last ran on  
- mappingResults/ - directory that stores all of the mapping results files (.bam)  
	- \*.bam - all the output files from all the combinations of mapping metagenomes to reference genomes  

 - \*.depth - the resulting depth (for each base) for all of the  combinations of mapping metagenomes to reference genomes  

- resultingPIDs.txt - All the lines from the \*.bam (converted to sam) that contain the percent identity (PID) information  
- parsedPID.txt - All of the percent identity hits with the info about which file they came from which meta vs which reference
- coverage.txt - The number of reads that mapped from each metagenome to each reference genome and the average coverage of each base.


### Resetting files
To reset repo use:
```
./resetFiles.sh
```
If you want to remove the files form mappingResults, as well:
```
./resetFiles.sh True
```
