
from enum import Enum


class ItemType(Enum):
    Weapon = 0
    Aromr = 1
    Consumables = 2


class Item(object):

    def __init__(
        self,
        _name: str,
        _itemtype: ItemType,
        _desc: str,
        _price,
        _sellprice
    ):
        self.Name = _name
        self.itemType = _itemtype
        self.Desc = _desc
        self.Price = _price
        self.SellPrice = _sellprice
