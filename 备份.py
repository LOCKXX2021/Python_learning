import os
import time
lst = []
name_lst =  []
counts = 1
_counts = 0
count = 0
flag = 0
def desktop_path():
    return os.path.join(os.path.expanduser('~'),"Desktop")
os.chdir(desktop_path())
with open('名单.txt','r') as f:
    for i in f:
        lst.append(i)
    for i in lst:
        lst[_counts] = lst[_counts].replace('\n','')
        _counts += 1
f = open('查询名单.txt','r')
for i in f:
    name_lst.append(i)
for i in name_lst:
    name_lst[count] = name_lst[count].replace('\n', '')
    count += 1
    if i == '':
        name_lst.remove(i)
suffix_Str = input('''请输入接龙做的事情，如1.xxx 已做 则输入已做''')
templist = list(suffix_Str)
for i in name_lst:
    name_lst[counts-1] = name_lst[counts-1].replace('{}. '.format(counts),'')
    name_lst[counts-1] = name_lst[counts-1].replace(' ','')
    for x in range(len(templist)):
        name_lst[counts-1] = name_lst[counts-1].replace(templist[x], '')
    counts += 1
for i in lst:
    if i not in name_lst:
        print('缺少{}'.format(i))
        flag = 1
if flag == 0:
    print('人齐了')
f.close()
time.sleep(1000)