sum =0
number_one=0
number_tow=0
s=0
z=0
while s<10:
    s += 1
    number_one=int(input('请输入数字'))
    sum=sum+number_one
    if number_one>z:
        z=number_one


print('这十个数的总和为',sum)
print('这10个数的平均数为',sum/s)
print('最大值为',z)