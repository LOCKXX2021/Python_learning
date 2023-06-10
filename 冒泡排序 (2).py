temp = input('input stop to kill program')
while temp != 'stop' or 'Stop':
    list = input('Please input your list and seperate them by comma')
    list = list.split(",")
    counts = 0
    for i in range(0,len(list)-1):
        if list[i] > list[i+1]:
            list[i],list[i+1] = list[i+1],list[i]
            counts += 1
        else:
            continue
    while counts != 0:
        counts = 0
        for i in range(0, len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                counts += 1
            else:
                continue
    print(list)
 
