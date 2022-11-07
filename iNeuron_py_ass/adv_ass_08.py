#%% Q1)
def isvowel(char):
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        return True
    return False

def vowel_links(s):
    arr = s.split()
    n = len(arr)
    for i in range(1,n):
        if isvowel(arr[i-1][-1]) and isvowel(arr[i][0]):
            return True
    return False

print(vowel_links("a very large appliance"))
print(vowel_links("go to edabit"))
print(vowel_links("an open fire"))
print(vowel_links("a sudden applause"))
# %% Q2)
def first_before_second(string, a, b):
    q = [i for i in range(len(string)) if string[i]==b]
    p = [i for i in range(len(string)) if string[i]==a]

    if p[-1] < q[0]:
        return True
    
    return False

print(first_before_second("a rabbit jumps joyfully", "a", "j"))
print(first_before_second("knaves knew about waterfalls", "k", "w"))
print(first_before_second("happy birthday", "a", "y"))
print(first_before_second("precarious kangaroos", "k", "a"))
            
    

# %% Q3)
def parse_even(obj):
    ans = [obj[i] for i in range(1,len(obj), 2) ]
    if type(obj) == list:
        return ans
    else:
        return "".join(ans)

def parse_odd(obj):
    ans = [obj[i] for i in range(0,len(obj), 2) ]
    if type(obj) == list:
        return ans
    else:
        return "".join(ans)

def char_at_pos(obj, method):
    if method == 'even':
        return parse_even(obj)
    elif method == 'odd':
        return parse_odd(obj)
    
    

print(char_at_pos([2, 4, 6, 8, 10], "even"))
print(char_at_pos("EDABIT", "odd"))
print(char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd"))

# %% Q4)

def gcd_2(a,b):
    while(b):
        a, b = b, a%b
    return a
def GCD(lst):
    x = lst[0]
    y = lst[1]
    gcd = gcd_2(x,y)
    for i in range(2, len(lst)):
        gcd = gcd_2(gcd, lst[i])
    return gcd

print(GCD([10, 20, 40]))
print(GCD([1, 2, 3, 100]))
print(GCD([1024, 192, 2048, 512]))

# %% Q5)
def convert_to_binary(num):
    x = num
    bin = ""
    while x > 0:
        bin += str(x%2)
        x = x//2
    
    return bin ## type string

def reverse_str(string):
    x = str(string)
    return "".join([x[i] for i in range(len(x)-1, -1, -1)])

def isPalindrome(obj):
    if str(obj) == reverse_str(obj):
        return True
    else:
        return False

def numbin(num):
    return f"\n#Decimal {num}\n#Binary {convert_to_binary(num)}\n\n"

def palindrome_type(num):
    if isPalindrome(num) == True and isPalindrome(convert_to_binary(num)) == True:
        return "Decimal and Binary" + numbin(num)
    elif isPalindrome(num) == False and isPalindrome(convert_to_binary(num)) == True:
        return "Binary only"+ numbin(num)
    elif isPalindrome(num) == True and isPalindrome(convert_to_binary(num)) == False:
        return "Decimal only"+ numbin(num)
    else:
        return "Neither"+ numbin(num)

print(palindrome_type(1306031))
print(palindrome_type(427787))
print(palindrome_type(313))
print(palindrome_type(934))




# %%
# %%
