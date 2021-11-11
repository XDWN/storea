'''x,length= 0,0
List = [1, 4, 7, 5, 8, 2, 1, 3, 4, 5, 9, 7, 6, 1, 10]
length=len(List)
for i in List:
    cou = 0
    a=0
    for s in range(length):
        c = List[a]
        if c==i:
            cou+=1
        a += 1
    print('数字%s的出现次数为%s' % (i, cou))


for f in range(11) :
    x=List.count(f)
    print(f,'出现的次数为',x)

'''
from collections import Counter

li = [1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]
res = Counter(li)
print(res)