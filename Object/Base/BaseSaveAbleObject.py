# 导入模块
from Object.Base.BaseObject import BaseObject
import abc

class BaseSaveAbleObject(BaseException,metaclass = abc.ABCMeta):
    '''
    所有可保存Object的基类
    '''
    @abc.abstractmethod
    def GetData(self):
        '''
        获取数据
        '''
        raise NotImplementedError("GetData()没有实现")
        pass

    @staticmethod
    @abc.abstractmethod
    def Load(data):
        '''
        加载数据
        '''
        raise NotImplementedError("Load()没有实现")