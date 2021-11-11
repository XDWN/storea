Friuts = {
	'苹果':12.3,  # 水果和单价
	'草莓':4.5,
    '香蕉':6.3,
    '葡萄':5.8,
    '橘子':6.4,
    '樱桃':15.8
}

info = {
    '小明': {
        'fruits': {'苹果':4, '草莓':13, '香蕉':10},
        'money': 'sum'
    },
    '小刚': {
        'fruits': {'葡萄':19, '橘子':12, '樱桃':30},
        'money': 'sum'
    }
}

print(info['小明']['fruits']['苹果'])
s=0
for k in info['小明']['fruits']:
    c=(info['小明']['fruits'][k])
    s=s+c
info['小明']['money']=s
print(info['小明']['money'])