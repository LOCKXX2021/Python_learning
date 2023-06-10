import easygui
import sys
while 1:
    easygui.msgbox("欢迎来到我的第一个游戏")
    msg = '你想学啥'
    title1 = '小游戏互动'
    list1 = ["谈恋爱'",'Python','琴棋书画','打游戏']
    choice = easygui.choicebox(msg=msg,title = title1,choices=list1)
