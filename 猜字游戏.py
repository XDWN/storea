import random


money = 1000
count = 0  # 计数

z = 0
name = 'root'
password = 'admin'
while z < 3:
    name_r = input('请输入用户名')
    password_r = input('请输入密码')
    if name == name_r and password == password_r:
        print('登陆成功')
        break
    elif name != name_r:
        print('用户名或密码错误')
    elif password != password_r:
        print('用户名或密码错误')
    z += 1
if z == 3:
    print('功能已锁定')

b = input('是否开始')
i = 0
while money > 0:
    a = random.randint(1, 10)

    if b == 'q' or b == 'Q':
        break
    c = int(input('请输入您预测的数字'))
    count += 1
    money = money - 100
    if c == a:
        print('恭喜中奖,您的余额还剩', money)
        break
    elif c < a:
        print('您输入的数字偏小哦!您的余额还剩', money)

    elif c > a:
        print('您输入的数字偏大哦!您的余额还剩', money)
        print(money)
    print(count)
    if money == 0:
        cc = input('金额已用完,是否充值')
        if cc == 'y' or cc == 'Y':
            money = money + int(input('请输入充值金额'))


