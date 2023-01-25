from MangoRPG.exception import *

from rich.console import Console
from rich.console import Group
from rich.text import Text
from rich.table import Table
from rich.panel import Panel
from rich.traceback import install
console=Console()
install(show_locals=True)

class Map(object):
    def __init__(self):
        pass