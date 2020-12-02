# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 17:29:16 2020

@author: jakas
"""

import sys
import fileinput

X = [line for line in fileinput.input('input2.txt')]

count1=0
count2=0

for x in X:
    policy = x.split(':')[0]
    policy_min = int(policy.split('-')[0])
    policy_max = int((policy.split('-')[1]).split(' ')[0])
    policy_letter = (policy.split('-')[1]).split(' ')[1]
    password = x.split(':')[1].replace(' ', '').replace('\n', '')
    
    if len(policy_min * policy_letter) <= password.count(policy_letter) and len(policy_max * policy_letter) >= password.count(policy_letter):
        count1+=1
    if len(password) >= policy_max:
        if (password[policy_min-1]==policy_letter and password[policy_max-1]!=policy_letter) or (password[policy_min-1]!=policy_letter and password[policy_max-1]==policy_letter):
            count2+=1
            
print(count1)
print(count2)
