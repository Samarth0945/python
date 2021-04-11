a=str(input('Enter ur string\n'))
b=a.split()
c=[]
for i in b:
    if(i not in c):
        c.append(i)
print(c)        
