from MangoRPG.items.weaponList import *
from MangoRPG.items.armorList import *
from MangoRPG.items.itemList import *

from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.traceback import install
from rich.console import Console
from rich.console import Group
install(show_locals=True)
console = Console()


class Shop:
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