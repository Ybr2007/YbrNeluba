'''
1.0.5
Time:2022.4.5
1.测试Text
'''

import YbrMatrixSo
import pygame

YbrMatrixSo.Init()
window = YbrMatrixSo.CreateWindow((800,600),"Test",resizable=True)

obj = YbrMatrixSo.Audio('./test.mp3',0.8)
YbrMatrixSo.Save(obj,"Test","obj")

obj = YbrMatrixSo.Load("Test","obj")

timer = YbrMatrixSo.Timer(1000,1)
YbrMatrixSo.Save(timer,"Test","timer")

timer = YbrMatrixSo.Load("Test","timer")

def Start():
    obj.Play()
    timer.Play()
    pass

def Update():
    pass

def Draw():
    window.fill((255,255,255))
    pass

def EventManage(event):
    if event.type == pygame.QUIT:
        YbrMatrixSo.Exit()
    if event.type == timer.timerEvent:
        obj.Pause()

if __name__ == "__main__":
    YbrMatrixSo.Framework(Start,Update,Draw,EventManage,60)