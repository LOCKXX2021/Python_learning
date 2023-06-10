var = input('请输入一个数字或输入stop终止')
length = len(var)
while var != 'stop':
    flag = 0
    if(length > 1) and (length %2  == 0):
        for i in range(1,int(1+(length/2))):
            if var[i-1] != var[-i]:
                flag = 1
                break
    elif (length > 1) and (length != 0):
        for i in range(1,int(1+(length-1)/2)):
             if var[i-1] != var[-i]:
                flag = 1
                break
  
    if len(var) == 1:
        print('请输入两位以上数字')
    elif flag == 0:
        print(var,'回文数')
    else:
        print(var,'非回文数')
    var = input('请输入一个数字或输入stop终止')
print('程序已终止')
