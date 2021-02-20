import xsh.Session
import xsh.Screen
import xsh.Dialog
import re


def sleep(ms: int):
    xsh.Session.Sleep(ms)


def get_row_info(row: int, chr_num: int):
    """
    获取第row行的前chr_num个字符
    row=0表示终端中最新的一行
    """
    n_row = xsh.Screen.CurrentRow - row
    return xsh.Screen.Get(n_row, 1, n_row, chr_num)


def wait(msg: str, timeout=0):
    """
    等待终端当前行出现期望的内容(不区分大小写)，直到超时或者找到
    timeout: 超时时间，单位秒，当为0时，表示一直等待
    """
    ret = False
    count = 0
    while not ret:
        ret = re.search(msg, get_row_info(0, 200), re.I)
        if ret:
            return True
        if timeout > 0 and count >= timeout * 10:
            return False
        count += 1
        sleep(100)


def wait_no(msg: str, timeout=0):
    """
    等待终端当前行不出现期望的内容(不区分大小写)，直到超时或者不出现
    timeout: 超时时间，单位秒，当为0时，表示一直等待
    """
    ret = False
    count = 0
    while ret:
        ret = re.search(msg, get_row_info(0, 200), re.I)
        if not ret:
            return True
        if timeout > 0 and count >= timeout * 10:
            return False
        count += 1
        sleep(100)


def send(msg: str, wait_time=200):
    """
    向终端发送字符串，然后等待一段时间
    wait_time: 命令执行后，等待的时间，单位毫秒
    """
    xsh.Screen.Send(msg + "\r")
    sleep(wait_time)


def input_passwd(passwd: str):
    """
    输入密码
    根据终端当前是否有输入密码的提示选择性的输入
    """
    if wait("yes/no", 1):
        send("yes")

    if wait("password", 1):
        send(passwd)


def su_root(passwd: str):
    """
    切换到root用户
    """
    send("su root")
    input_passwd(passwd)


def ssh(user: str, passwd: str, host: str, port=22):
    """
    ssh自动登录(不能在本地shell中执行)
    """
    send("ssh {}@{} -p {}".format(user, host, port), 1000)
    input_passwd(passwd)


def ssh_in_local_shell(user: str, passwd: str, host: str, port=22):
    """
    在本地shell中ssh自动登录
    """
    send("ssh {}:{}@{}:{}".format(user, passwd, host, port), 1000)
    if wait("yes/no", 1):
        send("yes")


def open_session(user: str, passwd: str, host: str, port=22):
    """
    打开一个会话，但不会切换到这个会话，后续命令不会在这个新的会话中执行；
    如果当前会话是本地shell，那么将切换到打开的会话中，后续命令也会在这个当前会话中执行；
    """
    xsh.Session.Open("ssh://{}:{}@{}:{}".format(user, passwd, host, port))
    xsh.Screen.Synchronous = True
    sleep(1000)


def scp_in_local_shell(src: str, dst: str, user: str, passwd: str, host: str, port=22, mode=0):
    """
    在本地shell中执行scp自动拷贝文件
    mode=0: 从远端主机拷贝文件到本地
    mode=1: 拷贝本地文件到远端主机
    """
    src = src.replace("\\", "/")
    dst = dst.replace("\\", "/")
    if mode == 0:
        send("scp -P {} {}:{}@{}:{} {}".format(port, user, passwd, host, src, dst), 1000)
    else:
        send("scp -P {} {} {}:{}@{}:{}".format(port, src, user, passwd, host, dst), 1000)
    if wait("yes/no", 1):
        send("yes")
    if wait(src.split("/")[-1], 1):
        wait_no(src.split("/")[-1])


def scp(src: str, dst: str, user: str, passwd: str, host: str, port=22, mode=0):
    """
    使用scp复制文件(不能在本地shell中执行)
    mode=0: 从远端主机拷贝文件到当前设备
    mode=1: 拷贝当前设备的文件到远端主机
    """
    src = src.replace("\\", "/")
    dst = dst.replace("\\", "/")
    if mode == 0:
        send("scp -P {} {}@{}:{} {}".format(port, user, host, src, dst), 1000)
    else:
        send("scp -P {} {} {}@{}:{}".format(port, src, user, host, dst), 1000)
    input_passwd(passwd)
    if wait(src.split("/")[-1], 1):
        wait_no(src.split("/")[-1])


def set_screen_sync(sync=True):
    """
    设置屏幕是否同步
    """
    xsh.Screen.Synchronous = sync
    sleep(1000)
