import YbrNebula as Nebula
import pygame

Nebula.Init() # 初始化
window = Nebula.CreateWindow(
    (800, 600),"Ybr Nebula",
    resizable=True
) # 创建窗口

#--------------------------------------------------------------
#在此处定义组件
obj = Nebula.EnInputBox(
    position=Nebula.Vector2(100,100),
    size=Nebula.Vector2(200,50),
    text=Nebula.Text(
        position=Nebula.Vector2(0,0),
    ),
    normalColor=Nebula.Color.LightGray.value,
    focusColor=Nebula.Color.PrussianBlue.value,
    callback=[
        print
    ]
)

#--------------------------------------------------------------

def Start(): # 在程序启动时调用
    pass

def Update(): # 每一帧调用
    pass

def Draw(): # 每一帧绘制
    window.fill(Nebula.Color.Black.value)
    obj.Draw(window)
    pass

def EventManager(event : pygame.event.Event): # 事件处理
    if event.type == pygame.QUIT:
        Nebula.Exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            Nebula.Exit()

    obj.Update(event)

if __name__ == "__main__":
    Nebula.Framework(Start,Update,Draw,EventManager,fps=120) # 启动框架