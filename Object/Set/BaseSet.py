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
            for obj in self.objects:
                if not isinstance(obj,BasePhysicalObject):
                    Debug.Log("Set中的Object必须是实体组件",type=DebugType.Error)
                    raise TypeError("Set中的Object必须是实体组件")

        self.PosProportions = []
        for obj in self.objects:
            if isinstance(obj,BasePhysicalObject):
                self.PosProportions.append(Vector2(obj.position.x / self.size.x,obj.position.y / self.size.y))
            
        self.SizeProportions = []
        for obj in self.objects:
            if isinstance(obj,BasePhysicalObject):
                self.SizeProportions.append(Vector2(obj.size.x / self.size.x,obj.size.y / self.size.y))

    def Keep(self):
        '''
        保持组件位置和大小
        '''
        for obj in self.objects:
            if isinstance(obj,BasePhysicalObject):
                obj.SetPosition(Vector2(self.PosProportions[self.objects.index(obj)].x * self.size.x,
                                            self.PosProportions[self.objects.index(obj)].y * self.size.y))

                obj.SetSize(Vector2(self.SizeProportions[self.objects.index(obj)].x * self.size.x,
                                            self.SizeProportions[self.objects.index(obj)].y * self.size.y))
    
    def SetPosition(self, position: Vector2):
        '''
        设置位置
        '''
        dPos = position - self.position

        self.position = position

        self.Keep()

    def SetSize(self, size: Vector2):
        '''
        设置大小
        '''
        dSizeX = size.x - self.size.x
        dSizeY = size.y - self.size.y

        super().SetSize(size)

        self.Keep()

    def SetScale(self, scale: float):
        newSize = scale / self.size.x
        self.size = Vector2(scale,self.size.y * newSize)

        self.Keep()

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
            position=data['position'],
            size=data['size'],
            objects=[obj['type'].Load(obj['data']) for obj in data['objects']]
        )