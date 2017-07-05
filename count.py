r=[]
a=map(int,raw_input().strip().split())
for i in a:
	if a.count(i)>1:
		r.append(i)
print len(set(r))