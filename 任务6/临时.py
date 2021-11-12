user={'1':
          {'id':'12345678','name':'admin','password':'admin','site':{
              '国家':'中国','省份':"北京",'街道':'昌平区沙河'
          },'blancee':'100',"op_bank":'中国工商银行的昌平支行'},

      }
import random
for a in user:
    c = 0
a = int(a) + 1
user[a] = {'id': '', 'name': '', 'password': '', 'site': {
    '国家': '', '省份': "", '街道': ''
}, 'blancee': '', "op_bank": ''},

# 账号
ide = random.randint(10000000, 100000000)
restart = True
while restart:
    restart = False
    for k in user:
        if user[k]["id"] != ide:
            break
        else:
            ide = random.randint(10000000, 100000000)
            restart = True
