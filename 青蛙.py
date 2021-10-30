forg=0
day=1
while 1:
    forg=forg+3


    if forg >= 20:
        print('脱险成功')
        break
    else:
        forg=forg-2
    day+=1
print(day)