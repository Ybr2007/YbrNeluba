class CallBack:
    def __init__(self,func,*args,**kwargs):
        self.__func = func
        self.__args = args
        self.__kwargs = kwargs

    def __call__(self):
        self.__func(*self.__args,**self.__kwargs)