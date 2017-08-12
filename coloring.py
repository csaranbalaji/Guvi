n=input()
s=raw_input().strip()
c=1
a=s[0]*n
for i in range(1,len(s)):
    if a==s:
	break
    else:
	if not(len(a)>i and a[i]==s[i]):
	    a=a[:i]+s[i]*n
	    c+=1
print c
