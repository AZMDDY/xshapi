import xsh.Session
import xsh.Screen
import xsh.Dialog

def get_current_row_info(num: int):
    """
    获取终端当前行num个字符
    """
    screenRow = xsh.Screen.CurrentRow
    line = xsh.Screen.Get(screenRow, 1, screenRow, num)
    return line


def Main():
    # 打开一个已经存在的会话
    # xsh.Session.Open("ssh://user:pass_word@192.168.31.52:22")
    xsh.Session.Open("G:\\zzb\\Documents\\NetSarang Computer\\7\\Xshell\\Sessions\\192.168.31.52.xsh")
    xsh.Screen.Synchronous = True
    xsh.Session.Sleep(1000)

    # 切换到root用户
    xsh.Screen.Send("su root\r")
    xsh.Session.Sleep(100)
    line = get_current_row_info(30)
    if "Password" in line:
        xsh.Screen.Send("paas_word\n")

    
