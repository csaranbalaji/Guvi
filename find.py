n=input()
a=map(int,raw_input().strip().split())
x=input()
try:
	print a.index(x),n-a[::-1].index(x)
except ValueError:
	print -1,-1
	