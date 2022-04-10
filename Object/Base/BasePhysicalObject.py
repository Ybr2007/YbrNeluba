# 导入模块
from Object.Base.BaseObject import BaseObject
from Math.Math import *
from Debug.Debug import *
import abc

class BasePhysicalObject(BaseObject,metaclass = abc.ABCMeta):
    '''
    所有实体selfect的基类
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
        self.size = size
        self.size.x = max(0,self.size.x)
        self.size.y = max(0,self.size.y)
        self.size.Update()

    @abc.abstractmethod
    def SetScale(self,scale : float):
        '''
        设置缩放
        参数:
            scale:缩放
        '''
        d = self.size.length / scale
        self.SetSize(self.size / d)

    def SetPosWithProportion(self,position1 : Vector2,position2 : Vector2,proportion : float or Vector2):
        w,h = self.size.tuple
        if isinstance(proportion,Vector2):
            _x,_y = proportion.tuple
            x = position1.x + (position2.x - position1.x) * _x
            y = position1.y + (position2.y - position1.y) * _y
        else:
            x = position1.x + (position2.x - position1.x) * proportion
            y = position1.y + (position2.y - position1.y) * proportion

        self.SetPosition(Vector2(x - w/2,y - h/2))

    def EasingSetPosWithProportion(self,position1 : Vector2,position2 : Vector2,proportion : float or Vector2):
        w,h = self.size.tuple
        if isinstance(proportion,Vector2):
            _x,_y = proportion.tuple
            x = position1.x + (position2.x - position1.x) * _x
            y = position1.y + (position2.y - position1.y) * _y

        else:
            x = position1.x + (position2.x - position1.x) * proportion
            y = position1.y + (position2.y - position1.y) * proportion

        self.SetPosition(self.position + (Vector2(x - self.position.x - w/2,y - self.position.y - h/2) * 0.1))

    def SetCenterPos(self,position : Vector2):
        w,h = self.size.tuple
        self.SetPosition(position - Vector2(w/2,h/2))

    def EasingSetCenterPos(self,position : Vector2):
        w,h = self.size.tuple
        self.SetPosition(self.position + (position - Vector2(w/2,h/2) - self.position) * 0.1)