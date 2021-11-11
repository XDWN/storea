names = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
]
'''
sum=0
#平均薪资
for i in range(len(names)):
    sum=sum+names[i][5]
svg=0
svg=sum/(i+1)
print(svg)
'''
#统计每个人的平均年龄
'''
age=0
e=0
for g in range(len(names)):
    e=e+int(names[g][6])
age=e/(g+1)
print(age)
#公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
names.extend(['刘备','45','男','220','alibaba',500,'30'])
print(names)
'''
#统计公司男女人数
'''
a,t,cou=0,0,0
for j in names:
    c = names[a][2]
    print(c)
    if c=='男':
        cou+=1
        print(cou)
    a += 1
sun_r=int(len(names))
print('公司有%s名男性,%s名女性'%(cou,sun_r-cou))
'''
