"""
可以通过以下接口处理Xshell的终端屏幕。包括清空终端内容，向终端发送字符串、获取字符串以及等待特定回显字符串
"""


CurrentColumn: int  # 当前列
CurrentRow: int  # 当前行
Columns: int  # 获取与终端的列宽相同的列数
Rows: int  # 获取与终端的行高相同的列数
Synchronous: bool  # 设置屏幕是否同步


def Clear():
    """
    清空终端屏幕内容
    """
    print("xsh.Screen.Clear()")


def Send(lpszStrToSend: str):
    """
    向终端发送信息
    :param lpszStrToSend: 向终端发送的字符串
    """
    print("xsh.Screen.Send({})".format(lpszStrToSend))


def Get(nBegRow: int, nBegCol: int, nEndRow: int, nEndCol: int):
    """
    从终端指定区域获取字符串
    :param nBegRow: 终端中起始行位置
    :param nBegCol: 终端中起始列位置
    :param nEndRow: 终端中结束行位置
    :param nEndCol: 终端中结束列位置
    :return: 返回获取到的字符串信息
    """
    print("xsh.Screen.Get({}, {}, {}, {})".format(nBegRow, nBegCol, nEndRow, nEndCol))
    return "terminal information"


def WaitForString(lpszString: str):
    """
    等待直到在终端中输入指定的字符串
    :param lpszString: 需要匹配的字符串
    """
    print("xsh.Screen.WaitForString({})".format(lpszString))


def WaitForStrings(strArray: list, nTimeout: int):
    """
     等待指定的时间，直到在终端中输入指定的字符串或超时
    :param strArray: 匹配的字符串列表
    :param nTimeout: 超时时间(毫秒)
    :return: 1: 匹配到了，0: 未匹配到或超时
    """
    print("xsh.Screen.WaitForStrings({}, {})".format(strArray, nTimeout))
    return 0
