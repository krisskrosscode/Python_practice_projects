#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 22:57:47 2022

@author: harshal
"""

#%% Q1)
lst1 = [
      ['#', '!'], 
      ['!!', 'X']
      ]

lst2 = [['!!!', 'O', '!' ], ['X', '#', '!!!'], ['!!', 'X', 'O']] 

def check_score(lst):
    sum = 0
    for i in lst:
        for j in i:
            if j == "#":
                sum += 5
            elif j == 'O':
                sum += 3 
            elif j == "X":
                sum += 1 
            elif j == '!':
                sum -= 1
            elif j == "!!":
                sum -= 3
            elif  j == "!!!":
                sum -= 5
    if sum < 0:
        return 0
    return sum
print(check_score(lst1))
print(check_score(lst2))


#%% Q2)
def combinations(*args):
    prod = 1
    for i in args:
        prod = prod * i
    return prod

print(combinations(2,3,4,5))


#%% Q3)

def encode_morse(string):
    char_to_dots = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
    ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
    '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }
    ans =""
    for i in string:
        
        ans = ans + char_to_dots[i]
    return ans

print(encode_morse("EDABBIT CHALLENGE"))
#%% Q4)
import math
def isPrime(num):
    for i in range(2, int(math.sqrt(num))):
        if num%i == 0:
            return False
    return True

print(isPrime(56963))


#%% Q5)
def to_boolean_list(string):
    ans = []
    for i in string.lower():
        if (ord(i) - 96)%2 == 0:
            ans.append(False)
        else:
            ans.append(True)
    return ans
print(to_boolean_list('deep'))
    

    
    






