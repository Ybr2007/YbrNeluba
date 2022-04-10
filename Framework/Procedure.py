from Debug.DebugLog import Debug, DebugType
import Framework.GlobalVariable as GlobalVariable
import Debug.Debug as Debugs

def SetProcedure(procedure,add : bool = False):
    '''
    改变流程
    参数:
        procedure:流程
    '''
    if procedure in GlobalVariable.procedurepFlow:
        GlobalVariable.currentProcedure = procedure
    else:
        if add:
            GlobalVariable.procedurepFlow.append(procedure)
            GlobalVariable.currentProcedure = procedure
        else:
            Debug.Log("当前的流程序列中不存在该流程，若要添加，请将add参数设置为True",type=DebugType.Warning)

def GetProcedure():
    '''
    获取当前流程
    返回:
        当前流程
    '''
    return GlobalVariable.currentProcedure

def InitProcedureFlow(procedures : list = []):
    GlobalVariable.procedurepFlow = procedures
