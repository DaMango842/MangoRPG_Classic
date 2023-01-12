
import os
import sys
import time
import cmd
import textwrap

from rich import print
from rich.bar import Bar
from rich.console import Console
from rich.style import Style
#import typer.rich_utils

from enum import Enum

class ReturnEvent(Enum):
    Success = 0
    Failure = 1

console = Console()

class System():
    def __init__(self) -> None:
        pass       
    #用于替代原本的print导致在对话中逐字边逐行列表
    #用法: System.Write("Hello world!")
    def Write(text):
        sys.stdout.write(text)
    #
    def Update():
        sys.stdout.flush()

    #清除一次屏幕
    #用法:System.Clear()
    def Clear():
        os.system('cls')
    #等待几秒
    #用法: System.Sleep(1)
    def Sleep(count: float):
        time.sleep(count)
    #作用就是替代功能
    #用法: System.Exit()


    
    #关于对话类的东西已全部移动至dialogue文件夹
    # # 用法:
    # # System.Dialogue("test","Hello,world",0.25)
    # def Dialogue(name,text,speed):
    #     if name != "":
    #         System.Write(f"{name}: ")
    #     else:
    #         pass
    #     for char in text:
    #         System.Write(char)
    #         System.Sleep(speed) 
    # # 对话系统的增强版
    # # 使用rich模块修改当前的Dialogue函数
    # # 使用方法:
    # # System.DialogueRich("test","Hello,world",None,None,0.12)
    # # name为当前对话的'角色'名称
    # # text为当前对话的文本
    # # nameStyle为当前对话'角色'名称的样式
    # # textStyle为当前对话文本的样式
    # # speed为当前文本中每一个字的速度
    # def DialogueRich(
    #     name:str,
    #     text:str,
    #     nameStyle:str|Style|None,
    #     textStyle:str|Style|None,
    #     speed:float
    #     ):
    #     if name != "":
    #         console.print(
    #             f"{name}",
    #             end="",
    #             style=nameStyle
    #             )
    #         console.print(
    #             ": ",
    #             end=""
    #             )
    #     else:
    #         pass
    #     for char in text:
    #         console.print(
    #             f"{char}",
    #             end="",
    #             style=textStyle
    #             )
    #         System.Sleep(speed)   