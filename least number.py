s=list(raw_input())
s.sort()
for i in range(input()):
	del s[len(s)-1]
print ''.join(s)