a=map(int,raw_input().strip().split())
k=input()
print a[len(a)-k:]+a[:len(a)-k]