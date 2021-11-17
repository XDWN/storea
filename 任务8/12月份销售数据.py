import xlrd

f = xlrd.open_workbook(filename=r"E:\测试开发\python\day08【excel表读写】\12月份衣服销售数据.xlsx", encoding_override=True)
sheet = f.sheet_by_index(0)
rows = sheet.nrows  # 获取多少行
cols = sheet.ncols  # 获取多少列

text = {}#数量
sum_piece = 0  # 总销售量
sum_s = 0  # 总销售量
ever_piece = 0  # 销售总额
piec = 0  # 每件销售量
for i in range(1, rows):
    data = sheet.row_values(i)
    if data[1] in text:
        text[data[1]] = data[4] + text[data[1]]
    else:
        text[data[1]] = data[4]
    # sum_s=sum_s+data[]
print(text)
for k in text:
    # print(k, '月平均销售量为', text[k] / 30)
    sum_s = text[k] + sum_s
List = {}#价格

for c in range(1, rows):
    data_1 = sheet.row_values(c)
    if data_1[1] in List:
        pass
    else:
        List[data_1[1]] = data_1[2]
print(List)
sum_m=0
for x in text:
    for j in List:
        if x==j:
            print(x,'的月销售额为',text[x]*List[j])
            sum_m=text[x]*List[j]+sum_m#总销售额
print(sum_m)
for f in text:
    for d in List:
        if f==d:
            print(x,'的月销售额为',text[f]*List[d]/sum_m,'%')

