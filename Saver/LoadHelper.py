# 导入模块
from Object.Base.BaseSaveAbleObject import BaseSaveAbleObject
import shelve

def Load(path : str,key : str) -> BaseSaveAbleObject:
    with shelve.open(path) as db:
        if isinstance(db[key],BaseSaveAbleObject):
            return db[key]
        obj = db[key]['type'].Load(db[key]['data'])
    return obj