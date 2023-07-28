#The goal of this code is to take two Excel files, compare them, identify differences and and create new file which outline this differences.

import pandas as pd

# Read in the two files
file1 = pd.read_excel('C:/Users/EriksEriksons/OneDrive - WorldHarbour/Desktop/Personal Review Files/Python Code/Group Incomestatement_BUD Unposted by CC DET.xlsx')
file2 = pd.read_excel('C:/Users/EriksEriksons/OneDrive - WorldHarbour/Desktop/Personal Review Files/Python Code/Group Incomestatement_FC Unposted by CC DET.xlsx')

# Merge the two files based on the same first column
merged = pd.merge(file1, file2, on=file1.columns[0], how = 'outer', suffixes = ('_file1', '_file2'), indicator = True)

# Filter for rows that are only in the second file
diff = merged[merged['_merge'] == 'left_only']

# Write the difference to a new file
diff.to_excel('C:/Users/EriksEriksons/OneDrive - WorldHarbour/Desktop/Personal Review Files/Python Code/diff2.xlsx', index = False)