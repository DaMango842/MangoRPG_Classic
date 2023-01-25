from MangoRPG.items.weaponList import *
from MangoRPG.items.armorList import *
from MangoRPG.items.itemList import *
from MangoRPG.character.player import Player
from MangoRPG.shop import *
from MangoRPG.exception import *

class BuyShop(Shop):
    def __init__(self):
        self.__shopList = [
            Old_WoodenSword,
            Old_LeatherClothes
        ]
        self.itemAmount = 0

    def add(self, item: Item):
        self.__shopList.append(item)
        if (item.amount >= 1):
            self.itemAmount += 1

    def remove(self, item: Item):
        self.__shopList.remove(item)
        if (item.amount >= 0):
            self.itemAmount -= 1

    def buyItem(self,who:Player,item:Item):
        if item in self.__shopList and item.amount >= 1:
            if len(who.Inventory.__inventory) > len(who.Inventory.__size):
                print("无法购买物品: 背包已满!")
            else:
                who.Inventory.addItem(item)
                item.amount -= 1
                print(f"已购买{item.name}")
        else:
            print("无法购买物品! 商店已售完或者未补货")            



    def Open(self, who):
        if (len(self.__shopList) > 0):
            shopListTable = Table()
            shopListTable.add_column("物品名称",header_style="#ffffff",style="#10afff",justify="center")
            shopListTable.add_column("物品介绍",header_style="#ffffff",style="#10afff",justify="center")
            shopListTable.add_column("数量",header_style="#ffffff",style="#10afff",justify="center")
            shopListTable.add_column("价格",header_style="#ffffff",style="#10afff",justify="center")
            if (self.itemAmount >= 1):
                shopListTable.add_column("库存",header_style="#ffffff",style="#af5f7f",justify="center")
            else:
                shopListTable.add_column("库存",header_style="#ffffff",style="#ff0000",justify="center")    
            for item in self.__shopList:
                shopListTable.add_row(f"{item.name}",f"{item.desc}",f"{item.amount}",f"{item.price}",f"{self.itemAmount}")        
            #BuyShopPanel = Panel(shopListTable, title="购买商店")
            console.print(Panel(shopListTable, title="购买商店"),justify="center")
        else:
            raise GameError("不合法的商店")
        input("购买物品?")