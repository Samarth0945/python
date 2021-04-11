a=input('Enter ur string')
b=a.split()
for i in b:
    c=i.endswith('s')
    if(c==1):
        print(i)        