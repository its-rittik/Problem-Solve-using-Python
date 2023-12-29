# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 12:43:24 2023

@author: ritti
"""
n = int(input())

welfare_str = input()
welfare_list = welfare_str.split()
welfare_list = list(map(int ,welfare_list))

temp = max(welfare_list)
result = 0 

for i in range(n):
    result += (temp - welfare_list[i])

print(result)
    
    