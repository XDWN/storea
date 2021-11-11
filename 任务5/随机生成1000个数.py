import random
List=[]
for i in range(1000):
    a=random.randint(20,100)
    List.append(a)
from collections import Counter
res=Counter(List)
print(res)
#print(res[20])

#print(sorted(res))提取键值进行排序
print(sorted(res.items()))#字典按键值进行从小到大排序
print(sorted(res.items(),reverse=True))#字典按照键值进行从大到小排序
print(sorted(res.items(),key=lambda x:x[1]))#字典按照value进行从小到大排序
print(sorted(res.items(),key=lambda x:-x[1]))#字典按照value进行从大到小排序
