from enum import Enum

class Color(Enum):
    Red = (255, 0, 0)
    Green = (0, 255, 0)
    Blue = (0, 0, 255)

    Yellow = (255, 255, 0)
    Magenta = (255, 0, 255)
    Cyan = (0, 255, 255)

    White = (255, 255, 255)
    Black = (0, 0, 0)

    LightGray = (192, 192, 192)
    Gray = (128, 128, 128)
    DarkGray = (64, 64, 64)

    WhiteGray = (229,229,229)
    KleinBlue = (0, 47, 167)
    PrussianBlue = (0, 49, 83)
    MarrsGreen = (1, 132, 127)
    ShenbulunYellow = (251, 210, 106)
    BurgundyRed = (71, 0, 36)
    VandykeBrown = (73, 45, 34)

def HexToRGB(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

def RGBToHex(rgb):
    return '#%02x%02x%02x' % rgb
