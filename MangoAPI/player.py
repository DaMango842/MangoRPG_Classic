# 玩家类

class Player(object):

    def __init__(
        self,
        _name,
        _lv,
        _hp, _hpmax,
        _mana, _manamax,
        _atk, _def, _matk, _mdef,
        _money, _exp,
        _nextexp
    ):
        self.Name = _name
        self.Lv = _lv
        self.Hp = _hp
        self.HpMax = _hpmax
        self.Mana = _mana
        self.ManaMax = _manamax
        self.Atk = _atk
        self.Def = _def
        self.Matk = _matk
        self.Mdef = _mdef
        self.Money = _money
        self.Exp = _exp
        self.NextExp = _nextexp
        
    
        
