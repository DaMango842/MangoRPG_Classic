#from MangoRPG.character.player import *
from MangoRPG.items.weaponList import *
from MangoRPG.items.armorList import *
from MangoRPG.items.itemList import *
from MangoRPG.shop import *
from MangoRPG.exception import *

class SellShop(Shop):
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

    # def sell(self, item:Item,who):
    #     if (item in who.Inventory.__inventory):
    #         who.Money += item.price
    #         who.Inventory.__inventory.remove(item)
    #         self.itemAmount += 1
    #     else:
    #         print("所指定的物品不合法!")    
                    

    def Open(self, who):
        if (len(self.__shopList) > 0):
            shopListTable = Table()
            shopListTable.add_column("物品名称",header_style="#ffffff",style="#10afff",justify="center")
            shopListTable.add_column("物品介绍",header_style="#ffffff",style="#10afff",justify="center")
            #shopListTable.add_column("数量",header_style="#ffffff",style="#10afff",justify="center")
            shopListTable.add_column("价格",header_style="#ffffff",style="#10afff",justify="center")
            if (self.itemAmount >= 1):
                shopListTable.add_column("库存",header_style="#ffffff",style="#af5f7f",justify="center")
            else:
                shopListTable.add_column("库存",header_style="#ffffff",style="#ff0000",justify="center")    
            for item in self.__shopList:
                shopListTable.add_row(f"{item.name}",f"{item.desc}",f"{item.sellPrice}",f"{self.itemAmount}")        
            #BuyShopPanel = Panel(shopListTable, title="购买商店")
            console.print(Panel(shopListTable, title="购买商店"),justify="center")
        else:
            raise GameError("不合法的商店")
        input("出售物品?")
