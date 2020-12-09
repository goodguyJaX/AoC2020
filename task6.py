# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:36:15 2020

@author: jakas
"""

import fileinput
#102
group = []
p1 = 0
p2 = 0
A = []
for line in fileinput.input('input6.txt'):
    
    line = line.strip()
    
    if not line:  
        c1 = int(len(set(''.join(group))))
        for i in range(len(group)):
            g = group[i]
            if g == group[0] and i == 0:
                c2 = set(g)
            else:
                c2 = set(c2) & set(g)
        
        p2 += len(c2)
        p1 += c1
        A.append(group)
        group = []

    else:
        group.append(line)

print(p1)
print(p2)     
