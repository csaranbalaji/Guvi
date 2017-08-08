def dig(n):
    if len(n)==1:
        return n
    return  dig(str(sum(map(int,n))))
print(dig(input().strip()))