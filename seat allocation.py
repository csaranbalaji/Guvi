import itertools as it
def subset(arr,num):
	a=[]
	for i in range(2,num):
		for j in it.combinations(arr,i):
			a.append(tuple(sorted(j)))
	return set(a)
s=input()
n=input()
c=1
for i in subset(range(1,n+1)*(s-1),s):
	if sum(i)==s:
		c+=1
print c
