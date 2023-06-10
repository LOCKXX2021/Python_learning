import os
from easygui import  enterbox
from easygui import msgbox
def desktop_path():
    return os.path.join(os.path.expanduser('~'),"Desktop")
os.chdir(desktop_path())
lst = []
temp = []
counts = 1
with open('名单.txt',mode = 'w',encoding='utf-8') as f:
    a = enterbox(title='请输入要提取名单的接龙')
    suffix_Str = input('''请输入接龙做的事情，如1.xxx 已做 则输入已做''')
    templist = list(suffix_Str)
    lst = a.split('\n')
    for i in lst:
        lst[counts-1] = lst[counts-1].replace('{}. '.format(counts),'')
        lst[counts-1] = lst[counts-1].replace(' ','')
        for x in range(len(templist)):
            lst[counts - 1] = lst[counts - 1].replace(templist[x], '')
        counts += 1
    for i in lst:
        f.writelines(i+'\n')
msgbox('名单已生成')