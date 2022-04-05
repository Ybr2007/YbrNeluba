'''
1.0.3
Time:2022.4.5
1.测试Image
'''

import YbrMatrixSo
import pygame

YbrMatrixSo.Init()
window = YbrMatrixSo.CreateWindow((800,600),"Test",resizable=True)

'''image = YbrMatrixSo.Image(YbrMatrixSo.Vector2(0,0),YbrMatrixSo.Vector2(800,600),"LogoV5.png",True)
YbrMatrixSo.Save(image,"Data",'image')'''

image = YbrMatrixSo.Load("Data","image")

def Start():
    pass

def Update():
    pass

def Draw():
    window.fill((255,255,255))
    image.Draw(window)
    pass

def EventManage(event):
    if event.type == pygame.QUIT:
        YbrMatrixSo.Exit()

if __name__ == "__main__":
    YbrMatrixSo.Framework(Start,Update,Draw,EventManage,60)