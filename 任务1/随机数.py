import random

a = random.randint(1, 10)
money = 1000
b = input('是否开始')
i = 0

# while 1:
#     if b=='q' or b=='Q':
#         break
#
#     else:
while money > 0:
    if b == 'q' or b == 'Q':
        break
    c = int(input('请输入您预测的数字'))
    money = money - 100
    if c == a:
        print('恭喜中奖,您的余额还剩', money)
        break
    elif c < a:
        print('您输入的数字偏小哦!您的余额还剩', money)

    elif c > a:
        print('您输入的数字偏大哦!您的余额还剩', money)
