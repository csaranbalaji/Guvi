n=input()
a=[1]
l=map(int,raw_input().strip().split())
a+=l
a.append(1)
c=[]+l
i1=a.index(max(l))
del l[i1]
i2=a.index(max(l))
del l[i2]
if i1>i2:
	i1,i2=i2,i1
while(i1+1!=i2):
	o.append(min(a[i1:i2]]))
	
