from Math.Vector import Vector2,zeroVector2
import YbrNebula as Nebula
import pygame

Nebula.Init() # 初始化
window = Nebula.CreateWindow(
    (800, 600),"Ybr Nebula",pygame.image.load("Asset\YbrMatrixSoLogo.png"),
    resizable=True
) # 创建窗口

#################################################################
#在此处定义组件

#################################################################

def Start(): # 在程序启动时调用
    pass

def Update(): # 每一帧调用
    pass

def Draw(): # 每一帧绘制
    window.fill(Nebula.Color.Black.value)
    pass

def EventManager(event : pygame.event.Event): # 事件处理
    if event.type == pygame.QUIT:
        Nebula.Exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            Nebula.Exit()

if __name__ == "__main__":
    Nebula.Framework(Start,Update,Draw,EventManager,fps=120) # 启动框架