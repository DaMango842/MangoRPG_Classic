# 本身不需要character类
# 所以import暂时没必要...(除了物品)
# from src.character import *
from MangoRPG.items.weaponList import *
from MangoRPG.items.armorList import *
from MangoRPG.items.itemList import *


class Enemy(object):

    def __init__(
        self,
        _name,
        _lv,
        _hp,
        _HpMax,
        _atk,
        _def,
        _money,
        _exp,
        dropItem: Item | None,
        isBoss: bool
    ):
        self.Name = _name
        self.Lv = _lv
        self.Hp = _hp
        self.HpMax = _HpMax
        self.Atk = _atk
        self.Def = _def
        self.Money = _money
        self.Exp = _exp
        self.dropItem = dropItem
        # 是否为boss
        self.isBoss: isBoss
