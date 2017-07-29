import itertools as it
def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0: return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False    

    return True
n=input()
a=[]
p=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
for i in p:
	if i<=n:
		a.append(str(i))
c=0
g=[]
for i in it.permutations(a,2):
	g.append(int(i[0]+i[1]))
for i in set(g):
	if isPrime(i):
		c+=1
print c
