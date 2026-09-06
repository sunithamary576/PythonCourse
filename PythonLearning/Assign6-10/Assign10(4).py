s="Banana"
vowels="a","e","i","o","u"
count=0

for i in s.lower():
    for j in vowels:
        if i==j:
            count+=1
print(count)
