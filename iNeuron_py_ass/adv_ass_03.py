#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 09:56:44 2022

@author: harshal
"""

#%% Q1)
import re 
pattern = r"(\d+) ([-+*]|[/]{1,2}) (\d+)"
p = re.compile(pattern)

def arithmetic_op(string):
    m = re.match(p, string)
    if m.group(2) == '+':
        return int(m.group(1)) + int(m.group(3))
    elif m.group(2) == '-':
        return int(m.group(1)) - int(m.group(3))
    elif m.group(2) == '*':
        return int(m.group(1)) * int(m.group(3))
    
    elif m.group(2) == '/':
        if m.group(3) == 0:
            return -1
        
        return int(m.group(1)) / int(m.group(3))
    elif m.group(2) == '//':
        if m.group(3) == 0:
            return -1
        return int(m.group(1)) // int(m.group(3))

print('------ Ans 1 -----------')    
print(arithmetic_op('12 // 5'))

#%% Q2)
import math
def dist(p1,p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def perimeter(coordinates):
    peri =  dist(coordinates[0], coordinates[1]) + dist(coordinates[0], coordinates[2]) + dist(coordinates[1], coordinates[2])
    return round(peri,2)

print("------- Ans 2 -------")
print(perimeter([ [15, 7], [5, 22], [11, 1] ]))  
print(perimeter([ [0, 0], [0, 1], [1, 0] ]))
print(perimeter([ [-10, -10], [10, 10 ], [-10, 10] ] ))

#%% Q3)
import numpy as np

buildings = [
  [1, 0, 0, 0],
  [1, 0, 0, 0],
  [1, 1, 1, 0],
  [1, 1, 1, 1]
]


def tallest_skyscraper(buildings):
    
    t = np.zeros([len(buildings), len(buildings)])
    
    for i in range(len(buildings)):
        for j in range(len(buildings[0])):
            t[j][i] = buildings[i][j]
    
    tallest = 0
    for i in range(len(t)):
        if tallest < sum(t[i]):
            tallest = sum(t[i])
    
    return tallest

print(tallest_skyscraper(buildings))

#%% Q4)

def bonus(n):
    b = 0
    
    if n>32:
        if n<=40:
            b = b + (n-32)*325
        else:
            b = b + 8*325
    if n > 40:
        if n <= 48:
            b = b + (n-40)*550
        else:
            b = b + 8*550 
    if n > 48:
        b = b + (n-48)*600
        
    return b
print("------- Ans 4 -----------")
print(bonus(50))

#%% Q5)

def is_disarium(num):
    disarium = 0
    n = num
    power = len(str(n))
    while(n!=0):
        digit = n%10
        disarium = disarium + digit**power
        n = int(n/10)
        power = power - 1
    
    if disarium == num:
        return True
    
    return False

print('------ Ans 5 --------')
print(is_disarium(518))
        

    
    
    
    