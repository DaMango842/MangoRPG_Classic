from enum import Enum

from MangoRPG.meta.loadmetaData import loadItemMetaData

class ItemType(Enum):
    Weapon = 1
    Armor = 2
    Consumable = 3
    Other = 4

item = loadItemMetaData()



class Item(object):
    # 定义物品
    # @property
    # @classmethod
    def __init__(
        self,
        id: int,
        name: str,
        type: ItemType,
        desc: str,
        price: int,
        sellPrice: int,
        Lv: int,
        Hp: int,
        Mana: int,
        Atk: int,
        Def: int,
        Matk: int,
        Mdef: int,
        amount: int
    ):
        self.id:int = id
        self.name:str = name
        self.type:ItemType = type
        self.desc:str = desc
        self.price:int = price
        self.sellPrice:int = sellPrice
        self.Lv:int = Lv
        self.Hp:int = Hp
        self.Mana:int = Mana
        self.Atk:int = Atk
        self.Def:int = Def
        self.Matk:int = Matk
        self.Mdef:int = Mdef
        self.amount:int = amount
    @property
    def itemtype(self):
        return self.type    
