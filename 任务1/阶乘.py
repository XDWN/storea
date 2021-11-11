num = 1
sum=0
factorial=21
c=0
for a in range(1,factorial):
    sum=sum+num
    c += 1
    print(a,'a')
    for b in [a+1]:
        num=num*b
        print(b)
print(sum)

