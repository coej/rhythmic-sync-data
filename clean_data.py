#!/usr/bin/python

from __future__ import print_function
import os, csv

path = os.path.join(os.getcwd(), 'data_csv_raw')

allfiles = os.listdir(path)
csvfiles = [os.path.join(path, f) 
            for f in list(allfiles) 
            if os.path.splitext(f)[1]==".csv"]

new_dir = os.path.join(os.getcwd(), 'data_csv_cleaned')
if not os.path.exists(new_dir):
    os.makedirs(new_dir)

bad_csv_keywords = ['[', 'taskRunCount', 'end,end,end', 'IntervalOut,X,X,0']
csv_header = "taskRunCount,taskID,taskName,i,channel,pitch,velocity,microseconds"


for old_path in csvfiles:    
    
    new_path = os.path.join(new_dir, os.path.basename(old_path))    
    
    with open(old_path) as oldfile, open(new_path, 'w') as newfile:
        
        newfile.write(csv_header + '\n')        
        for linecount, line in enumerate(oldfile):
            if any(word in line for word in bad_csv_keywords):
                continue
            elif not line[0].isdigit():
                continue

            # fixing error in construction of some data rows and using
            # a numeric key to indicate a particular kind of timestamp
            line = line.replace("IntervalOut,X,X,", "9999,9999,9999,9999,")

            #standardizing CSV: no comma at end of line
            line = line.replace(',\n', '\n')
            assert line[-1] != ','

            newfile.write(line)
            
            
cleaned_path = os.path.join(os.getcwd(), 'data_csv_cleaned')

cleaned_csvfiles = [os.path.join(cleaned_path, f) 
                    for f in list(os.listdir(cleaned_path)) 
                    if os.path.splitext(f)[1]==".csv"]


#confirm proper structure
dlists = [list(csv.DictReader(open(f))) for f in cleaned_csvfiles]
assert all([dl[0].keys() == ['taskRunCount', 'i', 'microseconds', 'taskID',
                            'pitch', 'velocity', 'taskName', 'channel']
            for dl in dlists])
    
