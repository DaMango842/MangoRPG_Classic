import pygame
import sys
import os

from rich.console import Console
from rich.traceback import install
install(show_locals=True)
console = Console()

def setConsoleMainTitle(_text:str):
    os.system("title " + _text)


def main():

    pygame.mixer.init()
    
    setConsoleMainTitle("Mango RPG Python Ver 0.1")
    
    print("Welcome Mango RPG!")




if __name__ == '__main__':
    main()