from Object.Base.BaseViewObject import BaseViewObject
from Object.Base.BaseUpdateObject import BaseUpdateObject
from Object.Base.BaseSaveAbleObject import BaseSaveAbleObject
from Math.Math import Vector2,zeroVector2
from Funcation.Funcation import *
from Object.Objects import Text,Image,Rect
from Color.Color import *
import pygame

class Button(BaseViewObject,BaseUpdateObject,BaseSaveAbleObject):
    def __init__(
        self,position : Vector2,size : Vector2,
        text : Text = Text(zeroVector2,text='',fontSize=24),
        rect : Rect = None,
        normalColor : tuple = Color.LightGray.value,
        hoverColor : tuple = Color.Gray.value,
        pressColor : tuple = Color.DarkGray.value,
        normalImage : Image = None,
        hoverImage : Image = None,
        pressImage : Image = None,
        atHoverCallBack : list = [],
        onHoverCallBack : list = [],
        atPressCallBack : list = [],
        onPressCallBack : list = [],
        atLeaveCallBack : list = [],
        onLeaveCallBack : list = [],
        atUpCallBack : list = [],
        onUpCallBack : list = [],
        mouseIds : list = [0],
    ):
        super().__init__(position,size)

        self.text = text
        self.oriTextSizeProportion = Vector2(self.text.size.x / self.size.x,self.text.size.y / self.size.y)
        SetPosWithProportion(self.text,self.position,self.position + self.size,0.5)

        if rect is None:
            rect = Rect(self.position,self.size)

        self.rect = rect
        if self.rect is not False:
            self.rect.SetPosition(self.position)
            self.rect.SetSize(self.size)
            self.rect.SetColor(normalColor)

        self.normalColor = normalColor
        self.hoverColor = hoverColor
        self.pressColor = pressColor

        self.normalImage = normalImage
        if self.normalImage is not None:
            SetPosWithProportion(self.normalImage,self.position,self.position + self.size,0.5)
        self.hoverImage = hoverImage
        if self.hoverImage is not None:
            SetPosWithProportion(self.hoverImage,self.position,self.position + self.size,0.5)
        self.pressImage = pressImage
        if self.pressImage is not None:
            SetPosWithProportion(self.pressImage,self.position,self.position + self.size,0.5)

        self.atHoverCallBack = atHoverCallBack
        self.onHoverCallBack = onHoverCallBack
        self.atPressCallBack = atPressCallBack
        self.onPressCallBack = onPressCallBack
        self.atLeaveCallBack = atLeaveCallBack
        self.onLeaveCallBack = onLeaveCallBack
        self.atUpCallBack = atUpCallBack
        self.onUpCallBack = onUpCallBack

        self.mouseIds = mouseIds

        self.isHover = False
        self.isPress = False

    def Draw(self,window : pygame.Surface):
        if self.rect is not False:
            self.rect.Draw(window)
        self.text.Draw(window)
        if self.isPress:
            if self.pressImage:
                self.pressImage.Draw(window)
            if self.rect is not False:
                self.rect.SetColor(self.pressColor)
        elif self.isHover:
            if self.hoverImage:
                self.hoverImage.Draw(window)
            if self.rect is not False:
                self.rect.SetColor(self.hoverColor)
        else:
            if self.normalImage:
                self.normalImage.Draw(window)
            if self.rect is not False:
                self.rect.SetColor(self.normalColor)

    def Update(self,event = None):
        if not pygame.mouse.get_focused():
            for func in self.onLeaveCallBack:
                func()

            if self.isHover:
                for func in self.atLeaveCallBack:
                    func()

            self.isHover = False

            for func in self.onUpCallBack:
                func()

            if self.isPress:
                for func in self.atUpCallBack:
                    func()

            self.isPress = False

            return

        x,y = pygame.mouse.get_pos()

        if self.position.x <= x <= self.position.x + self.size.x \
            and self.position.y <= y <= self.position.y + self.size.y:
            for func in self.onHoverCallBack:
                func()

            if not self.isHover:
                for func in self.atHoverCallBack:
                    func()

            self.isHover = True

            for _id in self.mouseIds:
                if pygame.mouse.get_pressed()[_id]:
                    for func in self.onPressCallBack:
                        func()

                    if not self.isPress:
                        for func in self.atPressCallBack:
                            func() 
                    
                    self.isPress = True

                    return 

            for func in self.onUpCallBack:
                func()

            if self.isPress:
                for func in self.atUpCallBack:
                    func()

            self.isPress = False

        else:
            for func in self.onLeaveCallBack:
                func()

            if self.isHover:
                for func in self.atLeaveCallBack:
                    func()

            self.isHover = False

            for func in self.onUpCallBack:
                func()

            if self.isPress:                    
                for func in self.atUpCallBack:
                    func()              

            self.isPress = False

    def SetPosition(self, position: Vector2):
        super().SetPosition(position)

        SetPosWithProportion(self.text,self.position,self.position + self.size,0.5)
        if self.rect is not False:
            self.rect.SetPosition(self.position)
        if self.normalImage:
            SetPosWithProportion(self.normalImage,self.position,self.position + self.size,0.5)
        if self.hoverImage:
            SetPosWithProportion(self.hoverImage,self.position,self.position + self.size,0.5)
        if self.pressImage:
            SetPosWithProportion(self.pressImage,self.position,self.position + self.size,0.5)

    def SetSize(self, size: Vector2,newFontSize : int or str = None):
        super().SetSize(size)

        if newFontSize is not None:
            if isinstance(newFontSize,int):
                self.text.SetFontSize(newFontSize)
            elif isinstance(newFontSize,str):
                self.text.SetSize(self.size)
        SetPosWithProportion(self.text,self.position,self.position + self.size,0.5)

        if self.rect is not False:
            self.rect.SetSize(self.size)
            self.rect.SetPosition(self.position)

        self.text.SetSize(Vector2(self.size.x * self.oriTextSizeProportion.x,self.size.y * self.oriTextSizeProportion.y))
        SetPosWithProportion(self.text,self.position,self.position + self.size,0.5)

        if self.normalImage:
            SetPosWithProportion(self.normalImage,self.position,self.position + self.size,0.5)
        if self.hoverImage:
            SetPosWithProportion(self.hoverImage,self.position,self.position + self.size,0.5)
        if self.pressImage:
            SetPosWithProportion(self.pressImage,self.position,self.position + self.size,0.5)

    def SetScale(self, scale: float):
        super().SetScale(scale)

        self.text.SetScale(scale)
        SetPosWithProportion(self.text,self.position,self.position + self.size,0.5)

        if self.rect is not False:
            self.rect.SetSize(self.size)
            self.rect.SetPosition(self.position)
        
        if self.normalImage:
            self.normalImage.SetScale(scale)
        if self.hoverImage:
            self.hoverImage.SetScale(scale)
        if self.pressImage:
            self.pressImage.SetScale(scale)

    def GetData(self):
        return {
            'type':self.__class__,
            'data':{
                'position':self.position,
                'size':self.size,
                'text':self.text.GetData(),
                'rect':self.rect.GetData(),
                'normalColor':self.normalColor,
                'hoverColor':self.hoverColor,
                'pressColor':self.pressColor,
                'normalImage':self.normalImage.GetData() if self.normalImage else None,
                'hoverImage':self.hoverImage.GetData() if self.hoverImage else None,
                'pressImage':self.pressImage.GetData() if self.pressImage else None,
                'atHoverCallBack':self.atHoverCallBack,
                'onHoverCallBack':self.onHoverCallBack,
                'atPressCallBack':self.atPressCallBack,
                'onPressCallBack':self.onPressCallBack,
                'atLeaveCallBack':self.atLeaveCallBack,
                'onLeaveCallBack':self.onLeaveCallBack,
                'atUpCallBack':self.atUpCallBack,
                'onUpCallBack':self.onUpCallBack,
                'mouseIds':self.mouseIds,
            }
        }

    def Load(data):
        return Button(data['position'],data['size'],
        data['text']['type'].Load(data['text']['data']),data['rect']['type'].Load(data['rect']['data']),
        data['normalColor'],data['hoverColor'],data['pressColor'],
        data['normalImage'],data['hoverImage'],data['pressImage']
        ,data['atHoverCallBack'],data['onHoverCallBack'],data['atPressCallBack'],
        data['onPressCallBack'],data['atLeaveCallBack'],data['onLeaveCallBack'],
        data['atUpCallBack'],data['onUpCallBack'],data['mouseIds'])