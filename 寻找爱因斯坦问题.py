x = 7
number = int(input("请输入你想要的满足条件的数的数量"))
counts = number
while bool(x%2 == 1) is False or bool(x%3 == 2) is False or bool(x%5 == 4) is False or counts>0:
    x = x +7
    if bool(x%2 == 1) is True and bool(x%3 == 2) is True and bool(x%5 == 4) is True :
        print(x)
        counts = counts - 1
        if counts == number-1:
            b = x
        if counts < number - 1:
            a = x
            c = a - b
            print('差值是'+str(c))
            b = a
