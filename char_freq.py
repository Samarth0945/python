a=str(input('Enter your string\n'))
count={}
for char in a:
    if char in count:
        count[char]+=1
    else:
        count[char]=1
print(a,count)        