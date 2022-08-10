s = "harshal"
for i in s:
        if i.islower():
            s.replace(i, i.upper())
        else:
            s.replace(i, i.lower())
            
k = s.replace('a', 'a'.upper())
print(k)

r = 'A'.lower()
print(r)