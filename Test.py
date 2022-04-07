'''
1.1.5
Time:2022.4.7
1.将SetSize的int重载改为SetScale
'''

from Debug.DebugLog import Debug,DebugType
from Math.Vector import Vector2
import YbrMatrixSo
import pygame

YbrMatrixSo.Init()
window = YbrMatrixSo.CreateWindow((800,600),"Test",resizable=True)

obj1 = YbrMatrixSo.Image(
    YbrMatrixSo.Vector2(0,0),YbrMatrixSo.Vector2(150,100),"Asset\YbrMatrixSoLogo.png"
)
obj2 = YbrMatrixSo.Rect(
    YbrMatrixSo.Vector2(0,0),YbrMatrixSo.Vector2(100,100),
    width=8
)
obj = YbrMatrixSo.BaseSet(YbrMatrixSo.Vector2(0,0),YbrMatrixSo.Vector2(100,100),[obj1,obj2])

def Start():
    YbrMatrixSo.Easing(
        obj.SetPosition,YbrMatrixSo.Vector2(0,0),YbrMatrixSo.Vector2(400,400),
        2000,YbrMatrixSo.EaseFuncation.BackEaseIn
    )
    YbrMatrixSo.Easing(
        obj.SetSize,Vector2(100,100),Vector2(300,300),
        1000,YbrMatrixSo.EaseFuncation.BackEaseIn
    )
    pass

def Update():
    x,y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        obj.SetScale((Vector2(x,y) - obj.position).length)
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