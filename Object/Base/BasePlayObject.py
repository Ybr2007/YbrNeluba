# 导入模块
from Object.Base.BaseObject import BaseObject
import abc

class BasePlayObject(BaseObject,metaclass = abc.ABCMeta):
    '''
    所有可播放Object的基类
    '''
    @abc.abstractmethod
    def Play(self):
        '''
        播放
        '''
        raise NotImplementedError("Play()没有实现")

    @abc.abstractmethod
    def Stop(self):
        '''
        停止
        '''
        raise NotImplementedError("Stop()没有实现")

    @abc.abstractmethod
    def Pause(self):
        '''
        暂停
        '''
        raise NotImplementedError("Pause()没有实现")