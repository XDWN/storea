i=0
name='root'
password='admin'
while i<3:
    name_r=input('请输入用户名')
    password_r=input('请输入密码')
    if name==name_r and password==password_r:
        print('登陆成功')
        break
    elif name!= name_r:
        print('用户名或密码错误')
    elif password!=password_r:
        print('用户名或密码错误')
    i+=1
if i==3:
    print('功能已锁定')