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
            
    

# %%
