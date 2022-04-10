from Object.Base.BasePhysicalObject import BasePhysicalObject
from Math.Math import Vector2

def SetPosWithProportion(obj : BasePhysicalObject,position1 : Vector2,position2 : Vector2,proportion : float or Vector2):
    w,h = obj.size.tuple
    if isinstance(proportion,Vector2):
        _x,_y = proportion.tuple
        x = position1.x + (position2.x - position1.x) * _x
        y = position1.y + (position2.y - position1.y) * _y
    else:
        x = position1.x + (position2.x - position1.x) * proportion
        y = position1.y + (position2.y - position1.y) * proportion

    obj.SetPosition(Vector2(x - w/2,y - h/2))

def EasingSetPosWithProportion(obj : BasePhysicalObject,position1 : Vector2,position2 : Vector2,proportion : float or Vector2):
    w,h = obj.size.tuple
    if isinstance(proportion,Vector2):
        _x,_y = proportion.tuple
        x = position1.x + (position2.x - position1.x) * _x
        y = position1.y + (position2.y - position1.y) * _y

    else:
        x = position1.x + (position2.x - position1.x) * proportion
        y = position1.y + (position2.y - position1.y) * proportion

    obj.SetPosition(obj.position + (Vector2(x - obj.position.x - w/2,y - obj.position.y - h/2) * 0.1))

def SetCenterPos(obj : BasePhysicalObject,position : Vector2):
    w,h = obj.size.tuple
    obj.SetPosition(position - Vector2(w/2,h/2))

def EasingSetCenterPos(obj : BasePhysicalObject,position : Vector2):
    w,h = obj.size.tuple
    obj.SetPosition(obj.position + (position - obj.position) * 0.1)