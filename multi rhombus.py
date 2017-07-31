n = input()

for idx in range(n):
    p=(n-idx-1) * '#'+'/' + (2*idx) * '#'+'\\'+(n-idx-1) * '#'
    s,e=p.rfind('/'),p.find('\\')
    while e-s>4:
    	p=p[:s+1]+'#/'+'#'*(e-s-5)+'\\#'+p[e:]
    	s,e=p.rfind('/'),p.find('\\')
    print p
    
for idx in range(n-1, -1, -1):
    p=(n-idx-1) * '#' +'\\'+ (2*idx) * '#'+'/'+(n-idx-1) * '#'
    s,e=p.rfind('\\'),p.find('/')
    while e-s>4:
    	p=p[:s+1]+'#\\'+'#'*(e-s-5)+'/#'+p[e:]
    	s,e=p.rfind('\\'),p.find('/')
    print p