from Object.Base.BasePhysicalObject import BasePhysicalObject
from Math.Math import Vector2

def SetPosWithProportion(obj : BasePhysicalObject,position1 : Vector2,position2 : Vector2,proportion : float):
    w,h = obj.size.tuple

    x = position1.x + (position2.x - position1.x) * proportion
    y = position1.y + (position2.y - position1.y) * proportion

    obj.SetPosition(Vector2(x - w/2,y - h/2))