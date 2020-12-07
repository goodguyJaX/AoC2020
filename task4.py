# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:36:15 2020

@author: jakas
"""

import fileinput

#byr (Birth Year) - four digits; at least 1920 and at most 2002.
#iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#hgt (Height) - a number followed by either cm or in:
#If cm, the number must be at least 150 and at most 193.
#If in, the number must be at least 59 and at most 76.
#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#pid (Passport ID) - a nine-digit number, including leading zeroes.
#cid (Country ID) - ignored, missing or not.

P = []

for line in fileinput.input('input4.txt'): 
    P.append(line.strip())

new_P = ''
NEW_P = []

for i in range(len(P)):
    
    if P[i] == '':
        NEW_P.append(new_P)
        new_P = ''
    else:
        new_P = new_P + ' ' + P[i]

part1 = 0
valid1 = []
part2 = 0
valid2 = []

for passport in NEW_P:
    check1 = 0
    count = 0
    passport = passport[1:]
    for criteria in passport.split(' '):
        
        if 'byr' in criteria:
            check1 += 1
            if 1920 <= int(criteria[4:]) <= 2002:
                count += 1                
            
        if 'iyr' in criteria:
            check1 += 1
            if 2010 <= int(criteria[4:]) <= 2020:
                count += 1

        if 'eyr' in criteria:
            check1 += 1
            if 2020 <= int(criteria[4:]) <= 2030:
                count += 1

        if 'hgt' in criteria:
            check1 += 1
            if criteria[-2:] == 'cm':
                if 150 <= int(criteria[4:len(criteria) - 2]) <= 193:
                    count+=1
            elif criteria[-2:] == 'in':
                if 59 <= int(criteria[4:len(criteria) - 2]) <= 76:
                    count+=1

        if 'hcl' in criteria:
            check1 += 1
            if len(criteria[4:]) == 7 and criteria[4] == '#':
                count += 1

        if 'ecl' in criteria:
            check1 += 1
            if criteria[4:] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                count += 1

        if 'pid' in criteria:
            check1 += 1
            if len(criteria[4:]) == 9:
                count += 1

    if check1 == 7:
        part1 += 1
        valid1.append(passport)
        
    if count == 7:
        part2 += 1
        valid2.append(passport)
        
print(part1)                  
print(part2)
            
            
            
            
            