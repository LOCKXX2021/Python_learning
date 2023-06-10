#名单的绝对路径，其中'\\'可以用'/'代替
infile='D:\\名单.txt'


f=open(infile,'r', encoding="utf-8")
#将名单的txt形式另存为编码为UTF-8
sourceInLine=f.readlines()
dataset=[]
for line in sourceInLine:
    temp=line.strip('\n')
    dataset.append(temp)
    
# 接龙信息，粘贴在三重引号'''   '''之间
stopword = "d"
print("请输入内容【单独输入'd'保存退出】：")
namelist = input("namelist")
#修改结束语 使得输入回车不会导致输入结束
for line in iter(input,stopword):
 namelist = namelist+line+"\n"

# 查找、打印没接龙的童鞋
for name in dataset:
    name = ''.join(name)
    where = namelist.find(name) 
    if where == -1:
        print(name)
