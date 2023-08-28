from items import Item

class Consumable(Item):
    
    def __init__(self, _name, _desc, _price, _sellprice,_hp,_mana):
        super().__init__(_name, _desc, _price, _sellprice)
        self.Hp = _hp
        self.Mana = _mana