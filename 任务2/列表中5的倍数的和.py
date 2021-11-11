#有以下一个列表，求其中是5的倍数的和
c=0
sum=0
a = [1,5,21,30,15,9,30,24]
for c in range(0,len(a)):
    if a[c]%5==0:
        sum=sum+a[c]
print(sum)
a.insert(-1, 'a')
print(a)

#有下列列表，请编程实现列表的数据翻转
List = [1,2,3,4,5,6,7,8,9]
frequency=len(List) #frequency频率,此次
x=0
i=-1
inversion=-1
if frequency/2!=0:
   z=(frequency-1)/2
else:z=frequency/2

while x<z:
    one=List.pop(x)#取出列表前面的元素
    two=List.pop(i)#取出列表后面的元素
    List.insert(x,two)#把后面的元素two插入前面
    if x==0:#如果是第一次循环
        List.append(one)#在最后插入前面的元素one
    else:#如果不是第一次循环
        List.insert(inversion,one)#把前面的元素one插入后面inversion的位置
        inversion -= 1
    i-=1
    x+=1
print(List)

#有下列列表，请编程实现列表的数据翻转 方法二

List_a = [1,2,3,4,5,6,7,8,9]
for n in reversed(List_a):
    print(n)
    Lins_c
print(List_a)