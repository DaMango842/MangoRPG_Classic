from MangoRPG.enumerates import ItemType
from MangoRPG.meta.loadmetaData import loadItemMetaData

item = loadItemMetaData()


class Item():
    # 定义物品
    # @property
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
