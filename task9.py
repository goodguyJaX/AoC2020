# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:36:15 2020

@author: jakas
"""

import fileinput

instruction = []

for line in fileinput.input('input9.txt'):
    instruction.append(line.strip())

preamble = 25
p1 = []
P2 =[]
p2 = []

for i in range(preamble,len(instruction)):
    check = []
    
    for k in range(i-preamble, i):
        for l in range(i-preamble-1, i):
            s = int(instruction[k]) + int(instruction[l])
            check.append(s)
            
    if int(instruction[i]) not in check:
        p1.append(instruction[i])
        break

p1 = int(p1[0])

for i in range(len(instruction)):
    suma = int(instruction[i])
    
    for k in range(i+1, len(instruction)):
        
        suma += int(instruction[k])
        
        if suma >= int(p1):
            break
    
    if suma == int(p1):
        for l in instruction[i:k]:
            P2.append(int(l))
        break

p2 = max(P2) + min(P2)

print(p1)
print(p2)  
        