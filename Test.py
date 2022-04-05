'''
1.0.5
Time:2022.4.5
1.测试Text
'''

import YbrMatrixSo
import pygame

YbrMatrixSo.Init()
window = YbrMatrixSo.CreateWindow((800,600),"Test",resizable=True)

obj = YbrMatrixSo.Text(YbrMatrixSo.Vector2(100,50),48,"Hello World")
YbrMatrixSo.Save(obj,"Test","obj")

obj = YbrMatrixSo.Load("Test","obj")

def Start():
    pass

def Update():
    pass

def Draw():
    window.fill((255,255,255))
    obj.Draw(window)
    pass

def EventManage(event):
    if event.type == pygame.QUIT:
        YbrMatrixSo.Exit()

if __name__ == "__main__":
    YbrMatrixSo.Framework(Start,Update,Draw,EventManage,60)