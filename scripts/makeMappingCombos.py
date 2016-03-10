# coding: utf-8
import os
with open('refGenomeList.txt','r') as f:
    refGenList = f.read().splitlines()
    
with open('metagenomeList.txt','r') as f:
    metaList = f.read().splitlines()

with open('mappingCombos.txt','w') as outfile:
    for ref in refGenList:
        for meta in metaList:
            refbase = os.path.splitext(os.path.basename(ref))[0]
            metabase = os.path.splitext(os.path.basename(meta))[0]
            outname = 'mappingResults/{}-vs-{}.sam'.format(refbase,metabase)
            outfile.write('{}\t{}\t{}\n'.format(ref,meta,outname))            
