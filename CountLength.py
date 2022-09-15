##this file counts the length of each node in a bin and writes a file with each bin, node, node length, and total bin length

import os 

directory = './BinnedBactAndArch.FASTA_SET1/Bins'
fout = open('BinCounter.txt', 'w')
#loops through directory of bin files 
for file in os.listdir(directory):
    total = 0
    with open('./BinnedBactAndArch.FASTA_SET1/Bins/' + file, 'r') as f:
        fout.write(file  + '\n')
        contents = f.readlines()
        #writes file with node followed by length of contig
        for line in contents:
            if line.startswith('>'):
                fout.write(line)
            else:
                length = len(line)
                #fout.write(line)
                total = total + length
                fout.write(str(length) + '\n')  
        #ends each bin chunk with total length 
        fout.write(file + " total " +str(total))
        fout.write('\n' + '\n')s
