# 本身不需要character类
# 所以import暂时没必要...(除了物品)
# from src.character import *
from MangoRPG.items import *

class Enemy():
    
    def __init__(
        self,
        _name,
        _lv,
        _hp,
        _HpMax,
        _atk,
        _def,
        _money,
        _exp
    ):
        self.Name = _name
        self.Lv = _lv
        self.Hp = _hp
        self.HpMax = _HpMax
        self.Atk = _atk
        self.Def = _def
        self.Money = _money
        self.Exp = _exp
        self.dropItem = []
