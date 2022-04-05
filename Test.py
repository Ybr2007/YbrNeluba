'''
1.0.8
Time:2022.4.6
1.测试BaseSet
'''

import YbrMatrixSo
import pygame

YbrMatrixSo.Init()
window = YbrMatrixSo.CreateWindow((800,600),"Test",resizable=True)

obj = YbrMatrixSo.BaseSet(YbrMatrixSo.Vector2(20,20),YbrMatrixSo.Vector2(200,200),
[
    YbrMatrixSo.Rect(YbrMatrixSo.Vector2(0,0),YbrMatrixSo.Vector2(100,100),width=1),
    YbrMatrixSo.Rect(YbrMatrixSo.Vector2(20,20),YbrMatrixSo.Vector2(50,50),width=1,color = YbrMatrixSo.Color.Red.value),
])

obj = YbrMatrixSo.Rect(YbrMatrixSo.Vector2(20,20),YbrMatrixSo.Vector2(200,200),width=1)

def Start():
    pass

def Update():
    x,y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        obj.SetPosition(YbrMatrixSo.Vector2(x,y))
    if pygame.mouse.get_pressed()[2]:
        obj.SetSize(YbrMatrixSo.Vector2(x,y) - obj.position)
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