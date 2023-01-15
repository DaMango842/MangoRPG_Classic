from enum import Enum

class ItemType(Enum):
    Weapon = 1
    Armor = 2
    Consumable = 3
    Other = 4

class Item():
    #定义物品
    #@property
    def __init__(
        self,
        id:int,
        name:str,
        type:ItemType,
        desc:str,
        price:int,
        sellPrice:int,
        Lv:int,
        Hp:int,
        Mana:int,
        Atk:int,
        Def:int,
        Matk:int,
        Mdef:int,
        amount:int
        ):
        self.id = id
        self.name = name
        self.type = type
        self.desc = desc
        self.price = price
        self.sellPrice = sellPrice
        self.Lv = Lv
        self.Hp = Hp
        self.Mana = Mana
        self.Atk = Atk
        self.Def = Def
        self.Matk = Matk
        self.Mdef = Mdef
        self.amount = amount

#在这里编写道具,因为我实在不懂python里的json,所以抱歉
#格式:
#ItemName = Item(0,"",1,"",0,0,0,0,0,0,0)
Old_Wooden_Sword = Item(1,"破旧的木剑",1,"一把很破旧的木剑",10,5,1,0,0,2,0,0,0,1)
Old_Leather_Clothes = Item(2,"破旧皮衣",2,"普通农民才会穿的衣服...",5,2,1,2,0,0,2,0,0,1)


Test_Item = Item(999,"测试物品",4,"就只是用来测试的",0,1,1,0,0,0,0,0,0,1)



#在这里把写好的道具放进物品列表里
itemList = [
    Old_Wooden_Sword,
    Old_Leather_Clothes
]
