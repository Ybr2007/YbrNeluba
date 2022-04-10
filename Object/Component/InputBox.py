from matplotlib.pyplot import text
from Object.Base.BasePhysicalObject import BasePhysicalObject
from Object.Base.BaseUpdateObject import BaseUpdateObject
from Object.Base.BaseSaveAbleObject import BaseSaveAbleObject
from Object.Component.Text import Text
from Object.Component.Button import Button
from Color.Color import Color
from Funcation.CallBack import CallBack
from Math.Math import *
import pygame

class EnInputBox(BasePhysicalObject,BaseUpdateObject,BaseSaveAbleObject):
    def __init__(
        self,position : Vector2,size : Vector2,text : Text = Text(zeroVector2,text=''),
        normalColor : tuple = Color.LightGray.value,
        focusColor : tuple = Color.PrussianBlue.value,
        callback : list = []
        ):
        BasePhysicalObject.__init__(self,position,size)

        self.txt = ''

        self.text = text
        self.text.SetText('')
        self.text.SetCenterPos(self.position + self.size/2)
        self.btn = Button(
            position,size,
            rect=False,
            )
        self.normalColor = normalColor
        self.focusColor = focusColor

        self.callback = callback

        self.isFocus = False
        self.oriSize = size

    def Keep(self):
        self.text.SetPosWithProportion(self.position , self.position + self.size , 0.5)
        self.text.SetPosition(Vector2(self.position.x + 10,self.text.position.y))
        self.btn.SetPosition(self.position)
        self.btn.SetSize(self.size)
        
        if self.text.surface.get_width() + 20 > self.oriSize.x:
            self.SetSize(Vector2(self.text.surface.get_width() + 20,self.size.y))
        else:
            self.SetSize(self.oriSize)

    def Draw(self,surface : pygame.Surface):
        self.Keep()
        if self.isFocus:
            pygame.draw.rect(
                surface,self.focusColor,(self.position.x,self.position.y,self.size.x,self.size.y),
                2
            )
        else:
            pygame.draw.rect(
                surface,self.normalColor,(self.position.x,self.position.y,self.size.x,self.size.y),
                2
            )
        self.text.Draw(surface)

    def SetPosition(self, position: Vector2):
        return super().SetPosition(position)

    def SetSize(self, size: Vector2):
        self.btn.SetSize(size)
        return super().SetSize(size)

    def SetScale(self, scale: float):
        return super().SetScale(scale)

    def Update(self, event : pygame.event.Event):
        self.btn.Update(event)
        if self.btn.isPress:
            self.isFocus = True
        
        if not self.btn.isHover and pygame.mouse.get_pressed()[0]:
            self.isFocus = False

        if self.isFocus:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.txt = self.txt[:-1]
                elif event.key == pygame.K_RETURN:
                    for func in self.callback:
                        func(self.txt)
                    self.txt = ''
                else:
                    self.txt += event.unicode
        self.text.SetText(self.txt)

    def GetData(self):
        return {
            'type':self.__class__,
            'data':{
                'position':self.position,
                'size':self.size,
                'text':self.text.GetData(),
                'normalColor':self.normalColor,
                'focusColor':self.focusColor,
                'callback':self.callback,
            }
        }

    def Load(data):
        return EnInputBox(
            position=data['position'],
            size=data['size'],
            text=Text.Load(data['text']),
            normalColor=data['normalColor'],
            focusColor=data['focusColor'],
            callback=data['callback'],
        )
