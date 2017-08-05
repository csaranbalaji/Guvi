s=input().strip().split()
for i in s:
    if i != "of" and i != "and":
        print(i[0].upper(),end='')