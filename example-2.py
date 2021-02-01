import xsh.Session
import xsh.Screen
import xsh.Dialog
import re


def get_current_row_info(num: int):
    """
    获取终端当前行num个字符
    """
    screenRow = xsh.Screen.CurrentRow
    line = xsh.Screen.Get(screenRow, 1, screenRow, num)
    return line


def Main():
    # 在一个存在的会话中执行
    xsh.Screen.Synchronous = True
    xsh.Session.Sleep(1000)

    xsh.Screen.Send("ssh zzb@192.168.31.52\r")
    xsh.Session.Sleep(100)

    # 当第一次登录时，会验证初始ssh连接
    line = get_current_row_info(100)
    if re.search("yes/no", line):
        xsh.Screen.Send("yes\r")
        xsh.Session.Sleep(100)

    # 终端出现提示输入密码时，输入密码
    line = get_current_row_info(100)
    if re.search("password", line, flags=re.I):
        xsh.Screen.Send("pass_word\r")
    
