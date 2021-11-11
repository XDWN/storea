z=1
n=9

for z in range(n,1,-1):
    j=1
    for j in range(j,z+1):
        print(j,'*',z,'=',z*j,end=(' '))
    print('')