s=raw_input().strip()
for i in s[:len(s)/2]:
    if i not in s[len(s)/2:]:
        print i
        break