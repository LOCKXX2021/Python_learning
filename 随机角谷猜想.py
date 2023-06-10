import random
x = random.randint(1,9999999999999999999999999999)
c = x
counts = 0
while str(x) != '1':
    if x %2 == 0:
        print("x/2",x//2,sep="=" )
        x = x //2
    elif x %2 == 1:
        print("3*x+1",3*x+1,sep='=')
        x = x * 3 + 1
    counts = counts + 1
print('结果是',x)
print('次数是',counts)
print('生成的随机数' ,c,sep="是")
print('次数与随机数的比值',c/counts,sep="是")
