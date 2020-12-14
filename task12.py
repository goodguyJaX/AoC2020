# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:36:15 2020

@author: jakas
"""

import fileinput

instruction = []

for line in fileinput.input('input12.txt'):
    instruction.append(line.strip())

direction_dict = {'N' : 0,
                  'E' : 1,
                  'S' : 2,
                  'W' : 3}

def rotate(direction, ins, magnitude):
    current_direction = direction_dict[direction]
    
    rotation = magnitude / 90
    if ins == 'R':
        new_direction = (current_direction + rotation) % 4
    else:
        new_direction = (current_direction - rotation) % 4
    
    new_direction = list(direction_dict.keys())[list(direction_dict.values()).index(new_direction)]

    return new_direction

x = 0
y = 0
direction = 'E'

for ins in instruction:
    action = ins[0]
    magnitude = int(ins[1:])
    
    if action == 'R' or action == 'L':
        direction = rotate(direction, action, magnitude)
    
    if action == 'F':
        action = direction
    
    if action == 'N':
        y += magnitude
    if action == 'E':
        x += magnitude
    if action == 'S':
        y -= magnitude
    if action == 'W':
        x -= magnitude

p1 = abs(x) + abs(y)
print(p1)

'''PART2'''
xx = 10
yy = 1
x = 0
y = 0

def rotate_way(xx, yy, action, magnitude):
    if action == 'R':
        if magnitude == 90:
            new_xx = yy
            new_yy = -xx
        elif magnitude == 180:
            new_xx = -xx
            new_yy = -yy
        elif magnitude == 270:
            new_xx = -yy
            new_yy = xx
    
    if action == 'L':
        if magnitude == 90:
            new_xx = -yy
            new_yy = xx
        elif magnitude == 180:
            new_xx = -xx
            new_yy = -yy
        elif magnitude == 270:
            new_xx = yy
            new_yy = -xx
    
    return new_xx, new_yy

for ins in instruction:
    action = ins[0]
    magnitude = int(ins[1:])
    
    if action == 'R' or action == 'L':
        xx, yy = rotate_way(xx, yy, action, magnitude)
    
    if action == 'F':
        x += (magnitude * xx)
        y += (magnitude * yy)
    
    if action == 'N':
        yy += magnitude
    if action == 'E':
        xx += magnitude
    if action == 'S':
        yy -= magnitude
    if action == 'W':
        xx -= magnitude
    
p2 = abs(x) + abs(y)
print(p2)      
