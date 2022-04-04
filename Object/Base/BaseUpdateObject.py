# 导入模块
from Object.Base.BaseObject import BaseObject
import abc

class BaseUpdateObject(BaseObject,metaclass = abc.ABCMeta):
    '''
    所有可更新Object的基类
    '''
    @abc.abstractmethod
    def Update(self):
        '''
        更新
        '''
        pass