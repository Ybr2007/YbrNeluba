from Debug.DebugLog import Debug,DebugType
from Object.Base.BaseViewObject import BaseViewObject
from Object.Base.BaseSaveAbleObject import BaseSaveAbleObject
from Math.Math import *
import pygame

class Image(BaseViewObject,BaseSaveAbleObject):
    '''
    图片类
    '''
    def __init__(self,position : Vector2,size : Vector2,imagePath : str,includeAlpha : bool = False):
        '''
        初始化
        参数:
            position:位置
            size:大小(若为None则根据图片大小自动设置)
            imagePath:图片路径
        '''
        super().__init__(position,size)

        self.imagePath = imagePath
        self.includeAlpha = includeAlpha

        if includeAlpha:
            self.surface = pygame.image.load(imagePath).convert_alpha()
        else:
            self.surface = pygame.image.load(imagePath)

        self.__oriSurface = self.surface

        if size is None:
            self.size = Vector2(self.surface.get_width(),self.surface.get_height())
        else:
            self.size = size
            self.surface = pygame.transform.smoothscale(self.surface,self.size.tuple)

    def SetPosition(self, position: Vector2):
        return super().SetPosition(position)

    def SetSize(self, size: Vector2 or float):
        if isinstance(size,Vector2):#如果size是Vector2类型,则表示图片尺寸
            super().SetSize(size)
            self.surface = pygame.transform.smoothscale(self.__oriSurface,self.size.tuple)
        elif isinstance(size,float):#如果size是float类型,则表示图片的缩放比例
            d = self.size.length / size
            super().SetSize(self.size / d)
            self.surface = pygame.transform.smoothscale(self.__oriSurface,self.size.tuple)

    def Draw(self, surface: pygame.Surface):
        return super().Draw(surface)

    def GetData(self):
        return {
            'type':self.__class__,
            'data':{
                'position':self.position,
                'size':self.size,
                'imagePath':self.imagePath,
                'includeAlpha':self.includeAlpha
            }
        }

    def Load(data):
        return Image(data['position'],data['size'],data['imagePath'],data['includeAlpha'])