from MangoRPG.exception import *

from rich import print
from rich.bar import Bar
from rich.console import Console
from rich.style import Style
from time import sleep

console = Console()


class Dialogue():
    def __init__(
        self,
        name: str | None,
        text: str,
        speed: float
    ):
        if name != "":
            print(f"{name}: ")
        else:
            pass
        if text == "":
            raise TextError("内容不能为空!")
        for char in text:
            print(char, end="")
            sleep(speed)
        # console.print(end="\n")


class DialogueRich():
    # 对话系统的增强版
    # 使用rich模块修改当前的Dialogue函数
    # 使用方法:
    # System.DialogueRich("test","Hello,world",None,None,0.12)
    # name为当前对话的'角色'名称
    # text为当前对话的文本
    # nameStyle为当前对话'角色'名称的样式(如果名字为空,则nameStyle也为空)
    # textStyle为当前对话文本的样式
    # speed为当前文本中每一个字的速度
    def __init__(
        self,
        name: str | None,
        text: str,
        nameStyle: str | Style | None,
        textStyle: str | Style | None,
        speed: float
    ):
        if name != "":
            console.print(f"{name}", end="", style=nameStyle)
            console.print(": ", end="")
        else:
            pass
        if text == "":
            raise TextError("内容不能为空!")
        for char in text:
            console.print(f"{char}", end="", style=textStyle)
            sleep(speed)
        console.print(end="\n")

class DialogueLog():
    # 对话系统,但带日志
    # 使用方法:
    # System.DialogueRich("test","Hello,world",None,None,0.12)
    # name为当前对话的'角色'名称
    # text为当前对话的文本
    # nameStyle为当前对话'角色'名称的样式(如果名字为空,则nameStyle也为空)
    # textStyle为当前对话文本的样式
    # speed为当前文本中每一个字的速度
    def __init__(
        self,
        text: str,
        textStyle: str | Style | None,
        speed: float
    ):
        if text == "":
            raise TextError("内容不能为空!")
        #for char in text:
        console.log(f"{text}", style=textStyle)
        sleep(speed)
