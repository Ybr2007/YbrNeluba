'''
1.0.2
Time:2022.4.5
1.测试Framework
'''

import YbrMatrixSo
import pygame

YbrMatrixSo.Init()
window = YbrMatrixSo.CreateWindow((800,600),"Test",resizable=True)

def Start():
    pass

def Update():
    pass

def Draw():
    window.fill((255,255,255))
    pass

def EventManage(event):
    if event.type == pygame.QUIT:
        YbrMatrixSo.Exit()

if __name__ == "__main__":
    YbrMatrixSo.Framework(Start,Update,Draw,EventManage,60)