# 导入模块（python自带）
import os

# 尝试导入模块（需安装）
try:
    import pygame
    from pygame.locals import *
except ImportError:
    print("YbrEegol是基于pygame的，请先安装pygame")
    os._exit(0)

# 导入YbrNebula模块
from Math.Math import *
from Object.Base.Base import *
from Funcation.Funcation import *
from Saver.Saver import *
from Framework.Framework import *
from Framework.GlobalVariable import *
from Debug.Debug import *
from Object.Objects import *
from Color.Color import *