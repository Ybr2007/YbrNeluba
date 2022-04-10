from enum import Enum

class BaseObjectStateType(Enum):
    '''
    对象状态类型
    '''
    Available = 1
    UpateAble = 2
    DrawAble = 3
    Destroyed = 4
    isChanging = 5
    