from Object.Base.BasePlayObject import BasePlayObject
from Object.Base.BaseSaveAbleObject import BaseSaveAbleObject
import pygame
from Debug.DebugLog import *

class Timer(BasePlayObject,BaseSaveAbleObject):
    def __init__(self,time,id = 1):
        '''
        初始化
        参数:
            time:间隔激活时间(ms)
        '''
        TIMER = pygame.USEREVENT + id
        pygame.time.set_timer(TIMER,time)

        self.timerEvent = TIMER
        self.time = time

        self.hasStopped = False
        self.isPaused = False

    def Play(self):
        '''
        播放计时器
        '''
        if self.hasStopped:
            Debug.Log("计时器已停止",type=DebugType.Warning)
            return
        TIMER = pygame.USEREVENT + 1
        pygame.time.set_timer(TIMER,self.time)
        self.timerEvent = TIMER
        self.isPaused = False

    def Stop(self):
        '''
        停止计时器
        '''
        TIMER = pygame.USEREVENT + 1
        pygame.time.set_timer(TIMER,0)
        self.timerEvent = TIMER
        self.hasStopped = True

    def Pause(self):
        '''
        暂停计时器
        '''
        TIMER = pygame.USEREVENT + 1
        pygame.time.set_timer(TIMER,0)
        self.timerEvent = TIMER
        self.isPaused = True

    def GetData(self):
        return self

    def Load(data):
        return data