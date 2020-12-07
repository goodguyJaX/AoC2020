# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:36:15 2020

@author: jakas
"""

import fileinput
import math as m

BS = []
seats = []
IDs = []

for line in fileinput.input('input5.txt'):
    BS.append(line.strip())

for bs in BS:
    
   r0 = 0
   rf = 127
   s0 = 0
   sf = 7
   
   for i in range(len(bs)):
        
        if bs[i] == 'F':
            rf = rf - m.ceil((rf-r0) / 2)
        if bs[i] == 'B':
            r0 = r0 + m.ceil((rf - r0) / 2)
        if bs[i] == 'L':
            sf = sf - m.ceil((sf-s0) / 2)
        if bs[i] == 'R':
            s0 = s0 + m.ceil((sf - s0) / 2)
            
   seats.append((r0, s0))
    
   for seat in seats:
       
       ID = seat[0] * 8 + seat[1]
       IDs.append(ID)


for i in range(1, 127):
    for j in range(8):
        ID = i * 8 + j
        
        if ID-1 in IDs and ID+1 in IDs and ID not in IDs:
            mySeat_xy = (i, j)
            mySeat = ID
       
print(max(IDs))
print(mySeat)
print(mySeat_xy)
