
def sum(a):
    s=0
    for i in a:
        if type(i)==int:
            s=s+i
    return s

list1=['罗恩', 23 ,35 ,44]
list2=['哈利 ',60, 77 ,68 ,88, 90]
list3=['赫敏', 97 ,99 ,89 ,91, 95, 90]
list4=['马尔福' ,100, 85 ,90]
print(list1[0],sum(list1))
print(list2[0],sum(list2))
print(list3[0],sum(list3))
print(list4[0],sum(list4))
