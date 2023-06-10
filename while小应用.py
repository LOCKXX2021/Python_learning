temp = input("请输入你的分数或输入e停止")
while (temp is not 'e' ):
    scores = int(temp)
    if scores <60:
     print("D")
    elif 60<=scores <80:
     print("C")
    elif 80<=scores <90:
     print("B")
    elif 90<=scores <100:
     print("A")
    else:
     print("S")
    temp = input("请输入你的分数或输入e停止")
print("programmer has been stopped")
