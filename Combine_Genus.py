##This file combines genus and outputs df with combined counts 

from operator import mod
import pandas as pd 

original_df = pd.read_csv("/Users/shayla/MetagenomeOTUs/soil_OTU_bacteria.csv")
mod_df = original_df.dropna(how='any', subset=['genus'])
final_df = mod_df.groupby('genus').sum()
final_df.to_csv("/Users/shayla/MetagenomeOTUs/GENUS_soil_OTU_bacteria.csv")

