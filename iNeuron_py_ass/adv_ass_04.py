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

#%% Q2)
def convert_to_hex(string):
    ans = []
    for i in string:
        ans.append(hex(ord(i)))
    return " ".join(ans)

print(convert_to_hex("hello world"))



# %% Q3)
def uncensor(censored_string, vowels):
    ans = ""
    j = 0
    for i in range(len(censored_string)):
        if censored_string[i] == '*':
            ans = ans + vowels[j]
            j = j+1

        else:
            ans = ans + censored_string[i]

    return ans

print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
print(uncensor("abcd", ""))
print(uncensor("*PP*RC*S*", "UEAE"))


# %% Q4)
def get_domain_name(ipaddr):
    import socket
    ans = socket.gethostbyaddr(ipaddr)
    return ans[0]

print(get_domain_name("8.8.8.8"))
print(get_domain_name("8.8.4.4"))

# %% Q5)
def factorial(num):
    ans = 1
    for i in range(num, 0, -1):
        ans  = ans * i
    return ans

def fact_of_fact(num):
    tmp = 1
    for i in range(num,0,-1):
        tmp = tmp * factorial(i)
    return tmp
# print(factorial(4))
print(fact_of_fact(10))
# %%
