'''
1.1.4
Time:2022.4.7
1.添加缓动功能
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
    YbrMatrixSo.Easing(
        obj.SetPosition,YbrMatrixSo.Vector2(0,0),YbrMatrixSo.Vector2(400,400),
        2000,YbrMatrixSo.EaseFuncation.BackEaseIn
    )
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