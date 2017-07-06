s1,s2=raw_input().strip(),raw_input().strip()
s3=0
for i in range(len(s1)):
    if s1[i:] == s2[:len(s1)-i]:
        s3=len(s1[i:])
        break
print len(s1+s2)-s3