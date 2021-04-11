a=input('Enter ur string')
b=a.split()
c=[]
for i in b:
    if i not in c:
         c.append(i)
    else:
        print(c)     
