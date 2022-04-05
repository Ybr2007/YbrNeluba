from Object.Base.BasePlayObject import BasePlayObject
from Object.Base.BaseSaveAbleObject import BaseSaveAbleObject
from Object.Base.BaseUpdateObject import BaseUpdateObject
import Framework.GlobalVariable as GlobalVariable
import pygame

class TimeLine(BasePlayObject,BaseSaveAbleObject,BaseUpdateObject):
    def __init__(self,timeEventPairList = [],timeCallBackPairList = []):
        timeEventPairList.sort(key = lambda x:x[0])
        
        self.index1 = 0
        self.index2 = 0

        self.timeEventPairList = timeEventPairList
        self.timeCallBackPairList = timeCallBackPairList

        self.deviationTime = 0
        self.isPause = False
        self.pauseTime = 0

        self.time = 0

    def Update(self,event=None):
        if self.isPause:
            return

        self.time = GlobalVariable.runTime - self.deviationTime
        
        if self.index1 < len(self.timeEventPairList):
            if self.time >= self.timeEventPairList[self.index1][0]:
                pygame.event.post(pygame.event.Event(self.timeEventPairList[self.index1][1]))
                self.index1 += 1
        if self.index2 < len(self.timeCallBackPairList):
            if self.time >= self.timeCallBackPairList[self.index2][0]:
                self.timeCallBackPairList[self.index2][1]()
                self.index2 += 1

    def Play(self):
        if self.isPause:
            self.deviationTime = GlobalVariable.runTime - self.pauseTime
        self.isPause = False

    def Pause(self):
        self.isPause = True
        self.pauseTime = GlobalVariable.runTime

    def Stop(self):
        self.timeCallBackPairList = []
        self.timeEventPairList = []
        self.index1 = 0
        self.index2 = 0
        self.deviationTime = 0
        self.isPause = True

    def GetData(self):
        return self

    def Load(data):
        return data
    