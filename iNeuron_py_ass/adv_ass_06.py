# %% Q1)
from itertools import count

from macpath import join


def find_the_difference(s, t):
    sum_s, sum_t = 0, 0
    if len(s)==0: return t
    for i in s:
        sum_s += ord(i)
    for i in t:
        sum_t += ord(i)

    return chr(sum_t - sum_s)

print(find_the_difference('abcd', 'abcde'))
print(find_the_difference('', 'y'))
print(find_the_difference('ae', 'aea'))
# %% Q2)

#[int, str, bool, list, tuple, dictionary]

def count_datatypes(*args):
    dt = {
        int:0,
        str:0,
        bool:0,
        list:0,
        tuple:0,
        dict:0
    }
    for i in list(args):
        dt[type(i)] += 1
    return list(dt.values())

print(count_datatypes(1,45,'HI', False))
print(count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1))
print(count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1,
3], {"Brayan": 18}, 25, 23))
print(count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]))
# %% Q3)
def fib_str(n, chars):
    ans = [chars[0], chars[1]]
    for i in range(2,n):
        ans.append(ans[i-1] + ans[i-2])
    print(', '.join(ans))

fib_str(3, ["j", "h"]) 
fib_str(5, ["e", "a"]) 
fib_str(6, ["n", "k"])  
# %%Q4)
def ones_threes_nines(num):
    ans = {
        'nines':0,
        'threes':0,
        'ones':0
    }
    n = num
    while n>0:
        if n>=9:
            ans['nines'] += 1
            n = n- 9
        elif n>=3:
            ans['threes'] += 1
            n = n - 3
        else:
            ans['ones'] += 1
            n = n - 1
    print(ans)

ones_threes_nines(10)
ones_threes_nines(15)
ones_threes_nines(22)


# %% Q5)
def fib(n):
    if n==0: return 0
    a, b = 0, 1
    for i in range(2,n):
        c = a + b
        a = b
        b = c
    
    return a+b

print(fib(5))
print(fib(2))
print(fib(7))
print(fib(8))
print(fib(9))

# %%
