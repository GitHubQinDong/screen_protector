# -*- coding: utf-8 -*- # 
import pythoncom
import pyHook
from time import sleep
from temp import ScreenSaver
from multiprocessing import Process,Pipe

starttime=0
def onActiveEvent(event,sub_p=None):
    sub_p.send(1)
    sub_p.close()
    # 监听键盘事件
    # print("MessageName:", event.MessageName)
    # print("Message:", event.Message)
    # print("Time:", event.Time)
    # print("Window:", event.Window)
    # print("WindowName:", event.WindowName)
    # print("Ascii:", event.Ascii, chr(event.Ascii))
    # print("Key:", event.Key)
    # print("KeyID:", event.KeyID)
    # print("ScanCode:", event.ScanCode)
    # print("Extended:", event.Extended)
    # print("Injected:", event.Injected)
    # print("Alt", event.Alt)
    # print("Transition", event.Transition)
    # print("---")
    # 同鼠标事件监听函数的返回值
    # p = Process(target=
    return True

def main(sub_p):

    global starttime
    # 创建一个“钩子”管理对象
    hm = pyHook.HookManager()
    # 监听所有键盘事件
    onActiveEvent=lambda sub_p=sub_p:onActiveEvent(sub_p=sub_p)
    hm.KeyDown=hm.MouseAll=onActiveEvent
    # 设置键盘“钩子”
    hm.HookKeyboard()
    # 监听所有鼠标事件
    # hm.MouseAll = onMouseEvent
    # 设置鼠标“钩子”
    hm.HookMouse()
    # 进入循环，如不手动关闭，程序将一直处于监听状态
    pythoncom.PumpMessages(10000)
    


if __name__ == "__main__":
    sup_p,sub_p=Pipe()
    p=Process(target=main,args=(sub_p,))
    p.start()
    while 1:
        if sup_p.recv():
            starttime=0  
        sleep(1)
        starttime+=1
        print(starttime)
        if starttime>20:
            ScreenSaver(10)
    