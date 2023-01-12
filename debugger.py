##################################################################
#                     Mango RPG(Debugger)
# 关于debugger.py
# 该文件用于B类调试内容
# 测试相关的东西
# 见谅
##################################################################
from src.gui import Gui
from src.system import System
from src.dialogue import DialogueRich
from src.item import *
from src.game import Game
from src.quest.questSystem import *
from src.preload import preload
import os
from pygame import mixer
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from rich.traceback import install
install(show_locals=True)
#调试变量(请勿删除)
DEBUGGER = True
#主程序
def main_debug():
    if DEBUGGER == True:
        Game.TitleLogo_Debug()
    else:
        Game.TitleLogo()    
    #模仿游戏加载进度速度
    preload()

    System.Sleep(2.5)
    #System.Clear()
    #DialogueRich("Mango","","#ff1500","#ffffff",0.15)
    #System.DialogueRich("Mango","test","#ff1500","#ffffff",0.15)
    #mixer.init()
    #Game.Title()
    return
#运行主程序    
if __name__ == '__main__':
    main_debug()