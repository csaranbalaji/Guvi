for tc in range(input()):
	n=[]
	for i in range(input()):
		n.append(raw_input())
	n.sort()
	p,m='',0
	for i in n:
		if len(set(i.strip()))>m:
			m=len(set(i.strip()))
			p=i
	print "Case #"+str(tc+1)+": "+p