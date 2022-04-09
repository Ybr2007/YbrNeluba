import math
class Matrix:
    '''
    YbrPygame Max 中的矩阵
    '''
    def __init__(self,row,col,data = None):
        '''
        初始化
        参数:
            rows:行数
            cols:列数
        '''
        assert isinstance(row,int) and isinstance(col,int) and row > 0 and col > 0 , "矩阵行列数必须为正整数"
        assert data is None or isinstance(data,list) and len(data) == row and len(data[0]) == col , "矩阵数据必须为二维列表，且行数和列数必须与矩阵行列数相等"
        if data:
            self.data = data
        else:
            self.data = [[0 for i in range(col)] for j in range(row)]
        self.row = row
        self.col = col

    def __str__(self):
        '''
        转换为字符串
        '''
        return "Matrix:"+str(self.data)

    def __getitem__(self,index):
        '''
        获取某个元素
        '''
        return self.data[index]

    def __setitem__(self,index,value):
        '''
        设置某个元素
        '''
        self.data[index] = value

    def __add__(self,other):
        '''
        加法
        '''
        if self.row == other.row and self.col == other.col:
            result = Matrix(self.row,self.col)
            for i in range(self.row):
                for j in range(self.col):
                    result[i][j] = self[i][j] + other[i][j]
            return result
        else:
            raise Exception("矩阵维度不匹配")

    def __sub__(self,other):
        '''
        减法
        '''
        if self.row == other.row and self.col == other.col:
            result = Matrix(self.row,self.col)
            for i in range(self.row):
                for j in range(self.col):
                    result[i][j] = self[i][j] - other[i][j]
            return result
        else:
            raise Exception("矩阵维度不匹配")

    def __mul__(self,other):
        '''
        乘法
        '''
        if isinstance(other,Matrix):
            if self.col == other.row:
                result = Matrix(self.row,other.col)
                for i in range(self.row):
                    for j in range(other.col):
                        for k in range(self.col):
                            result[i][j] += self[i][k] * other[k][j]
                return result
            else:
                raise Exception("矩阵维度不匹配,矩阵A:",str(self),"矩阵B:",str(other))
        else:
            if isinstance(other,int) or isinstance(other,float):
                result = Matrix(self.row,self.col)
                for i in range(self.row):
                    for j in range(self.col):
                        result[i][j] = self[i][j] * other
                return result

    def __truediv__(self,other : float or int): 
        '''
        除法
        '''
        result = Matrix(self.row,self.col)
        for i in range(self.row):
            for j in range(self.col):
                result[i][j] = self[i][j] / other
        return result

    def Fill(self,value):
        '''
        填充
        '''
        for i in range(self.row):
            for j in range(self.col):
                self[i][j] = value

    def __call__(self,other):
        return self * other
