"""
可以通过以下接口来控制Xshell的会话。包括打开、关闭会话，记录会话日志等。
"""

Connected = False  # 当前会话是否连接
LocalAddress = "LocalAddress"  # 获取本地地址
Path = "Path"  # 获取当前会话文件路径
RemoteAddress = "RemoteAddress"  # 获取远端地址
RemotePort = "RemotePort"  # 获取远端端口号
Logging = False  # 当前会话是否正在记录日志文件
LogFilePath = "LogFilePath"  # 存放日志文件的路径


def Open(lpszSession: str):
    """
    打开新的会话或URL。
    :param lpszSession: xshell会话路径或xshell使用url格式
    """
    print("xsh.Session.Open({})".format(lpszSession))


def Close():
    """
    关闭当前连接的会话。
    """
    print("xsh.Session.Close()")


def Sleep(timeout: int):
    """
    设置xshell等待时间。
    :param timeout: 毫秒
    """
    print("xsh.Session.Sleep({})".format(timeout))


def LogFilePath(lpszNewFilePath: str):
    """
    指定日志文件路径。
    :param lpszNewFilePath: 文件名(包括路径)
    """
    print("xsh.Session.LogFilePath({})".format(lpszNewFilePath))


def StartLog():
    """
    开始记录会话。存储在LogFilePath()中指定的日志文件中，如果未指定路径，则使用默认路径
    """
    print("xsh.Session.StartLog()")


def StopLog():
    """
    停止记录会话。
    """
    print("xsh.Session.StopLog()")
