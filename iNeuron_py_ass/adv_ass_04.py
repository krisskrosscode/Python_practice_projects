#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 19:51:12 2022

@author: harshal
"""

#%% Q1)
cache = {}
def fib_fast(n):
    if n in cache:
        return cache[n]
    
    if n == 0 or n == 1:
        return n
    else:
        res = fib_fast(n-1) + fib_fast(n-2)
        cache[n] = res
        # print(type(cache))
        print(cache)
        return res
    
print(fib_fast(3))