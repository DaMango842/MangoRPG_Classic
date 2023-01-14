from src.character import *


class Player():
    # 定义方法:
    # player = Player("Player Name",1,100,100,0,0,10,10,0,0,10)
    def __init__(
        self,
        _name: str,
        _lv: int=0,
        _hp: float=0,
        _hpMax: float=0,
        _mana: int=0,
        _manaMax: int=0,
        _atk: int=0,
        _def: int=0,
        _matk: int=0,
        _mdef: int=0,
        _money: int=0,
        _exp: int=0,
        _nextExp: int=0
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
        # 初始化玩家背包
        self.Inventory = Inventory()
        # 初始化玩家的任务列表
        self.Quest = QuestSystem()
        # 当前武器(当里面为无,则无装备武器)
        self.currWeapon = ["无", "无"]
        # 当前防具(如果当前为无,则无装备防具)
        self.currArmor = ["无", "无", "无", "无"]

        # self.teamList = [
            
        # ]

        self.gameOver: bool = False
    # 使用方法:
    # Player.playerStats()
    # player.playerStats()

    def playerStats(self):
        pStatsTable = Table()
        pStatsTable.add_column("名称", justify="center")
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
        console.print(Panel(pStatsTable,title="成员"), justify="center")
        input("> ")
    # 使用方法：
    # Player.GameOver()
    # player.GameOver()

    def GameOver(self):
        System.Clear()
        print("游戏结束!")
        input()
        sys.exit(1)
        # if (self.Hp > 0):
        #     pass
        # else:
        #     System.Clear()
        #     print("游戏结束!")
        #     input()
        #     sys.exit(1)
    # 使用方法:
    # Player.levelUp() #需要放到战斗中判定或者在任务中判定
    # player.levelUp()

    def levelUp(self):
        if (self.Exp > self.nextExp):
            self.Exp -= self.nextExp
            self.nextExp *= random.randint(0, 10)
            print("恭喜升级!\n")
            print(f"下个等级所需经验: {self.nextExp}")
        else:
            print(f"下个等级所需经验: {self.nextExp}")
    # 使用方法:
    # Player.enterPlayerName()
    # player.enterPlayerName()

    def enterPlayerName():
        # 在这行中,你必须输入你的玩家名
        Name = input("-> ")
        # 这里进行名字判定,如果为空,则使用固定名称
        # 否则则是你输入的名称
        if (Name != ""):
            name = Name
        else:
            name = "Mango"
        # 在这个位置修改除了name之外的参数
        # 不能修改name这个值(因为name = 你输入的名字)
        return Player(name, 1, 100, 100, 0, 0, 10, 10, 0, 0, 0, 0, 10)
    # 使用方法:
    # Player.openInventory()
    # player.openInventory()

    def openInventory(self):
        self.Inventory.showInventory()
        return
    # 使用方法:
    # Player.saveGame()
    # player.saveGame() #需要创建变量 = Player()

    def saveGame(self):
        s = self.Name+'\n'+str(self.Lv)+'\n'
        s += str(self.Hp)+'\n'+str(self.HpMax)+'\n' + \
            str(self.Mana)+'\n'+str(self.ManaMax)+'\n'
        s += str(self.Atk)+'\n'+str(self.Def)+'\n' + \
            str(self.Matk)+'\n'+str(self.Mdef)+'\n'
        s += str(self.Money)+'\n'+str(self.Exp)+'\n'+str(self.nextExp)+'\n'
        s += str(self.currWeapon[1])+'\n'+str(self.currArmor[3])
        with open('player.save', 'w', encoding="utf-8") as f:
            f.write(s)
        print("存档已记录完成!")

    # def stats():
        # print("------------------------------------------")
        # print(f"名称: {self.Name}")
        # print(f"等级: {self.Lv}")
        # print("生命: %d / %d" % (self.Hp, self.HpMax))
        # print("Mana: %d / %d" % (self.Mana, self.ManaMax))
        # print("------------------------------------------")
        # print(f"攻击: {self.Atk}")
        # print(f"防御: {self.Def}")
        # print(f"魔攻: {self.Matk}")
        # print(f"魔防: {self.Mdef}")
        # print("------------------------------------------")
        # print(f"当前武器: {self.currWeapon[1]}")
        # print(f"当前装备: {self.currArmor[3]}")
        # print("------------------------------------------")
        # print(f"金钱: {self.Money}")
        # print("经验: %d / %d" % (self.Exp, self.nextExp))
        # print("------------------------------------------")
