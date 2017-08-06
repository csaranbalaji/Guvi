n=int(input())
a=[]
for i in range(n):
    a.append(input().strip())
i,j,flag=0,0,1
while(True):
    if i==n-1 and j==n-1:
        break
    if i<n-1:
        if a[i+1][j]=='.':
            i+=1
            continue
    if a[i][j+1]=='.':
        j+=1
    else:
        flag=0
        break
if flag:
    print("YES")
else:
    print("NO")
    