from items import Item

class Weapon(Item):
    
    def __init__(self, _name, _desc, _price, _sellprice,_hpmax,_manamax,_atk,_def,_matk,_mdef):
        super().__init__(_name, _desc, _price, _sellprice)
        self.HpMax = _hpmax
        self.ManaMax = _manamax
        self.Atk = _atk
        self.Def = _def
        self.Matk = _matk
        self.Mdef = _mdef
        