import time
from rich.text import Text
from rich.console import Console
from rich.console import Group
from rich.panel import Panel
from rich.table import Table
from MangoRPG.items import Item
from MangoRPG.enumerates.ItemType import ItemType
from MangoRPG.character.player import *

console = Console()


class Inventory():

    def __init__(self, size: int = 10):
        self.__inventory = []
        self.__size = size
        pass

    def addItem(self, item: Item):
        if (len(self.__inventory) < self.__size):
            self.__inventory.append(item)

    def useItem(self, item: Item):
        if item in self.__inventory:
            if (item.type == ItemType.Consumable):
                if (item.amount >= 1):
                    print("使用成功!")
                else:
                    print("使用失败!")
            else:
                print("错误:使用的物品非消耗品或永久使用的道具!")        
        else:
            print("背包不存在该道具")      

    def equipItem(self, who, item:Item):
        if item in self.__inventory:
            if (item.type == ItemType.Weapon):
                who.currWeapon.append(item.name)
                who.HpMax += item.Hp
                who.ManaMax += item.Mana
                who.Atk += item.Atk
                who.Def += item.Def
                who.Matk += item.Matk
                who.Mdef += item.Mdef
                self.__inventory.remove(item)
            elif (item.type == ItemType.Armor):
                who.currArmor.append(item.name)
                who.HpMax += item.Hp
                who.ManaMax += item.Mana
                who.Atk += item.Atk
                who.Def += item.Def
                who.Matk += item.Matk
                who.Mdef += item.Mdef
                self.__inventory.remove(item)
            else:
                console.print("错误: 该物品不是装备类型")
        else:
            console.print("该物品不存在!")
        time.sleep(5)    

    def unequipItem(self, who, item:Item):
        if item in who.currWeapon:
            who.currWeapon.remove(item.name)
            who.HpMax -= item.Hp
            who.ManaMax -= item.Mana
            who.Atk -= item.Atk
            who.Def -= item.Def
            who.Matk -= item.Matk
            who.Mdef -= item.Mdef
            self.__inventory.append(item)
        elif item in who.currArmor:
            who.currArmor.remove(item.name)
            who.HpMax -= item.Hp
            who.ManaMax -= item.Mana
            who.Atk -= item.Atk
            who.Def -= item.Def
            who.Matk -= item.Matk
            who.Mdef -= item.Mdef
            self.__inventory.append(item)
        else:
            print("不合法的装备!")

    def showInventory(self,who):
        console.clear(True)
        InvTable = Table()
        InvTable.add_column("ID", header_style="#ffffff",
                            style="#ffffff", justify="center")
        InvTable.add_column("名称", header_style="#ffffff",
                            style="#ffffff", justify="center")
        InvTable.add_column("介绍", header_style="#ffffff",
                            style="#ffffff", justify="center")
        InvTable.add_column("数量", header_style="#ffffff",
                            style="#ffffff", justify="center")
        #InvTable.add_column("装备类型",header_style="#ffffff",justify="center")
        if (len(self.__inventory) > 0):
            for item in self.__inventory:
                InvTable.add_row(f"{item.id}", f"{item.name}",
                                 f"{item.desc}", f"{item.amount}")
              
                
        itemPanelText = Text()
        if (ItemType.Consumable):
            itemPanelText.append("[使用物品] ")
        elif (ItemType.Weapon or ItemType.Armor):
            itemPanelText.append("[装备物品] ")
        else:
            itemPanelText.append("[使用物品] ")
        itemPanelText.append("[查看物品] ")
        itemPanelText.append("[丢弃物品]")
        hasItemGroup = Group(
            InvTable,
            itemPanelText
        )
        noItemGroup = Group(
            Text("背包里面是空的", justify="center")
        )
        hasItemPanel = Panel(hasItemGroup, title="背包", subtitle=None)
        NoItemPanel = Panel(noItemGroup, title="背包", subtitle=None)
        if (len(self.__inventory) > 0):
            console.print(hasItemPanel)
        else:
            console.print(NoItemPanel)
        ainv = input("> 选择输入的命令")
        if (ainv in ['装备物品', '装备', 'Equip', 'equip', 'EQUIP']):
            print("暂未开放")
            #inputEquip = input("输入装备名称")
            #self.equipItem(who,inputEquip)
        elif (ainv in ['卸下物品', "卸下", 'unEquip', 'equip']):
            print("暂未开放")
            # inputEquip = input("输入装备名称")
            # self.unequipItem(inputEquip)
        elif (ainv in ['查看物品','查看','check','Check','CHECK']):
            inputCheck = input("查看哪个物品?")
            self.checkItemStat(inputCheck)
        elif (ainv in ['使用物品', '使用', 'Use', 'use', 'USE']):
            print("暂未开放")
            # inputItem = input("输入物品名称")
            # self.useItem()
        elif (ainv in ['丢弃物品', '丢弃', 'Drop', 'drop', 'DROP']):
            print("暂未开放")
            # inputItem = input("输入物品名称")
            # self.dropItem()
        console.clear(True)
        return
    @classmethod
    def checkItemStat(self, item: Item):
        try:
            console.clear()
            print(f"---------{item.name}--------")
            if (ItemType.Weapon):
                print(f"物品类型: 武器")
            elif (ItemType.Armor):
                print(f"物品类型: 装备")
            elif (ItemType.Consumable):
                print(f"物品类型: 消耗品")
            else:
                print(f"物品类型: 其他")
            print(f"物品介绍: {item.desc}")
            print("---------物品属性---------")
            print(f"装备等级: {item.Lv}")
            print(f"生命: {item.Hp}")
            print(f"Mana: {item.Mana}")
            print(f"攻击: {item.Atk}")
            print(f"防御: {item.Def}")
            print(f"魔攻: {item.Matk}")
            print(f"魔防: {item.Mdef}")
            print("-------------------------")
            print(f"价格: {item.price}")
        except:
            print("不是一个物品!")   
        time.sleep(5)
             
