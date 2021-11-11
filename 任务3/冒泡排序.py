a=[5,2,4,7,9,1,3,5,4,0,6,1,3]

for i in range((len(a))):
    for s in range((len(a)-1)):
        if a[s]>a[s+1]:
            a.insert(s,a.pop(s+1))
print(a)