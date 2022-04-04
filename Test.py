'''
1.0.1
Time:2022.4.5
1.测试Saver
'''

import YbrEegol
import pygame

class Obj(YbrEegol.BaseSaveAbleObject):
    def __init__(self,x,y):
        self.surface = pygame.Surface((x,y))
    
    def GetData(self):
        return {
            'type':self.__class__,
            'data':{
                'x':self.surface.get_width(),
                'y':self.surface.get_height()
            }
        }

    def Load(data):
        return Obj(data['x'],data['y'])

obj = Obj(100,200)
print(obj.GetData())
YbrEegol.Save(obj,'test','obj')
obj2 = YbrEegol.Load('test','obj')
print(obj2.surface.get_width(),obj2.surface.get_height())