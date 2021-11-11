a=int(input('请输入边长'))
b=int(input('请输入边长'))
c=int(input('请输入边长'))
if a+b<=c or b+c<=a or a+c<=b:
    print('这几个边长组成不了三角形哦!')
else:
    print('可以构成三角形呦')
    if a==b and b==c and c==a:
        print('组成的三角形是等边三角形呢')
    elif a==b or b==c or c==b:
        print('组成的三角形是等腰三角形呢')
    elif a*a+b*b==c*c or c*c+b*b==a*a or a*a+c*c==b*b:
        print('组成的三角形是直角三角形呢')
    else:
        print('组成的三角形是普通三角形呢')


