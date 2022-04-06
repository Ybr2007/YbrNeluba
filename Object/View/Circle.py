from Debug.DebugLog import Debug, DebugType
from Object.Base.BaseViewObject import BaseViewObject
from Object.Base.BaseSaveAbleObject import BaseSaveAbleObject
import pygame
from Math.Math import Vector2
from Color.Color import *

class Circle(BaseViewObject,BaseSaveAbleObject):
    '''
    圆形类
    '''
    def __init__(self, position: Vector2,r : int = 0,color : tuple = Color.KleinBlue.value,
                width: int = 0):
        super().__init__(position,Vector2(r*2,r*2))
        
        self.color = color
        self.width = width
        self.r = r

        self.surface = pygame.Surface(self.size.tuple)
        self.surface.set_colorkey(Color.Black.value)
        self.surface = self.surface.convert_alpha()

        pygame.draw.circle(self.surface, self.color, (self.r,self.r), self.r, self.width)

    def SetPosition(self, position: Vector2):
        return super().SetPosition(position)

    def SetSize(self, size: Vector2 or float):
        if isinstance(size,Vector2):#如果size是Vector2类型,则表示椭圆外接矩形的大小
            super().SetSize(size)

            self.surface = pygame.Surface((self.r * 2,self.r * 2))
            self.surface.set_colorkey(Color.Black.value)
            self.surface = self.surface.convert_alpha()

            pygame.draw.circle(self.surface, self.color, (self.r,self.r), self.r, self.width)
            self.surface = pygame.transform.scale(self.surface, self.size.tuple)
        elif isinstance(size,float):#如果size是int类型,则表示圆的直径
            Debug.Log("Circle.SetSize(int)",type=DebugType.Success)
            self.r = size/2

            self.surface = pygame.Surface((self.r * 2,self.r * 2))
            self.surface.set_colorkey(Color.Black.value)
            self.surface = self.surface.convert_alpha()

            pygame.draw.circle(self.surface, self.color, (self.r,self.r), self.r, self.width)

    def Draw(self, surface: pygame.Surface):
        return super().Draw(surface)

    def GetData(self):
        return {
            'type':self.__class__,
            'data':{
                'position':self.position,
                'r':self.r,
                'color':self.color,
                'width':self.width,
            }
        }

    def Load(data):
        return Circle(data['position'],data['r'],data['color'],data['width'])
    