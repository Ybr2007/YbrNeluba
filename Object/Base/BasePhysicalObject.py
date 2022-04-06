# 导入模块
from Object.Base.BaseObject import BaseObject
from Math.Math import *
from Debug.Debug import *
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

    @abc.abstractmethod
    def SetPosition(self,position : Vector2):
        '''
        设置位置
        参数:
            position:位置
        '''
        self.position = position

    @abc.abstractmethod
    def SetSize(self,size : Vector2):#TODO:当size中的x或y为负数时，会出现问题，应进行特殊处理
        '''
        设置大小
        参数:
            size:大小
        '''
        if size.x <= 0 or size.y <= 0:
            Debug.Log("size的x或y值不能小于等于0",type=DebugType.Error)
            return
        self.size = size
