from Object.Base.BasePlayObject import BasePlayObject
from Object.Base.BaseSaveAbleObject import BaseSaveAbleObject
import pygame
from Framework.GlobalVariable import isAudioPause

def Pause():
    '''
    暂停音频
    '''
    pygame.mixer.pause()
    global isAudioPause
    isAudioPause = True
    
def UnPause():
    '''
    继续音频
    '''
    pygame.mixer.unpause()
    global isAudioPause
    isAudioPause = False

class Audio(BasePlayObject,BaseSaveAbleObject):
    '''
    音频类
    '''
    def __init__(self,filePath,volume = 1):
        '''
        初始化
        参数:
            filePath:音频路径
            volume:音量
        '''
        self.filePath = filePath
        self.audio = pygame.mixer.Sound(filePath)
        self.volume = volume
        self.audio.set_volume(self.volume)

    def Play(self,loop = 0,maxtime = -1):
        '''
        播放音频
        参数:
            loop:重复次数(-1:无限循环)
            maxtime:播放时间(-1:无限制)
        '''
        self.audio.play(loop,maxtime)

    def Stop(self,fadeOutFime = 0):
        '''
        停止音频
        '''
        if fadeOutFime == 0:
            self.audio.stop()
        else:
            self.audio.fadeout(fadeOutFime)

    def Pause(self):
        '''
        暂停音频
        '''
        Pause()

    def ReSetVolume(self,volume):
        '''
        重新设置音量
        参数:
            volume:音量
        '''
        self.volume = volume
        self.audio.set_volume(self.volume)

    def GetData(self):
        '''
        获取数据
        '''
        return {
            'type':self.__class__,
            'data':{
                'filePath':self.filePath,
                'volume':self.volume,
            }
        }

    def Load(data):
        '''
        加载数据
        '''
        return Audio(data['filePath'],data['volume'])