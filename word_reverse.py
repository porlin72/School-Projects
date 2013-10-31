def reverse(s):
    r = []
    ns = ""
    count = len(s)-1
    while count != -1:
        r.append(s[count])
        count -= 1
    for i in range(len(s)):
        ns += r[i]
    return ns
    
print reverse("apple")