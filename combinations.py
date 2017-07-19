from itertools import permutations
for i in permutations(raw_input(),input()):
	o=''
	for j in i:
		o+=j
	print o
