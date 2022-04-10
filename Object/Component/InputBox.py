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
        self,positon : Vector2,size : Vector2,text : Text = Text(zeroVector2,text=''),
        normalColor : tuple = Color.LightGray.value,
        focusColor : tuple = Color.PrussianBlue.value,
        callback : CallBack = None
        ):
        BasePhysicalObject.__init__(self,positon,size)

        self.txt = ''

        self.text = text
        self.text.SetPosition(self.position)
        self.btn = Button(
            positon,size,
            rect=False,
            )
        self.normalColor = normalColor
        self.focusColor = focusColor

        self.callback = callback

        self.isFocus = False

    def Keep(self):
        self.text.SetPosition(self.position)
        self.btn.SetPosition(self.position)
        self.btn.SetSize(self.size)

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
                    if self.callback is not None:
                        self.callback(self.txt)
                    self.txt = ''
                else:
                    self.txt += event.unicode
        self.text.SetText(self.txt)
        self.SetSize(Vector2(max(self.text.surface.get_width()*1.1,self.size.x),self.size.y))

    def GetData(self):
        raise NotImplementedError

    def Load(data):
        raise NotImplementedError