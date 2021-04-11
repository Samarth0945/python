a=str(input('Enter your string'))
vow=0
cons=0
wspace=0
digit=0
for i in range(0,len(a)):
    if(a[i] in ('a','e','i','o','u')):
        vow+=1
    elif(a[i]==' '):
        wspace+=1
    elif(a[i].isdigit()):
        digit+=1
    else:
        cons+=1
print(vow,cons,digit,wspace)            