'''
1.0.4
Time:2022.4.5
1.测试Shape
'''

import YbrMatrixSo
import pygame

YbrMatrixSo.Init()
window = YbrMatrixSo.CreateWindow((800,600),"Test",resizable=True)

rect = YbrMatrixSo.Rect(YbrMatrixSo.Vector2(100,100),YbrMatrixSo.Vector2(100,100),r = 10)
YbrMatrixSo.Save(rect,'Test','rect')


#rect = YbrMatrixSo.Load('Test','rect')

def Start():
    pass

def Update():
    pass

def Draw():
    window.fill((255,255,255))
    rect.Draw(window)
    pass

def EventManage(event):
    if event.type == pygame.QUIT:
        YbrMatrixSo.Exit()

if __name__ == "__main__":
    YbrMatrixSo.Framework(Start,Update,Draw,EventManage,60)