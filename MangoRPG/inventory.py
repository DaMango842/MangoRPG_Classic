from MangoRPG.items import Item
from MangoRPG.items import ItemType

from rich import print

class Inventory():

    def __init__(self,size:int=10):
        self.__inventory = []
        self.__size = size
        pass


    def addItem(self,item:Item):
        if (len(self.__inventory) < self.__size):
            self.__inventory.append(item)

    def showInventory(self):
        print("--------------------背包--------------------")
        print("")
        if (len(self.__inventory) > 0):
            for item in self.__inventory:
                print(f"{item.id} : {item.name} *{item.amount} | {item.desc}")
        else:
            print("背包里面是空的")        
        print("")
        print("--------------------------------------------")
        print("[1|N]查看物品 [2|B]使用物品 [3|K]装备物品 [4|M]丢弃物品")
        input("")

        return

    def checkItemStat(self,item:Item):
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
