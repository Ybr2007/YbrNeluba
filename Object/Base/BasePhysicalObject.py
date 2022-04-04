# 导入模块
from Object.Base.BaseObject import BaseObject
from Math.Math import *
import abc

class BasePhysicalObject(BaseObject,metaclass = abc.ABCMeta):
    '''
    所有实体Object的基类
    '''
    position : Vector2 = None

    size : Vector2 = None

    @abc.abstractmethod
    def __init__(self,position : Vector2,size : Vector2):
        '''
        初始化
        参数:
            position:位置
            size:大小
        '''
        self.position = position
        self.size = size
