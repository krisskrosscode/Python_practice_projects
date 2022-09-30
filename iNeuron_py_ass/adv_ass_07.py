#%% Q1)
from sympy import is_primitive_root, isprime


def count_layers(s):
    layers = 0
    if len(s)%2==0:
        n = len(s)//2 - 1
    else:
        n = len(s)//2
    
    if len(s[n])%2==0:
        nn = len(s[n])//2 - 1
    else:
        nn = len(s[n])//2

    for i in range(1, nn+1):
        if s[n][i] != s[n][i-1]:
            layers += 1
    
    return layers+1

print(count_layers([
"AAAA",
"ABBA",
"AAAA"
]))

print(count_layers([
"AAAAAAAAA",
"ABBBBBBBA",
"ABBAAABBA",
"ABBBBBBBA",
"AAAAAAAAA"
]))


print(count_layers([
"AAAAAAAAAAA",
"AABBBBBBBAA",
"AABCCCCCBAA",
"AABCAAACBAA",
"AABCADACBAA",
"AABCAAACBAA",
"AABCCCCCBAA",
"AABBBBBBBAA",
"AAAAAAAAAAA"
]))
# %% Q2)

def unique_styles(arr):
    arr = ','.join(arr).split(',')
    return len(set(arr))

print(unique_styles([
"Dub,Dancehall",
"Industrial,Heavy Metal",
"Techno,Dubstep",
"Synth-pop,Euro-Disco",
"Industrial,Techno,Minimal"
]))

print(unique_styles([

"Soul",
"House,Folk",
"Trance,Downtempo,Big Beat,House",
"Deep House",
"Soul"
]))
# %% Q3)
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
71, 73, 79, 83, 89, 97]

def binary_search(primes, start, end, target):
    while start<=end:
        mid =(start + end) // 2
        if primes[mid] == target:
            return mid
        elif primes[mid] < target:
            start = mid + 1
        else:
            end = mid -1
        
    return -1

def is_prime(primes, target):
    start = 0
    end = len(primes) - 1

    loc = binary_search(primes, start, end, target)

    return "yes" if loc != -1 else 'no'

print(is_prime(primes, 3))
print(is_prime(primes, 4))
print(is_prime(primes, 67))
print(is_prime(primes, 36))


# %% Q4)
def power_ranger(n, a, b):
    i  = 1
    count = 0

    while i**n <= b:
        if i**n >=a:
            count+=1
        i+=1
    return count
print(power_ranger(2, 49, 65))
print(power_ranger(3, 1, 27))
print(power_ranger(10,1 ,5))
print(power_ranger(5, 31, 33))
print(power_ranger(4, 250, 1300))
# %%Q5)
def rearranged_difference(num):
    n = num
    l = []
    while n>0:
        l.append(n%10)
        n = n//10
    
    largest = [str(i) for i in sorted(l)[::-1]]
    smallest = [str(i) for i in sorted(l)]

    lno = int(''.join(largest))
    sno = int(''.join(smallest))

    return lno - sno

print(rearranged_difference(972882))
print(rearranged_difference(3320707))
print(rearranged_difference(90010))
# %%
