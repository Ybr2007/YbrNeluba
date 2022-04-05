import pygame
import time
import Framework.GlobalVariable as gv
import os
import tkinter as tk

__win = tk.Tk()

def Framework(StartFuncation,UpdateFuncation,DrawFuncation,EventManageFuncation,fps = -1):
    '''
    Pygame的基本框架
    参数:
        StartFuncation:开始函数
        UpdateFuncation:更新函数
        DrawFuncation:绘制函数
        EventManageFuncation:事件管理函数
        fps:帧率(默认为-1,不限制)
    '''
    StartFuncation()
    while True:
        for event in pygame.event.get():
            EventManageFuncation(event)
        UpdateFuncation()
        DrawFuncation()
        if fps > 0:
            gv.flock.tick(fps)

        gv.__lastT = gv.runTime
        gv.runTime = time.time() - gv.__startT
        gv.delatTime = gv.runTime - gv.__lastT

        pygame.display.update()

def Init():
    '''
    初始化
    '''
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    pygame.display.init()
    
    gv.flock = pygame.time.Clock()
    gv.__startT = time.time()
    
    return True

def CreateWindow(size : tuple = (800,600),title : str = 'YpgWindow',
icon : pygame.Surface = None,fullWindow : bool = False,resizable : bool = False):
    '''
    创建窗口
    参数:
        size:窗口尺寸,默认(800,600)
        title:窗口标题,默认'YpgWindow'
        icon:窗口图标,默认None
    '''
    if fullWindow:
        window = pygame.display.set_mode(GetScreenSize(),pygame.FULLSCREEN)
    elif resizable:
        window = pygame.display.set_mode(size,pygame.RESIZABLE)
    else:
        window = pygame.display.set_mode(size)
    pygame.display.set_caption(title)
    if icon:
        pygame.display.set_icon(icon)
    return window

def Exit():
    '''
    结束程序
    '''
    gv.isGameOver = True
    pygame.quit()
    os._exit(0)

def GetScreenSize():
    '''
    获取屏幕分辨率
    返回:
        屏幕分辨率,元组(宽,高)
    '''
    return (__win.winfo_screenwidth(),__win.winfo_screenheight())
