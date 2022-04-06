'''
1.1.3
Time:2022.4.6
1.为ViewObject的SetSize添加等比缩放重载
'''

from Debug.DebugLog import Debug,DebugType
import YbrMatrixSo
import pygame

YbrMatrixSo.Init()
window = YbrMatrixSo.CreateWindow((800,600),"Test",resizable=True)

obj = YbrMatrixSo.Text(
    YbrMatrixSo.Vector2(0,0),text='Text',
)


def Start():
    pass

def Update():
    x,y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        obj.SetSize((YbrMatrixSo.Vector2(x,y) - obj.position).length)
    if pygame.mouse.get_pressed()[2]:
        obj.SetSize(YbrMatrixSo.Vector2(x,y) - obj.position)
    pass

def Draw():
    window.fill((0,0,0))
    obj.Draw(window)
    pass

def EventManage(event):
    if event.type == pygame.QUIT:
        YbrMatrixSo.Exit()

if __name__ == "__main__":
    YbrMatrixSo.Framework(Start,Update,Draw,EventManage,60)