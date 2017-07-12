n=input()
a=[]
for i in range(n):
    a.append(map(int,raw_input().strip().split()))
d=[input()]
for test in range(n):
    for i in range(len(a)):
        if a[i][0] in d or a[i][1] in d:
            d+=a[i]
            del a[i]
            break
print len(set(d))