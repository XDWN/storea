import xlrd
def chan(a):
    for i in a:
        return  i
        break
def zon(a):
    rea = sorted(a.items(), key=lambda x: -x[1])  # 全年销售量最高的衣服
    for i in rea:
        return i
        break


f = xlrd.open_workbook(filename=r"E:\测试开发\python\day08【excel表读写】\2020年每个月的销售情况.xlsx", encoding_override=True)
# 获取多少行 sheet.nrows
# 获取多少列 sheet.ncols
sum_s=0#全年销售总额
every=0
piece=0
piec=0
list={}
list_e={}#每种衣服的销售量
list_m={}#每件衣服的价格
tex_1={}
tex_2={}
tex_3={}
tex_4={}
for x in range(12):
    sheet = f.sheet_by_index(x)
    rows = sheet.nrows  # 获取多少行

    for i in range(1, rows):
        data = sheet.row_values(i)
        if data[1] in list:
            list[data[1]]=list[data[1]]+data[2]*data[4]
        else:
            list[data[1]]=data[2]*data[4]
    for o in range(1,rows):#销售数量
        data_1 = sheet.row_values(o)
        if data_1[1] in list_e:
            list_e[data_1[1]] = list_e[data_1[1]] + data_1[4]
        else:
            list_e[data_1[1]] =data_1[4]
    for i in range(1, rows):#销售价格
        data = sheet.row_values(i)
        if data[1] in list_m:
            pass
        else:
            list_m[data[1]]=data[2]

    if x ==1 or x ==2 or x ==3:
        for w in range(1, rows):  # 销售数量
            dat = sheet.row_values(w)
            if dat[1] in tex_1:
                tex_1[dat[1]] = tex_1[dat[1]] + dat[4]
            else:
                tex_1[dat[1]] = dat[4]
    if x ==4 or x ==5 or x ==6:
        for r in range(1, rows):  # 销售数量
            dat_1 = sheet.row_values(r)
            if dat_1[1] in tex_2:
                tex_2[dat_1[1]] = tex_2[dat_1[1]] + dat_1[4]
            else:
                tex_2[dat_1[1]] = dat_1[4]
    elif x == 7 or x == 8 or x == 9:
        for t in range(1, rows):  # 销售数量
            dat_2 = sheet.row_values(t)
            if dat_2[1] in tex_3:
                tex_3[dat_2[1]] = tex_3[dat_2[1]] + dat_2[4]
            else:
                tex_3[dat_2[1]] = dat_2[4]
    elif x == 10 or x == 11 or x == 0:
        for y in range(1, rows):  # 销售数量
            dat_3 = sheet.row_values(y)
            if dat_3[1] in tex_4:
                tex_4[dat_3[1]] = tex_4[dat_3[1]] + dat_3[4]
            else:
                tex_4[dat_3[1]] = dat_3[4]


for p in list_e:#总的销售量
    piece=list_e[p]+piece
for l in list_e:#每种衣服销售量的占比
    piec=list_e[l]/piece*100
    print(piec,'%')
#print(list_e)

res=sorted(list_e.items(),key=lambda x:x[1])#全年销售量最低的衣服

rea=sorted(list_e.items(),key=lambda x:-x[1])#全年销售量最高的衣服
print('全年最低:',chan(res))
print('全年最高:',chan(rea))
#全年销售总额
for k in list:
    sum_s=sum_s+list[k]
print(sum_s)
for i in list:
    print(i,'的销售额占比为:',list[i]/sum_s*100,'%')
print('第一季度最畅销衣服是:',zon(tex_1),'第二季度最畅销衣服是:',zon(tex_2),'第三季度最畅销衣服是:',zon(tex_3),'第四季度最畅销衣服是:',zon(tex_4))




