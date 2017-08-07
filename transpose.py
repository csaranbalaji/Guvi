from __future__ import print_function
r,c=map(int,raw_input().strip().split())
a=[]
for row in range(r):
    a.append(map(int,raw_input().strip().split()))
for row in zip(*a):
    print(*row)