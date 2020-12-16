import pandas as pd
import os

# LOOKING FOR CSV FILE IN DIRECTORY
all_files = os.listdir() 
data_frames = []
first_file = True
out_file = 'merged.csv'
final_file = 'final_merged.csv'
for file in all_files:
    if file.endswith('.csv'):
        df = pd.read_csv(file)
        df = df.dropna()
        if first_file:
            df.to_csv(out_file, index=False) 
            first_file = False
        else:
            df.to_csv(out_file, index=False, header=False, mode='a')

merged = pd.read_csv(out_file)
no_duplcates = merged.drop_duplicates()
no_duplcates.to_csv(final_file, index=False)