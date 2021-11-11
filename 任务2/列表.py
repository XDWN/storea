#在列表后面添加列表
province=["北京","上海","广东",]#proyince:省,领域
province.append("新疆")#在最后添加一个内容
province.extend(["河北","山东","湖南","内蒙古"])#一次性添加多个内容
province.insert(2,province.pop(1))
print(province)
'''
#循环方法
Shing=["北京","上海","广东",]
while True:
    Shing.append(input('请添加省份'))
    print(Shing)
'''
#GDP和与平均数
GDP=[36710.36,36710.36,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
a=0
sum_GDP=0
svg=0
while a<8:
    sum_GDP=sum_GDP+GDP[a]
    a+=1
print('GDP总和为',sum_GDP)
svg=sum_GDP/a
print('平均GDP为',svg)
print(36710.36+36710.36)
