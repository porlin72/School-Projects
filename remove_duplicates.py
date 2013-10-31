def remove_duplicates(a):
    b = []
    print len(a)
    if len(a) == 1:
        b.append(a[0])
    else:
        for i in range(len(a)):
            if a[i] not in b:
                print b.append(a[i])
            else:
                pass
    return b
    
print remove_duplicates([1,1,1,1,1,3,3,3,3,5,5,5,5,6,6,6,6])