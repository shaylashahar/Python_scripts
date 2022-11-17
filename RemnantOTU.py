### This file reads large OTU table, filters for desired domain/kingdom 
### and merges to add counts

from operator import mod
import pandas as pd

### read in orig OTU, split by domain for bacteria and archaea
otu = pd.read_csv("/Users/shayla/Cayla-otu.csv")
#print(otu.head)
otu = otu.drop(["Unnamed: 0", "percent_identity"], axis=1)
otu['domain'] = otu['lineage'].str.split(';').str.get(0)
new_otu = otu.query("domain == 'Bacteria' | domain == 'Archaea'")
new_otu.to_csv("/Users/shayla/Cayla-otu_bact_arch.csv")
### read in euks OTU, filter for fungi kingdom 
euks = pd.read_csv("/Users/shayla/Cayla_Project/Cayla-otu_euks.csv")
euks["kingdom"] = euks['lineage'].str.split(';').str.get(1)
#print(euks["kingdom"].unique())
fung = euks.query("kingdom == 'Mucoromycota' | kingdom == 'Blastocladiomycota' | kingdom == 'Ascomycota' | kingdom == 'Basidiomycota' | kingdom == 'Zoopagomycota' | kingdom == 'Chytridiomycota' | kingdom == 'Microsporidia'")
fung.to_csv("/Users/shayla/Cayla_Project/Cayla-otu_fungi.csv")

### match columns of bact/arch with fungi 
bactarch = pd.read_csv("/Users/shayla/Cayla_Project/Cayla-otu_bact_arch.csv")
bactarch = bactarch.drop(['Unnamed: 0', 'gene_id', 'domain'], axis=1)
print(bactarch.columns)
fungi = pd.read_csv("/Users/shayla/Cayla_Project/Cayla-otu_fungi.csv")
fungi = fungi.drop(['Unnamed: 0.1', 'Unnamed: 0', 'gene_id', 'kingdom', 'domain'], axis=1)
print(fungi.columns)

### merge bach/arch with fungi and add count column
merged = pd.concat([bactarch, fungi], axis=0)
merged['Count']=1
print(merged.columns)
merged.to_csv("/Users/shayla/Cayla_Project/Cayla-otu_ToCount.csv")

### add counts for matching lineages 
merged = merged.groupby(['lineage', 'sample']).agg({"Count": "sum"})
merged.to_csv("/Users/shayla/Cayla_Project/Cayla-otu_final.csv")