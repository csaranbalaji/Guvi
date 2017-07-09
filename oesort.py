n=input()
o,e=[],[]
a=map(int,raw_input().strip().split())
for i in a:
	if i%2:
		o.append(i)
	else:
		e.append(i)
o.sort()
e.sort()
for i in a:
	if i%2:
		print o[0]
		del o[0]
	else:
		print e[0]
		del e[0]