# 导入模块
import abc

class BaseObject(metaclass = abc.ABCMeta):
    '''
    所有Object的基类
    '''
    @abc.abstractmethod
    def __init__(self):
        pass
