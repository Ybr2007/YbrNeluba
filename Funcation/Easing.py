import math
from enum import Enum
import threading
from Framework.GlobalVariable import isGameOver
import time

def QuadEaseIn(b,e,t,dt):
    t = t/dt
    return (e - b) * t * t + b

def QuadEaseOut(b,e,t,dt):
    t = t/dt
    return -(e - b) * t * (t - 2) + b

def BackEaseIn(b,e,t,dt):
    t = t/dt
    s = 1.70158
    return (e - b) * t * t * ((s + 1) * t - s) + b

class EaseFuncation(Enum):
    '''
    平滑函数类型
    '''
    Linear = lambda b,e,t,dt:b + (e - b) * t / dt

    SineEaseIn = lambda b,e,t,dt:b -(e - b) * math.cos(t/dt * (math.pi/2)) + (e - b)
    SineEaseOut = lambda b,e,t,dt:b + (e - b) * math.sin(t/dt * (math.pi/2))
    SineEaseInOut = lambda b,e,t,dt:b - (e - b) / 2 * (math.cos(math.pi * t/dt) - 1)

    QuadEaseIn = QuadEaseIn
    QuadEaseOut = QuadEaseOut

    BackEaseIn = BackEaseIn

def __EasingThread(func,b,e,duration,funcation,callback,dt = 10,*args):
    '''
    缓动线程
    '''
    global isGameOver
    timer = 0
    func(b,*args)
    while timer < duration:
        if isGameOver:
            return
        timer += dt
        func(funcation(b,e,timer,duration),*args)
        time.sleep(dt/1000)
    func(e,*args)
    for func in callback:
        func()

def Easing(func,b,e,duration,funcation = EaseFuncation.Linear,callback = [],dt = 10,*args):
    '''
    缓动
    '''
    threading.Thread(target = __EasingThread,args = 
    (func,b,e,duration,funcation,callback,dt,*args)).start()
