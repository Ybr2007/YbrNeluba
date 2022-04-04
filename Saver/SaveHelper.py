# 导入模块
from Object.Base.BaseSaveAbleObject import BaseSaveAbleObject
import shelve

def Save(obj : BaseSaveAbleObject,path : str,key : str):
    with shelve.open(path) as db:
        db[key] = obj.GetData()