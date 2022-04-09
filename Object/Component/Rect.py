from Object.Base.BaseViewObject import BaseViewObject
from Object.Base.BaseSaveAbleObject import BaseSaveAbleObject
import pygame
from Math.Math import Vector2
from Color.Color import *

class Rect(BaseViewObject,BaseSaveAbleObject):
    '''
    矩形类
    '''
    def __init__(self, position: Vector2, size: Vector2,color : tuple = Color.KleinBlue.value,
                width: int = 0,r : int = 0):
        super().__init__(position, size)

        self.color = color
        self.width = width
        self.r = r

        self.surface = pygame.Surface(self.size.tuple)
        self.surface.set_colorkey(Color.Black.value)
        self.surface = self.surface.convert_alpha()
        pygame.draw.rect(self.surface, self.color, (0, 0, self.size.x, self.size.y), self.width, self.r)

    def SetPosition(self, position: Vector2):
        return super().SetPosition(position)

    def SetSize(self, size: Vector2):
        super().SetSize(size)
        self.surface = pygame.Surface(self.size.tuple)
        self.surface.set_colorkey(Color.Black.value)
        self.surface = self.surface.convert_alpha()

        pygame.draw.rect(self.surface, self.color, (0, 0, self.size.x, self.size.y), self.width, self.r)
    
    def SetScale(self, scale: float):
        super().SetScale(scale)
            
        self.surface = pygame.Surface(self.size.tuple)
        self.surface.set_colorkey(Color.Black.value)
        self.surface = self.surface.convert_alpha()

        pygame.draw.rect(self.surface, self.color, (0, 0, self.size.x, self.size.y), self.width, self.r)

    def SetColor(self, color: tuple):
        self.color = color

        self.surface = pygame.Surface(self.size.tuple)
        self.surface.set_colorkey(Color.Black.value)
        self.surface = self.surface.convert_alpha()

        pygame.draw.rect(self.surface, self.color, (0, 0, self.size.x, self.size.y), self.width, self.r)

    def Draw(self, surface: pygame.Surface):
        return super().Draw(surface)

    def GetData(self):
        return {
            'type':self.__class__,
            'data':{
                'position':self.position,
                'size':self.size,
                'color':self.color,
                'width':self.width,
                'r':self.r
            }
        }

    def Load(data):
        return Rect(data['position'],data['size'],data['color'],data['width'],data['r'])