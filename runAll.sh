
#!/bin/bash

#nohup ./runAll.sh threads(default=10) memlimit(default=4g) > $(echo $(date +%Y%m%d_%H%M%S))_nohup.log 2> $(echo $(date +%Y%m%d_%H%M%S))_nohup.err &
# nohup bash runAll.sh 20 4g > $(echo $(date +%Y%m%d_%H%M%S))_nohup.log 2> $(echo $(date +%Y%m%d_%H%M%S))_nohup.err &
bbpath=../bbmap/bbmap.sh

# Make list of all files ending in .f*a in refGenomes directory
if [ ! -e refGenomeList.txt ]
then
	ls refGenomes/*.f*a > refGenomeList.txt
else
	echo "Using existing refGenomeList, use reset script or delete this file and run again to remake"
fi

# Make list of all files ending in .f*a metagenomes directory
if [ ! -e metagenomeList.txt ]
then
	ls metagenomes/*.f*a > metagenomeList.txt
else
	echo "Using existing metagenomeList, use reset script or delete this file and run again to remake"
fi

# Python script that makes all of the combo's to map
if [ ! -e mappingCombos.txt ]
then
	python scripts/makeMappingCombos.py
else
	echo "Using existing mappingCombos, use reset script or delete this file and run again to remake"
fi

# For every combination of reference and metagenome, if the output doesn't exist the mapping will run
echo python scripts/runMapping.py mappingCombos.txt $bbpath ${1-'10'} ${2-'4g'}
python scripts/runMapping.py mappingCombos.txt $bbpath ${1-'10'} ${2-'4g'}

#Parsing the PID out of the results
for filename in mappingResults/*.bam
do
        outname="${filename%.*}".pid
        if [  ! -e $outname ] && [[ $filename != *.sorted.bam ]]
        then
                samtools view $filename | grep 'YI:f:' > $outname
        else
                echo "${outname} exists, use reset scripts or delete this file to remake"
        fi
done

for filename in mappingResults/*.pid
do
        outname="${filename%.*}".pidOnly
        if [ ! -e $outname ] 
        then
                python scripts/parsePID.py $filename
        else
                echo "${outname} exists, use reset script or delete this file  to remake"
        fi
done

# Getting number of reads in metagenomes
if [ ! -e metaReads.txt ]
then
	for filename in metagenomes/*.fa*; do echo $filename >> metaReads.txt ; grep -c '>' $filename >> metaReads.txt; done
else
	echo "Using existing metaRead.txt, delete or reset to remake"
fi

# Calculating and putting together the ANI values
if [ ! -e ani.txt ]
then
        for filename in mappingResults/*.pidOnly; do python scripts/calcANIfromPID.py $filename; done
else
        echo "ANI file exists, use reset script or delete this file to remake"
fi

# Getting the coverage out of the sam files and converting to sorted bam
# Making depth files for each
for filename in mappingResults/*.bam
do
        if [ ! -e $filename.sorted ] && [[ $filename != *.sorted.bam ]]
        then
                samtools sort $filename $filename.sorted
        else
                echo "${filename}.sorted exists, use reset script or delete to remake"
        fi
done

for filename in mappingResults/*sorted.bam
do
	outname="${filename%.*}".depth
	if [ ! -e $outname ]
	then
		samtools depth "$filename" > "$outname"
	else
		echo "${outname} exists use reset script or delete this file and run again to remake"
	fi
done

## Getting size of genomes
for filename in refGenomes/*.fna
do
	if [ ! -e $filename.len ]
	then
		python scripts/countbasesFNA.py $filename
	else
		echo "Length already calculated for ${filename}"
	fi
done
if [ ! -e refGenomes.len ]
then
	cat refGenomes/*.len > refGenomes.len
else
	echo "Using created refGenomes.len delete or reset if you need to remake"
fi


# Write python script to parse depth files
if [ ! -e coverage.txt ]
then
	for filename in mappingResults/*.depth; do python scripts/calcCovFromDepth.py $filename; done
else
	echo "Coverage file exists, use reset script or delete this file and run again to remake"
fi
