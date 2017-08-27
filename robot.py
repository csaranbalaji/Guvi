def smax(numbers):
    count = 0
    m1 = m2 = 0
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1            
            else:
                m2 = x
    return m2 if count >= 2 else None
n=input()
a=map(int,raw_input().strip().split())
x=max(a)
y=smax(a)
s=x-y
print s,x,y