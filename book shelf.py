n,k=map(int,raw_input().strip().split(','))
a=[]
k=k+1
for i  in range(n):
	a.append(input())
maxCoins={}
for i in range(k):
	maxCoins[i]=a[i]
for index in range(k,n):
	maxCoins[index] = max(maxCoins[index-k]+a[index], maxCoins[index-k+1])
print maxCoins