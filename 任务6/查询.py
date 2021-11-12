def cx():
    acc = input("请输入账号")
    pas = int(input("请输入密码"))
    for k in Library:
        acc_1 =k
        if acc == acc_1:
            pas_1 = Library[k]["password"]
            if pas == pas_1:
                print('账号:', Library[k]["name"])
                print('密码:', Library[k]["password"])
                print('余额:', Library[k]["money"])
                print('居住地址:', Library[k]["country"], Library[k]["province"], Library[k]["street"], Library[k]["door"])
                print('开户银行地址:', Library[k]["bank_name"])
            else:
                print("密码错误")
        else:
            print("您查找的账户不存在")
Library = {"1": {"name": 1,
                 "password": 123456,
                 "country": 1,
                 "province": 1,
                 "street": 1,
                 "door": 1,
                 "money": 100,
                 "bank_name": 1},
           "2": {"name": 2,
                 "password": 123456,
                 "country": 1,
                 "province": 1,
                 "street": 1,
                 "door": 1,
                 "money": 100,
                 "bank_name": 1}, }
inquire=int(input("请输入您需要的业务"))
if inquire==6:
    cx()
















