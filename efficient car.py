m=0.0
for tc in range(int(input())):
    x,y=list(map(float,raw_input().strip().split()))
    if m<y/x:
        m=y/x
print m