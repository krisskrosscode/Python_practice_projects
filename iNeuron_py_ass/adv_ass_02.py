#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 08:29:38 2022

@author: harshal
"""

#%% Q1)
pentagonal_list = [1]

def pentagonal(n):
    ans = 1
    if n == 1:
        return ans
    for i in range(2, n+1):
        ans = ans + 5*(i-1)
        
    return ans
        
print("Ans 1 : Pentagonal List: ",pentagonal(8))

#%% Q2)

def encrypt(string):
    chart = {'a':'0', 'e':'1', 'i':'2', 'o':'2', 'u':'3' }
    reverse = string[::-1]
    
    for i in reverse:
        if i in chart.keys():
            reverse = reverse.replace(i, chart[i])
    
    return reverse + 'aca'

print("Ans 2 : Encryption : ",encrypt('apple'))

#%% Q3)
import datetime

def has_friday_13(m, y):
    if datetime.date(y,m,13).weekday() == 4:
        return True
    return False

print("Ans 3 : has_friday_13 : ",has_friday_13(3, 2020))


#%% Q4)
import re
lst = ["bad cookie", "good cookie", "bad cookie", "good cookie", "good cookie"]
string = ",".join(lst)

p = re.compile(r'\bbad')

z = re.findall(p, string)
print("Ans 4 : Bad Cookies", len(z))

#%%
ip = ["chair", "pencil", "arm"]

def pluralize(lst):
    ans = []
    for i in lst:
        if lst.count(i) > 1:
            ans.append(i + 's')
        else:
            ans.append(i)
            
    return set(ans)
print("Ans 5 : Pluralize : ", pluralize(ip))

    