import os
import pickle
counts = 1
flag = 0
def desktop_path():
    return os.path.join(os.path.expanduser('~'),"Desktop")
os.chdir(desktop_path())
with open('lst.pk','rb') as f:
    lst = pickle.load(f)
temp_str = input('请输入要查询的字符')
suffix_Str = input('''请输入接龙做的事情，如1.xxx 已做 
                       则输入已做                  ''')
name_lst = temp_str.split('\n')
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