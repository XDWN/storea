city = {
    "北京": {
        "昌平": {"八达岭": ["八达岭长城"],
               "回龙观": ["永旺超市", "永辉超市", "呷哺呷哺"]
               },
        "海淀": {"高校": ["清华", "北大"],
               "公园": ["香山", "植物园"],
               "博物馆": ["军事博物馆", "国家地质博物馆"]
               },
        "朝阳": {"景观": ["玉渊潭公园", "朝阳公园"]},
    },
    "上海": {},
    "西藏": {}
}
goods = [{"name": "电脑", "price": 1999},
         {"name": "鼠标", "price": 10},
         {"name": "显示器", "price": 120},
         {"name": "内存", "price": 230}, ]
goods.insert(0, '')


def dic(a):
    for k in a:  # k变量每次循环中的key
        print(k)


print('--------------------------------------欢迎使用啥都没有旅游系统--------------------------------------')
while True:

    print("本系统有一下城市共宁选择")
    dic(city)
    site = input("您要去那个城市")
    if site == 'q' or site == 'Q':
        break
    else:
        dic(city[site])
        site1 = input("您要去那个地区")
        if site1 == 'q' or site1 == 'Q':
            break
        else:
            dic(city[site][site1])
            site2 = input("您要去那个地点")
            if site2 == 'q' or site2 == 'Q':
                break
            else:
                dic(city[site][site1][site2])
                site3 = input("您要去哪个地方")
                if site3 == 'q' or site3 == 'Q':
                    break
                else:
                    print("您要去哪个地方")
