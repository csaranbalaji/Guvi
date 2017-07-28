n=input()
a=[]
for i in range(n):
    a.append(raw_input().strip()+' ')
s=raw_input().strip()
sp=s[0]+s[1:].replace('',' ')
for i in range(n):
    a[i]=a[i].replace('+ '*len(s),sp)
x=0
for i in range(n):
    if a[i].find('+')!=-1:
        a[i]=a[i].replace('+',s[x])
        x+=1
for i in a:
    print i