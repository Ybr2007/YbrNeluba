from Object.Base.BaseViewObject import BaseViewObject
from Object.Base.BaseUpdateObject import BaseUpdateObject
from Object.Base.BaseSaveAbleObject import BaseSaveAbleObject
from Object.Base.BasePhysicalObject import BasePhysicalObject
from Math.Math import *
from Debug.DebugLog import Debug,DebugType
import pygame

class BaseSet(BaseViewObject,BaseUpdateObject,BaseSaveAbleObject):
    '''
    实体组件集合
    '''
    def __init__(self,position : Vector2,size : Vector2,
                objects : list = None
                ):
        super().__init__(position,size)
        
        if objects is None:
            self.objects = []
        else:
            self.objects = objects
    
    def SetPosition(self, position: Vector2):
        '''
        设置位置
        '''
        dPos = position - self.position

        self.position = position

        for obj in self.objects:
            if isinstance(obj,BasePhysicalObject):
                obj.SetPosition(obj.position + dPos)

    def SetSize(self, size: Vector2):#TODO:修复子object的size不随着Set的size变化的BUG
        '''
        设置大小
        '''
        if self.size.x == 0:
            self.size.x = 1e-18 
        if self.size.y == 0:
            self.size.y = 1e-18

        dSizeX = size.x / self.size.x
        dSizeY = size.y / self.size.y


        self.size = size

        for obj in self.objects:
            if isinstance(obj,BasePhysicalObject):
                obj.SetSize(Vector2(obj.size.x * dSizeX,obj.size.y * dSizeY))

    def Update(self):
        '''
        更新
        '''
        for obj in self.objects:
            if isinstance(obj,BaseUpdateObject):
                obj.Update()

    def Draw(self, surface: pygame.Surface,drawFrame: bool = False):
        '''
        绘制
        '''
        for obj in self.objects:
            if isinstance(obj,BaseViewObject):
                obj.Draw(surface)
        if drawFrame:
            pygame.draw.rect(surface,(255,0,0),(self.position.x,self.position.y,self.size.x,self.size.y),1)

    def GetData(self):
        l = []
        for obj in self.objects:
            if isinstance(obj,BaseSaveAbleObject):
                l.append(obj.GetData())
            else:
                Debug.Log("若要保存Set,则Set的object必须是BaseSaveAbleObject的子类",type=DebugType.Error)
        return {
            'type':self.__class__,
            'data':{
                'position':self.position,
                'size':self.size,
                'objects':l
            }
        }

    def Load(data):
        '''
        加载
        '''
        return BaseSet(
            position=data['data']['position'],
            size=data['data']['size'],
            objects=[obj['type'](obj[data]) for obj in data['data']['objects']]
        )