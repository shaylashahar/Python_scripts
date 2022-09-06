##this file writes a dictionary with {bin:nodes}

import os
import pandas as pd

directory="Bins/"
bindict = {}
i=0
for file in os.listdir(directory):
    valuelist=[]
    key=file
    bindict[key]=file
    with open("./Bins/" + file, 'r') as f:
        contents = f.readlines()
        for line in contents: 
            if line.startswith(">"):
                line=line.replace(">", "")
                line=line.replace("\n", "")
                valuelist.append(line)
                bindict[file]=valuelist
#print(bindict)
final = pd.DataFrame({'MaxBins': (bindict.keys()), 'Contig_Nodes': list(bindict.values())})
final = final.explode(column='Contig_Nodes')
#newfinal = final.drop_duplicates(subset=['Contig_Nodes'])
final.to_csv('/Users/shayla/KelleyLab/BinnedBactAndArch.FASTA_SET1/out.csv')
