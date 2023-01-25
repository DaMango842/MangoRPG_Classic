#from MangoRPG.exception import *
#from MangoRPG.battle import *

from rich.console import Console
from rich.console import Group
from rich.text import Text
from rich.table import Table
from rich.panel import Panel
from rich.traceback import install
console = Console()
install(show_locals=True)


class Room():
    # 房间名称,北部,南部,西部,东部,遇敌步数
    def __init__(
        self,
        name:str,
        north:str|None,
        south:str|None,
        west:str|None,
        east:str|None,
        step:int|None
    ):
        self.name = name
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.step = step

    def enterRoom(self,name):
        self.name = name
        return self.name


MangoRoom = Room(
    "Mango的房间",
    "",
    "",
    "",
    "",
    None
)

MangoHallway = Room(
    "Mango家走廊",
    "Mango房间",
    "",
    "",
    "",
    None
)



