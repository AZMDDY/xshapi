# XShell Script API (Python)

> XShell支持使用VB,JS,Python脚本去启动自动化任务。官方提供了相关的API， 由于没有相关的包可以直接使用，需要我们对照这官方文档去写脚本，
> 个人感觉不是很方便，所以在此对官方API进行打包，以便于在写脚本时能够快速而准确的调用官方API。

借助本项目开发xshell的python脚本的优点:

+ 移植方便：由于本项目中所有关于xsh的API和官方同名，所以在利用本项目开发完脚本后，仅仅需要注释掉导入的语句即可使用。
+ 快速而准确：借助本项目开发脚本，大大减少了错误使用API的概率，因为提供了比较详细的注释。

## 示例

### example-1: 自动切换到root用户

```Python
# import xsh.Session
# import xsh.Screen
# import xsh.Dialog

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
    xsh.Session.Open("G:\\user\\Documents\\NetSarang Computer\\7\\Xshell\\Sessions\\192.168.31.52.xsh")
    xsh.Screen.Synchronous = True
    xsh.Session.Sleep(1000)

    # 切换到root用户
    xsh.Screen.Send("su root\r")
    xsh.Session.Sleep(100)
    line = get_current_row_info(30)
    if "Password" in line:
        xsh.Screen.Send("paas_word\n")

```

## example-2: 登录另一台设备

```Python
# import xsh.Session
# import xsh.Screen
# import xsh.Dialog
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
    if re.search("paasword", line, flags=re.I):
        xsh.Screen.Send("yes\r")
    if "password" in line:
        xsh.Screen.Send("paas_word\r")
    
```
