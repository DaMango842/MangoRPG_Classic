
import os
import sys
import time
import cmd
import textwrap
from enum import Enum
from pygame import mixer
from rich.console import Console
from rich.traceback import install
install(show_locals=True)


#
from storys.storyPrologue import Prologue
from src.character.player import *
from src.version import *
from src.exception import *
from src.dialogue import Dialogue
from src.dialogue import DialogueRich
from battle import *



console = Console()

class StartType(Enum):
    START = 1
    LOAD = 2

class Game():
    def __init__(self):
        pass

    # 用法:
    # Game.TitleLogo()
    def TitleLogo(): 
        # ---------------------------------------------
        # -         Mango RPG(0.1.0 Alpha)            -
        # -     (C) 2022 ~ 2023 黑夜下的糖果酱         -
        # ---------------------------------------------
        System.Write(" ")
        console.print(f"Mango RPG({versionStr})",end="",style="#ffffff",justify="center")
        console.print(f"(C) 2022 ~ 2023 黑夜下的糖果酱",end="",justify="center")
        System.Write(" ")

    def TitleLogo_Debug():
        print(" ----------------------------- ")
        print(" -      Mango RPG(Debug)     - ")
        print(" (C) 2022 ~ 2023 黑夜下的糖果酱 ")
        print(" ----------------------------- ")
    
    title:str = "Mango RPG"
    version:str = versionStr
    isPrologueSeen:bool = False

    # 用法:
    # Game.Title()            
    def Title():
        System.Clear()
        System.Write(" ")
        for prefix in range(0,57):
            System.Write("-")
            prefix += 1
        System.Write("\n")    
        print(f" -                {Game.title}({Game.version})                 - ")
        print("             (C) 2022 - 2023 黑夜下的糖果酱                    ")
        System.Write(" ")
        for middle in range(0,57):
            System.Write("-")
            middle += 1 
        print("                                                          ")
        print("      [S]Start     [L]Load    [N]Settings     [Q]Exit        ")
        print("                                                          ")
        System.Write(" ")
        for suffix in range(0,57):
            System.Write("-")
            suffix += 1    
        print("")
        System.Write("\n")
        option = input("-> ")
        while (True):
            if option in ['start','Start','START']:
                Game.Start("start")
            elif option in ['load','Load','LOAD']:
                Game.Start("load")
            elif option in ['setting','Setting','SETTING']:
                print("设置未在这个版本上启用! \n")
                input("> ")
                Game.Title()
            elif option in ['exit','Exit','EXIT','quit','Quit','QUIT']:
                System.Exit(0)
            else:
                print("请输入一个正确的命令")
                Game.Title()

    def Start(Type:str):
        if (Type in ['start','Start','START']):
            global player
            System.Clear()
            Game.Start("playing")
            pass
        elif (Type in ['load','Load','LOAD']):
            global player
            if (os.path.exists('player.save')):
                try:
                    with open('player.save','r',encoding='utf-8') as f:
                        data=f.read().split('\n')
                    player=Player(data[0])
                    player.Lv=int(data[1])
                    player.Hp=int(data[2])
                    player.HpMax=int(data[3])
                    player.Mana=int(data[4])
                    player.ManaMax=int(data[5])
                    player.Atk=int(data[6])
                    player.Def=int(data[7])
                    player.Matk=int(data[8])
                    player.Mdef=int(data[9])
                    player.Money=int(data[10])
                    player.Exp=int(data[11])
                    player.nextExp=int(data[12])
                    player.currWeapon[1]=str(data[13])
                    player.currArmor[3]=str(data[14])
                    Game.isPrologueSeen = True
                    print("读取存档成功!")
                    input("> ")
                    Game.Start("playing")
                    pass
                except Exception as e:
                    raise GameError(f"错误:读取存档时出错!   {e}")
                  
            if player.Name == "":
                Dialogue("","输入你的新名字",0.25)
                player=Player.enterPlayerName()
            else:
                pass

        elif (Type in ['playing','Playing','PLAYING']):
            if(Game.isPrologueSeen == False):
                Prologue()
                Game.isPrologueSeen = True
                player = Player("",0,1,1,0,0,0,0,0,0,0,0,10)    
            if(player.Name == ""):
                Dialogue("","输入你的新名字",0.25)
                player=Player.enterPlayerName()
            else:
                pass

            while(player.gameOver != True):
                System.Clear()
                if (player.Hp <= 0):
                    player.gameOver = True
                    player.GameOver()
                    return
                print("------ 菜单 ------")
                print(" [C]探索 ")
                print(" [M]商店 ")
                print("--(B)状态--(I)背包--(S)保存--(P)任务--(Q)退出--")
                option = input("-> ")
                if option in ['探索','c','C']:
                    print("由于某些原因,探索暂不开放")
                    #战斗系统维修中
                    print("但你可以游玩战斗部分")
                    Battle.startBattle(player)
                elif option in ['副本','f','F']:
                    pass
                elif option in ['任务','p','P','quest','Quest','QUEST']:
                    pass
                elif option in ['背包','i','I','inventory','Inventory','INVENTORY']:
                    player.openInventory()
                elif option in ['状态','b','B','stats','Stats','STATS']:
                    player.playerStats()
                elif option in ['保存','s','S','save','Save','SAVE']:
                    player.saveGame()
                elif option in ['商店','m','M','shop','Shop','SHOP']:
                    pass
                elif option in ['退出','q','Q','exit','Exit','EXIT','quit','Quit','QUIT']:
                    System.Exit(0)
                else:
                    print("请输入正确的命令")

            return       
        else:
            pass

              
        

        
        
        #player.inventory.addItem(Old_Wooden_Sword)
        #player.OpenInventory()

        #Battle.startBattle(player)

    def aboutMenu():
        print("")
        input("按任意键返回标题")
        Game.Title()


    def credits():
        print("")
        input()
        Game.Title()        



            
        

