import easygui
import sys
while 1:
    easygui.msgbox("欢迎来到我的第一个游戏")
    msg = '你想学啥'
    title1 = '小游戏互动'
    list1 = ["谈恋爱",'Python','琴棋书画','打游戏']
    choice = easygui.choicebox(msg,title1,list1)
    if choice:
     easygui.msgbox('你的选择是{}'.format(choice))
    else:
     easygui.msgbox('那好吧您再想想')