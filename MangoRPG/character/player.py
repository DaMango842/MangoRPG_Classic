import sys
import random
import numpy as np

from MangoRPG.character import *
from MangoRPG.inventory import Inventory
from MangoRPG.quest.questSystem import QuestSystem


class Player(object):
    # 定义方法:
    # player = Player("Player Name",1,100,100,0,0,10,10,0,0,10)
    def __init__(
        self,
        _name: str,
        _career: str | None = "",
        _lv: int = 0,
        _hp: float = 0,
        _hpMax: float = 0,
        _mana: float = 0,
        _manaMax: float = 0,
        _atk: int = 0,
        _def: int = 0,
        _matk: int = 0,
        _mdef: int = 0,
        _money: int = 0,
        _exp: int = 0,
        _nextExp: int = 0
    ):
        self.Name = _name
        self.Lv = _lv
        self.Hp = _hp
        self.HpMax = _hpMax
        self.Mana = _mana
        self.ManaMax = _manaMax
        self.Atk = _atk
        self.Def = _def
        self.Matk = _matk
        self.Mdef = _mdef
        self.Money = _money
        self.Exp = _exp
        self.nextExp = _nextExp
        # 职业
        self.career = _career
        # 身份
        # self.identity = ""
        self.defeatEnemies = 0
        # 初始化玩家背包
        self.Inventory = Inventory()
        # 初始化玩家的任务列表
        self.Quest = QuestSystem()
        # 当前武器(当里面为无,则无装备武器)
        self.currWeapon = "破旧木剑"
        # 当前防具(如果当前为无,则无装备防具)
        self.currArmor = "破旧衣服"

        self.trainerWon: bool = False
        self.isSeenPrologue: bool = False
        # 游戏结束开关
        self.gameOver: bool = False

    def setNewCareer(self, name):
        self.career = name
        return self.career

    # 使用方法:
    # player.playerStats()
    def playerStats(self):
        pStatsTable = Table()
        pStatsTable.add_column("名称", justify="center")
        pStatsTable.add_column("职业", justify="center")
        # pStatsTable.add_column("名称", justify="center")
        pStatsTable.add_column("等级", justify="center")
        pStatsTable.add_column("生命", justify="center")
        pStatsTable.add_column("Mana", justify="center")
        pStatsTable.add_column("攻击", justify="center")
        pStatsTable.add_column("防御", justify="center")
        pStatsTable.add_column("魔攻", justify="center")
        pStatsTable.add_column("魔防", justify="center")
        pStatsTable.add_column("金币", justify="center")
        pStatsTable.add_column("经验", justify="center")
        pStatsTable.add_row(
            f"{self.Name}",
            f"{self.career}",
            f"{self.Lv}",
            f"{self.Hp} / {self.HpMax}",
            f"{self.Mana} / {self.ManaMax}",
            f"{self.Atk}",
            f"{self.Def}",
            f"{self.Matk}",
            f"{self.Mdef}",
            f"{self.Money}",
            f"{self.Exp} / {self.nextExp}",
        )
        pStatsTable2 = Table()
        pStatsTable2.add_column("当前武器", justify="center")
        pStatsTable2.add_column("当前防具", justify="center")
        if len(self.currWeapon) >= 1 and len(self.currArmor) >= 1 and not "[]":
            for i,j in self.currWeapon,self.currArmor:
                pStatsTable2.add_row(
                    f"{self.currWeapon[i]}",
                    f"{self.currArmor[j]}"
                )
        else:
            pStatsTable2.add_row(
                "无",
                "无"
            )        
        console.print(Panel(pStatsTable, title="成员"), justify="center")
        console.print(Panel(pStatsTable2, title="成员装备"), justify="center")
        console.print(Panel(f"击败敌人数: {self.defeatEnemies}"), justify="center")
        input("> ")
    # 使用方法：
    # player.GameOver()
    def GameOver(self):
        console.clear()
        print("游戏结束!")
        input()
        sys.exit(1)
    # 使用方法:
    # player.levelUp()
    def levelUp(self):
        if (self.Exp >= self.nextExp):
            # 扣除当前经验值
            self.Exp -= self.nextExp
            # 增加等级
            self.Lv += 1
            # 增幅属性(血量上限,攻击,防御,魔攻,魔防)
            self.HpMax += (np.random.randint(1,100) - (self.Lv*4))
            if self.ManaMax != 0:
                self.ManaMax += (np.random.randint(1,50) * 2 - (self.Lv*4))
            self.Atk += (np.random.randint(1,15) * 2 - (self.Lv*2))
            self.Def += (np.random.randint(1,15) * 2 - (self.Lv*2))
            self.Matk += (np.random.randint(1,15) * 2 - (self.Lv*6))
            self.Mdef += (np.random.randint(1,15) * 2 - (self.Lv*6))
            # 计算下个等级所需经验
            self.nextExp *= (np.random.randint(1,10) - (self.Lv*2))
            print(f"恭喜升级!\n你现在的等级为Lv.{self.Lv}")
            self.Hp = self.HpMax
            if self.ManaMax != 0:
                self.Mana = self.ManaMax
            else:
                pass    
            if self.Matk < 0:
                self.Matk = 0
            if self.Mdef < 0:
                self.Mdef = 0    
            print(f"下个等级所需经验: {self.nextExp - self.Exp}")
        else:
            print(f"下个等级所需经验: {self.nextExp - self.Exp}")
        input()
    # 使用方法:
    # player.enterPlayerName()
    def enterPlayerName():
        # 在这行中,你必须输入你的玩家名
        Name = input("-> ")
        # 这里进行名字判定,如果为空,则使用固定名称
        # 否则则是你输入的名称
        if Name != "":
            name = Name
        else:
            name = "Mango"
        # 在这个位置修改除了name之外的参数
        # 不能修改name这个值(因为name = 你输入的名字)
        return Player(name, "无", 1, 100, 100, 0, 0, 10, 10, 0, 0, 200, 0, 10)
    # 使用方法:
    # player.openInventory()
    def openInventory(self,who):
        self.Inventory.showInventory(who)
        return
    # 使用方法:
    # player.openQuestMenu()
    def openQuestMenu(self):
        self.Quest.showQuestList()
        return
    # 使用方法:
    # player.saveGame() #需要创建变量 = Player()
    def saveGame(self):
        s = self.Name+'\n'+str(self.Lv)+'\n'
        s += str(self.Hp)+'\n'+str(self.HpMax)+'\n' + \
            str(self.Mana)+'\n'+str(self.ManaMax)+'\n'
        s += str(self.Atk)+'\n'+str(self.Def)+'\n' + \
            str(self.Matk)+'\n'+str(self.Mdef)+'\n'
        s += str(self.Money)+'\n'+str(self.Exp)+'\n'+str(self.nextExp)+'\n'
        s += str(self.currWeapon)+'\n'+str(self.currArmor)+'\n'
        s += str(self.career)+'\n'+str(0)+'\n'+str(0)+'\n'
        s += str(self.defeatEnemies)+'\n'
        s += str(self.trainerWon)+'\n'
        s += str(self.isSeenPrologue)
        with open('player.save', 'w', encoding="utf-8") as f:
            f.write(s)

        print("存档已记录完成!")
    def test():
        pass
