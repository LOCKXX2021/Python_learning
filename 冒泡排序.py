list = input('please input your list and separate those numbers by comma')
list = list.split(",")
counts = 1
while 1:
    for i in range(0,len(list)-1):
        if list[i] > list[i+1]:
            counts += 1
            list[i],list[i+1] = list[i+1],list[i]
        else:
            continue
    if counts > 0 :
        counts = 0
        continue
    else:
        break
print(list)