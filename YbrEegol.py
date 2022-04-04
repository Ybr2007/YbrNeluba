# 导入模块（python自带）
import os

# 尝试导入模块（需安装）
try:
    import pygame
    from pygame.locals import *
except ImportError:
    print("YbrEegol是基于pygame的，请先安装pygame")
    os._exit(0)

# 导入YbrEegol模块
from Math.Math import *
from Object.Base.Base import *
from Funcation.Funcation import *