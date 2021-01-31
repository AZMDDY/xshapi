"""
可以通过以下接口来操作Xshell的终端屏幕。包括显示对话框，获取对话框中的用户输入。
"""


def MsgBox(lpszMsg: str):
    """
    打开一个消息框
    :param lpszMsg: 消息框中显示的消息
    :return 消息的长度
    """
    print("xsh.Dialog.MsgBox({})".format(lpszMsg))
    return len(lpszMsg)


def Prompt(lpszMessage: str, lpszTitle: str, lpszDefault: str, bHidden: bool):
    """
    从提示对话框中返回用户的输入
    :param lpszMessage: 在提示对话框中显示的字符串
    :param lpszTitle: 提示对话框的标题
    :param lpszDefault: 提示对话框中输入栏中的初始默认字符串
    :param bHidden: 输入是否被隐藏，例如，当输入密码时，设置为True，则显示为"***"
    :return: 用户输入到提示对话框中的内容
    """
    print("xsh.Dialog.Prompt({}, {}, {}, {})".format(lpszMessage, lpszTitle, lpszDefault, bHidden))


def MessageBox(lpszMessage: str, lpszTitle: str, nType: int):
    """
    显示指定类型的提示确认对话框，返回点击的按钮对应的值
    :param lpszMessage: 在提示对话框中显示的字符串
    :param lpszTitle: 提示对话框的标题
    :param nType: 确认对话框的类型[0: OK, 1: OK/Cancel, 2: Abort/Retry/Ignore, 3: Yes/No/Cancel, 4: Yes/No,
     5: Retry/Cancel, 6: Cancel/TryAgain/Continue]
    :return: [1: OK, 2: Cancel, 3: Abort, 4: Retry, 5: Ignore, 6: Yes, 7: No, 10: TryAgain, 11: Continue]
    """
    print("xsh.Dialog.MessageBox({}, {}, {})".format(lpszMessage, lpszTitle, nType))
    return 0
