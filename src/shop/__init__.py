
from src.inventory import *
from src.item import *
from src.exception import *
from src.character.player import *

from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.traceback import install
from rich.console import Console
from rich.console import Group
install(show_locals=True)
console = Console()
