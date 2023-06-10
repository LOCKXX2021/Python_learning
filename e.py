import turtle
turtle.pensize(10)
turtle.setup(1920,1080)
turtle.circle(100)
i = 0
def add_plus(x):
    if x == 1:
        return 1
    else:
        return x*add_plus(x-1)
_sum = 1
num = 16
while 1:
    i += 1
    _sum += 1/add_plus(i)
    temp = str(_sum)
    if len(temp) >=17:
        temp = str(10**num*_sum)
        num +=1
    if int(temp[-1]) %2 == 0:
        turtle.goto(int(temp[-1]),int(temp[-1]))
        turtle.dot(10)
    if int(temp[-1])  %2 != 0:
        turtle.goto(int(temp[-1]), int(temp[-1]))
        turtle.dot(10)
    print(temp)