import pandas as pd
import os

# LOOKING FOR CSV FILE IN DIRECTORY
all_files = os.listdir() 
csv_files = []
for file in all_files:
    if file.endswith('.csv'):
        csv_files.append(file) 
print(csv_files)