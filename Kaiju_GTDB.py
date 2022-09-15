#This program loops through bacteria files, takes first acc#, finds tax ID,
# and outputs file with tax ID and protein sequence 

import os
import subprocess
from subprocess import check_output

directory = "./bacteria"
fout=open("proteins.faa", "w")
for file in os.listdir(directory): #loop through files
    with open("./bacteria/" + file) as f:
        #reads each file and finds accession number
        contents = f.readlines()
        first = contents[0].strip()
        per=first.find(".")
        acc= first[1:per]
        #uses accession number to search NCBI for taxid
        taxid = subprocess.check_output(f'efetch -db nuccore -id {acc} -format docsum | xtract -pattern DocumentSummary -element TaxId', shell=True)
        taxid = taxid.decode('utf-8')
        for line in contents: #writes new file with tax id followed by sequence 
            if line.startswith(">"):
                fout.write(">" + str(taxid))
            else:
                fout.write(line)


        
