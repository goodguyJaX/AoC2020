# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:36:15 2020

@author: jakas
"""

import fileinput

instruction = []

for line in fileinput.input('input8.txt'):
    instruction.append(line.strip())

p1 = []
p2 = []

for k in range(len(instruction)):
    ins = []

    for line in fileinput.input('input8.txt'):
        ins.append(line.strip())
        
    first_iteration = True
    I = []
    i = 0
    accumulator = 0
    
    change = 0
    
    if 'acc' in ins[k]:
        pass
    if 'jmp' in ins[k]:
        ins[k] = ins[k].replace('jmp', 'nop')
        change = 1
    if 'nop' in ins[k] and change != 1:
        ins[k] = ins[k].replace('nop', 'jmp')
        
    while first_iteration:
        
        I.append(i)
        action, number = ins[i].split()
     
        if action == 'acc':
            i += 1
            accumulator += int(number)
        
        if action == 'jmp':
            i += int(number)
            
        if action == 'nop':
            i += 1
        
        if i in I or i >= len(instruction):
            first_iteration = False
            
        if k == 0 and first_iteration == False:
            p1.append(accumulator)
        
        if i == len(instruction):
            p2.append(accumulator)

print(p1)
print(p2)
    
    
