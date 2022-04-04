from Math.Matrix import Matrix
import math

class Vector2(Matrix):
    '''
    YbrPygame Max 中的2维向量
    '''
    def __init__(self,x,y):
        '''
        初始化
        参数:
            x:x坐标
            y:y坐标
        '''
        super().__init__(3,1,[[x],[y],[1]])
        self.x = x
        self.y = y
        self.tuple = (x,y)
        self.length = math.sqrt(x**2 + y**2)

    def Update(self):
        self.tuple = (self.x,self.y)
        self.length = math.sqrt(self.x**2 + self.y**2)

    def __add__(self, other):
        return MatrixToVector2(super().__add__(other))

    def __sub__(self, other):
        return MatrixToVector2(super().__sub__(other))
    
    def __mul__(self, other):
        '''
        乘法
        '''
        if isinstance(other,Vector2):
            return self.x * other.x + self.y * other.y
        else:
            return MatrixToVector2(super().__mul__(other))

    def __truediv__(self, other):
        '''
        除法
        '''
        return Vector2(self.x / other,self.y / other)

    def __str__(self):
        '''
        转换为字符串
        '''
        return str(self.tuple)

class Vector3(Matrix):
    '''
    YbrPygame Max 中的3维向量
    '''
    def __init__(self,x,y,z):
        '''
        初始化
        参数:
            x:x坐标
            y:y坐标
            z:z坐标
        '''
        super().__init__(4,1,[[x],[y],[z],[1]])
        self.x = x
        self.y = y
        self.z = z
        self.tuple = (x,y,z)
        self.length = math.sqrt(x**2 + y**2 + z**2)
    def Update(self):
        self.tuple = (self.x,self.y,self.z)
        self.length = math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, other):
        return MatrixToVector3(super().__add__(other))
    
    def __sub__(self, other):
        return MatrixToVector3(super().__sub__(other))

    def __mul__(self, other):
        '''
        乘法
        '''
        if isinstance(other,Vector3):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            return MatrixToVector3(super().__mul__(other))

    def __truediv__(self, other):
        '''
        除法
        '''
        return Vector3(self.x / other,self.y / other,self.z / other)
    
    def __str__(self):
        '''
        转换为字符串
        '''
        return str(self.tuple)

# 矩阵与向量的转换

def Vector2ToMatrix(vector):
    '''
    向量转矩阵
    '''
    return Matrix(3,1,[[vector.x],[vector.y],[1]])

def Vector3ToMatrix(vector):
    '''
    向量转矩阵
    '''
    return Matrix(4,1,[[vector.x],[vector.y],[vector.z],[1]])

def MatrixToVector2(matrix):
    '''
    矩阵转向量
    '''
    return Vector2(matrix[0][0],matrix[1][0])

def MatrixToVector3(matrix):
    '''
    矩阵转向量
    '''
    return Vector3(matrix[0][0],matrix[1][0],matrix[2][0])

# 常量
zeroVector2 = Vector2(0,0)
zeroVector3 = Vector3(0,0,0)
oneVector2 = Vector2(1,1)
oneVector3 = Vector3(1,1,1)

#对向量的特殊变换矩阵

def TranslationMatrix2D(x,y):
    '''
    2d平移矩阵
    '''
    return Matrix(3,3,[
        [1,0,x,],
        [0,1,y,],
        [0,0,1,],
    ])

def TranslationMatrix3D(x,y,z):
    '''
    3d平移矩阵
    '''
    return Matrix(4,4,[
        [1,0,0,x,],
        [0,1,0,y,],
        [0,0,1,z,],
        [0,0,0,1,],
    ])

def ScaleMatrix2D(x,y):
    '''
    2d缩放矩阵
    '''
    return Matrix(3,3,[
        [x,0,0,],
        [0,y,0,],
        [0,0,1,],
    ])

def ScaleMatrix3D(x,y,z):
    '''
    3d缩放矩阵
    '''
    return Matrix(4,4,[
        [x,0,0,0,],
        [0,y,0,0,],
        [0,0,z,0,],
        [0,0,0,1,],
    ])

def RotationMatrix2D(angle,center=Vector2(0,0)):
    '''
    2d旋转矩阵
    '''
    angle = math.radians(angle)
    return TranslationMatrix2D(center.x,center.y)*Matrix(3,3,[
        [math.cos(angle) ,math.sin(angle),0,],
        [-math.sin(angle),math.cos(angle),0,],
        [0               ,              0,1,],
    ])*TranslationMatrix2D(-center.x,-center.y)

def RotationZMatrix3D(angle,center=Vector3(0,0,0)):
    '''
    3d旋转矩阵(x轴)
    '''
    angle = math.radians(angle)
    return TranslationMatrix3D(center.x,center.y,center.z)*Matrix(4,4,[
        [math.cos(angle),-math.sin(angle),0,0,],
        [math.sin(angle),math.cos(angle) ,0,0,],
        [0              ,               0,1,0,],
        [0              ,               0,0,1,],
    ])*TranslationMatrix3D(-center.x,-center.y,-center.z)

def RotationYMatrix3D(angle,center=Vector3(0,0,0)):
    '''
    3d旋转矩阵(y轴)
    '''
    angle = math.radians(angle)
    return TranslationMatrix3D(center.x,center.y,center.z)*Matrix(4,4,[
        [math.cos(angle),0,math.sin(angle),0,],
        [0              ,1,0              ,0,],
        [-math.sin(angle),0,math.cos(angle),0,],
        [0              ,0,0              ,1,],
    ])*TranslationMatrix3D(-center.x,-center.y,-center.z)

def RotationXMatrix3D(angle,center=Vector3(0,0,0)):
    '''
    3d旋转矩阵(x轴)
    '''
    angle = math.radians(angle)
    return TranslationMatrix3D(center.x,center.y,center.z)*Matrix(4,4,[
        [1,               0,              0,0,],
        [0, math.cos(angle),math.sin(angle),0,],
        [0,-math.sin(angle),math.cos(angle),0,],
        [0,               0,              0,1,],
    ])*TranslationMatrix3D(-center.x,-center.y,-center.z)
