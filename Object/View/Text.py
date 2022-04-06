from Object.Base.BaseViewObject import BaseViewObject
from Object.Base.BaseSaveAbleObject import BaseSaveAbleObject
import pygame
from Math.Math import Vector2
from Color.Color import *

class Text(BaseViewObject,BaseSaveAbleObject):
    '''
    文本类
    '''
    def __init__(self, position: Vector2, fontSize : int = 36,text : str = 'Text',
                 color : tuple = Color.PrussianBlue.value,useSystemFont = True,fontName = '微软雅黑'):
        self.position = position
        self.fontSize = fontSize
        self.text = text
        self.color = color
        self.useSystemFont = useSystemFont
        self.fontName = fontName

        if useSystemFont:
            self.font = pygame.font.SysFont(fontName,fontSize)
        else:
            self.font = pygame.font.Font(fontName,fontSize)

        self.surface = self.font.render(self.text,True,self.color)

        self.oriSurface = self.surface

    def SetPosition(self, position: Vector2):
        return super().SetPosition(position)

    def SetSize(self, fontSize: int or Vector2 or float):
        if isinstance(fontSize,int) or isinstance(fontSize,float):
            fontSize = int(fontSize)
            self.fontSize = fontSize
            
            if self.useSystemFont:
                self.font = pygame.font.SysFont(self.fontName,fontSize)
            else:
                self.font = pygame.font.Font(self.fontName,fontSize)

            self.surface = self.font.render(self.text,True,self.color)
        elif isinstance(fontSize,Vector2):
            super().SetSize(fontSize)

            self.surface = pygame.transform.scale(self.oriSurface, self.size.tuple)

    def SetText(self, text: str):
        self.text = text
        self.surface = self.font.render(self.text,True,self.color)

    def Draw(self, surface: pygame.Surface):
        return super().Draw(surface)

    def GetData(self):
        return {
            'type':self.__class__,
            'data':{
                'position':self.position,
                'fontSize':self.fontSize,
                'text':self.text,
                'color':self.color,
                'useSystemFont':self.useSystemFont,
                'fontName':self.fontName
            }
        }
    
    def Load(data):
        return Text(data['position'],data['fontSize'],data['text'],
                data['color'],data['useSystemFont'],data['fontName'])