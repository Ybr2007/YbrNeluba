'''
1.0.7
Time:2022.4.6
1.测试TimeLine
'''

import YbrMatrixSo
import pygame

YbrMatrixSo.Init()
window = YbrMatrixSo.CreateWindow((800,600),"Test",resizable=True)

EVENT = pygame.USEREVENT + 1

obj = YbrMatrixSo.TimeLine(
    [(4,EVENT)],[(1,YbrMatrixSo.CallBack(YbrMatrixSo.Debug.Log,"1s"))]
)

YbrMatrixSo.Save(obj,"Test","obj")

obj = YbrMatrixSo.Load("Test","obj")
assert isinstance(obj,YbrMatrixSo.TimeLine)

def Start():
    obj.Play()
    pass

def Update():
    obj.Update()
    pass

def Draw():
    window.fill((255,255,255))
    pass

def EventManage(event):
    if event.type == pygame.QUIT:
        YbrMatrixSo.Exit()
    if event.type == EVENT:
        YbrMatrixSo.Debug.Log("4s")
        YbrMatrixSo.Debug.Record()

if __name__ == "__main__":
    YbrMatrixSo.Framework(Start,Update,Draw,EventManage,60)