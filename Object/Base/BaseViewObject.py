# 导入模块
from Object.Base.BasePhysicalObject import BasePhysicalObject
import abc
import pygame
class BaseViewObject(BasePhysicalObject,metaclass = abc.ABCMeta):
    '''
    所有可见Object的基类
    '''
    surface : pygame.Surface = None

    @abc.abstractmethod
    def Draw(self,surface : pygame.Surface):
        '''
        绘制
        参数:
            surface:绘制的Surface
        '''
        surface.blit(self.surface,self.position.tuple)