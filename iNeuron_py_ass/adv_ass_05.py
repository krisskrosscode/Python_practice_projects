#%% Q1)
from tkinter import TRUE


even_odd = [8,2]
n = int(input("Enter number : "))
print(even_odd[n & 1])

# %% Q2)
def majority(lst):

    ans_dict = {k:0 for k in list(set(lst))}
    

    for i in lst:
        ans_dict[i] += 1
        

    for k,v in ans_dict.items():
        if v > len(lst)/2:
            return k
        
    return None

print(majority(["B", "B", "B", "B", "C", "A"]))
print(majority(["A", "B", "B", "A", "C", "C"]))


# %% Q3)
def censor_word(word, symbol):
    return symbol*len(word)

def censor_string(line, lst, symbol):
    for i in range(len(lst)):
        lst[i] = lst[i].lower()

    line_list = line.split()
    for i in range(len(line_list)):
        if line_list[i].lower() in lst:
            line_list[i] = censor_word(line_list[i], symbol)
    return " ".join(line_list)

print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))
print(censor_string("The cow jumped over the moon.", ["cow", "over"], "*"))
print(censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "?"))

# %% Q4)

def isPolydiv(num) :
    s = str(num)
    l = len(s)

    if s[0] == '0':
        ans = False
    else:
        ans = True

    for i in range(1,l):
        if int(s[:i])%i == 0:
            ans = ans and True
        else:
            ans = ans and False
            break
    return ans
print(isPolydiv(123220))

# %% Q5)

def isPrime(num):
    if num == 0 or num == 1:
        return False
    import math
    for i in range(2, int(math.sqrt(num)) + 1):
        if num%i == 0:
            return False
    return True

def sum_primes(lst):

    if len(lst) == 0:
        return None
    sum = 0
    for i in lst:
        if isPrime(i):
            sum  += i
 
    return sum

print(sum_primes([]))
# %%
