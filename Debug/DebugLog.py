from enum import Enum
import Framework.GlobalVariable as GlobalVariable

class DebugType(Enum):
    Print = 'Print'
    Warning = 'Warning'
    Error = 'Error'
    Success = 'Success'
    Info = 'Info'
    Debug = 'Debug'

class Debug(object):

    __record = []

    @staticmethod
    def Log(*args,type=DebugType.Print,record=True):
        # 设置控制台颜色
        if type == DebugType.Print:
            print('\033[0m'+type.value+":")
        elif type == DebugType.Warning:
            print('\033[0;33m'+type.value+":")
        elif type == DebugType.Error:
            print('\033[0;31m'+type.value+":")
        elif type == DebugType.Success:
            print('\033[0;32m'+type.value+":")
        elif type == DebugType.Info:
            print('\033[0;36m'+type.value+":")
        elif type == DebugType.Debug:
            print('\033[0;35m'+type.value+":")
        if record:
            Debug.__record.append((type,args,GlobalVariable.runTime))
        print(' ',end='')
        print(*args,'\033[0m')

    @staticmethod
    def Record():
        print("\033[3;44m"+"Record:"+str(len(Debug.__record)),"\033[0m")
        for i in Debug.__record:
            print('\033[3;46m'+"At:"+str(i[2])+'\033[0m',end='')
            Debug.Log(i[1],type=i[0],record=False)
        print('\033[3;44m'+"End"+'\033[0m')
