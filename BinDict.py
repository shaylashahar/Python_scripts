##this file writes a dictionary with {bin:nodes}

import os
import pandas as pd

directory="Bins/"
bindict = {}
i=0
#loop through directory of bins
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
#turning dictionary into DF to merge with data from Salmon
final = pd.DataFrame({'MaxBins': (bindict.keys()), 'Contig_Nodes': list(bindict.values())})
final = final.explode(column='Contig_Nodes')
final.to_csv('/Users/shayla/KelleyLab/DictOut.csv')
