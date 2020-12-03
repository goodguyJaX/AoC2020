# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:36:15 2020

@author: jakas
"""

import sys
import fileinput

X = [line for line in fileinput.input('input3.txt')]

#slopes = [[3,1]]
slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

trees = 1

for slope in slopes:
    on_the_road = True
    tree = 0
    x = 0
    y = 0
    while on_the_road:
          
        x+=slope[0]
        y+=slope[1]
        
        if x > (len(X[y].strip()) - 1):
            x = x - len(X[y].strip())
        
        if X[y][x] == '#':
            tree += 1
        
        if y == (len(X) - 1):
            on_the_road = False
        
    trees = trees * tree
    
print(trees)
        
    