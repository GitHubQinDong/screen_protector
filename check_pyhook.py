# -*- coding: utf-8 -*- # 
import pythoncom
import pyHook
from time import sleep
from temp import ScreenSaver
from threading import Thread

def onActiveEvent(event,sub_p=None):
    global starttime
    starttime=0
    return True

def show_win(rest_time=5):
    global starttime
    while 1:
        sleep(1)
        starttime+=1
        print(starttime)
        if starttime>=rest_time:
            ScreenSaver(rest_time)

starttime = 0

def main():
    t=Thread(target=show_win,args=(10,),name='show_win_thread')
    t.start()
    hm = pyHook.HookManager() # 创建一个“钩子”管理对象
    help(hm)
    hm.KeyDown=onActiveEvent  # 监听所有键盘事件
    hm.HookKeyboard() # 设置键盘“钩子”
    # hm.MouseAll=onActiveEvent # 监听所有鼠标事件
    # hm.HookMouse()  # 设置鼠标“钩子”
    pythoncom.PumpMessages() # 进入循环，如不手动关闭，程序将一直处于监听状态
    
if __name__ == "__main__":
    main()
    