goods = [{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "显示器", "price": 120},
{"name": "内存", "price": 230}, ]
goods.insert(0,'')
for i in range(len(goods)):
    if i !=0:
        print(i,goods[i]["name"],goods[i]["price"])
while True:
    c=input('请选择您所需要的商品序号')
    if c!='q' or c!='Q':
        c=int(c)
        if c>(len(goods)-1):
            print('请输入正确的商品序号')
        else:
            c=int(c)
            for k in range(len(goods)):
                if k !=0:
                    if k==c:
                        print(k, goods[k]["name"], goods[k]["price"])
    else:
        print('欢迎下次光临')
        break