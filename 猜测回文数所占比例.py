import random
counts = 0
while counts >=0:
    var = random.randint
    counts += 1
    while var != 'stop':
        flag = 0
        length = len(var)
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
    if flag == 0:
        print(var,'回文数')
        print(var/counts)

