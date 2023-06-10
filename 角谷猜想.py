temp = input("请输入任意整数")
flag = 0
def fl():
    for i in temp:
        if '0'<= i <= '9':
            continue
        else:
            global flag
            flag = 1
fl()
while flag != 0:
    temp = input('请输入整数,不要乱输入')
    flag = 0
    fl()
x = int(temp)
counts = 0
while x != 1:
    if x %2 == 0:
        x = x //2
    elif x %2 == 1:
        x = x * 3 + 1
    counts = counts + 1
print('结果是',x)
print('次数是',counts)
