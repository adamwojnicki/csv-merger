import pandas as pd
import os
import time

# INITIAL SETTINGS
first_file = True
out_file = 'merged.csv'
final_file = 'final_merged.csv'
print('Reading .csv files...')
all_files = os.listdir() 
# APPENDING DATA TO NEW CSV FILE
for file in all_files:
    if file.endswith('.csv') and not file.endswith('merged.csv'):
        print(f'Merging {file}')
        df = pd.read_csv(file)
        df = df.dropna()
        if first_file:
            df.to_csv(out_file, index=False) 
            first_file = False
        else:
            df.to_csv(out_file, index=False, header=False, mode='a')

# CLEARING FROM DUPLACATES
print(f'Saving merged data to {out_file}')
merged = pd.read_csv(out_file)
print('Clearing duplicated data...')
no_duplcates = merged.drop_duplicates()
print(f'Saving final data to {final_file}')
no_duplcates.to_csv(final_file, index=False)
print('ALL DONE!')
time.sleep(5)
