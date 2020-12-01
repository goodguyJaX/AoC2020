# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd


expense_report = pd.read_clipboard(header=None)
expense_report.columns = ['Entries']

'''part 1'''

#for index, entry in expense_report.iterrows():
#    
#    diff = 2020 - int(entry)
#    
#    if diff in expense_report.values:
#        result = int(entry) * diff
#        print(int(entry))
#        print(diff)
#        print(result)
#        break


'''part 2'''

for entry1 in expense_report.values:
    result = 0
    diff1 = 2020 - int(entry1)
    
    for entry2 in expense_report.values:
        diff2 = diff1 - int(entry2)
        
        if diff2 in expense_report.values:
            
            result = int(entry1) * int(entry2) * diff2
            print(int(entry1))
            print(int(entry2))
            print(diff2)
            print(result)
            break
    
    if result!=0:
        break
            
            