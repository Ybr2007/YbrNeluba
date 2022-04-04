'''
1.0.0
Time:2022.4.5
测试：
1.Object基类
2.CallBack
3.矩阵与向量
'''

import YbrEegol

#1.Object基类
class Obj(YbrEegol.BaseObject):
    def __init__(self):
        print("A new Obj is created")

obj = Obj()

#2.CallBack
callBack = YbrEegol.CallBack(print,"CallBack","is called")
callBack()

#3.矩阵与向量
v = YbrEegol.Vector2(1,2)
print(v)
m = YbrEegol.Matrix(3,3,[[1,0,0],[0,1,0],[0,0,1]])
print(YbrEegol.MatrixToVector2(m(v)))