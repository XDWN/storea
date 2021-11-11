dict = {"k1":"v1","k2":"v2","k3":"v3"}
'''
1.取值
dict['k1']
2.增加/修改  
# 如果key不存在添加键值对
dict["age"]=18
# 如果key存在修改已存在的键值对
dict["k1"]="vb"
3.删除
dict.pop("k2")

dict.update()合并字典
dict.chear()清空字典
'''
len(dict)
def dic(a):
    for k in a:#k变量每次循环中的key
        #print(k)
        print(dict[k])
        print("%s,%s"% (k,dict[k]))
dic(dict)