Library = {"1": {"account": 1,
                 "password": 123456,
                 "country": 1,
                 "province": 1,
                 "street": 1,
                 "door": 1,
                 "money": 100,
                 "bank_name": 1},
           "2": {"account": 2,
                 "password": 123456,
                 "country": 1,
                 "province": 1,
                 "street": 1,
                 "door": 1,
                 "money": 100,
                 "bank_name": 1}, }


def start():
    import random
    id = str(random.randint(10000000, 99999999))
    if id in Library:
        id = random.randint(10000000, 99999999)
    else:
        Library[id] = {}
        Library[id]["name"] = input('姓名')
        Library[id]["password"] = input('密码')
        Library[id]["country"] = input('国家')
        Library[id]["province"] = input('省市')
        Library[id]["door"] = input('街道')
        Library[id]["money"] = input('存款金额')
        Library[id]["bank_name"] = '中国工商银行的昌平支行'

    for k in Library[id]:
        print(Library[id][k])
    print('开户成功')

#存钱
def register():
    account = input('请输入账号')
    password = int(input('请输入密码'))
    if account in Library:
        if Library[account]['password'] == password:
            money_0 = int(input('请输入存款金额'))
            money_1=Library[account]["money"]
            Library[account]["money"]=money_0+money_1
            print( Library[account]["money"])
        else:
            print("密码错误,登录失败")
    else:
        return False
#取钱
def withdrawal():
    account = input('请输入账号')
    password = int(input('请输入密码'))
    if account in Library:
        if Library[account]['password'] == password:
          money_2=Library[account]["money"]
          money_3=input('请输入取款金额')
          if money_2<money_3:
              print("您的资金不足,无法取款")
              #return 3
          else:
              Library[account]["money"]=money_2-money_3
        else:
            print("密码错误,登录失败")
    else:
        return False
#转账
def turn():
    account = input('请输入账号')
    password = int(input('请输入密码'))
    if account in Library:
        if Library[account]['password'] == password:
          money_2=Library[account]["money"]
          account_1=input('请输入转入账号')
          if account_1 in Library:
              money_1=input('请输转入款金额')
              if money_2<money_1:
                  print("您的资金不足,无法转账")
                  # return 3
              else:
                  money_3=Library[account_1]["money"]
                  Library[account_1]["money"]=money_3+money_1
                  Library[account]["money"]=money_2-money_1
        else:
            print("密码错误,登录失败")
    else:
        return False
#查询
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
print("************************************************")
print("*            中国工商银行账户管理系统v1.0*         *")
print("************************************************")
print("                                               ")
print("*1.开户                                         *")
print("*2.存钱                                         *")
print("*3.取钱                                         *")
print("*4.转账                                         *")
print("*5.查询                                         *")
print("*6.bye                                         *")
print("************************************************")

num = input('请输入您要办理的业务')
while True:
    if num == '1':
        start()
    elif num == '2':
        register()
    elif num=='3':
        withdrawal()
    elif num=='4':
        turn()
    elif num=='5':
        cx()
    else:
        break