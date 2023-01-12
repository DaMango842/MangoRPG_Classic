#<------------我只是个占位符------------>
from src.gui import Gui
from src.system import System
from src.item import *
from src.game import Game
#导入的模块
import os
from pygame import mixer
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from rich.traceback import install
install(show_locals=True)

# will be updated python 3.11 soon

def main():   
    #player = Player("test",1,100,100,0,0,10,10,0,0,10)
    #加载Logo?
    Game.TitleLogo()
    #模仿游戏加载进度速度
    System.Sleep(5.5)
    System.Clear()
    #pygame音频初始化
    mixer.init()
    #游戏标题界面
    Game.Title()

    return
if __name__ == '__main__':

    main()