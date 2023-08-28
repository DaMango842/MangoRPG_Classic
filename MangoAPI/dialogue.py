
import time
from rich.console import Console
from rich.style import Style

console = Console()


class Dialogue():
    
      def __init__(
        self,
        name: str | None,
        text: str,
        nameStyle: str | Style | None,
        textStyle: str | Style | None,
        speed: float
    ):
        if name != "":
            console.print(f"{name}", end="", style=nameStyle)
            console.print(": ", end="")
        else:
            pass
        if text == "":
            return
        for char in text:
            console.print(f"{char}", end="", style=textStyle)
            time.sleep(speed)
        console.print(end="\n")
            

