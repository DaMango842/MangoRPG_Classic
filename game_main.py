import pygame
import sys
import os
import ctypes

from MangoAPI.window import *
from MangoAPI.audio import *
from constant import *

from rich.console import Console
from rich.traceback import install
install(show_locals=True)
console = Console()

pygame.init()
pygame.font.init()

ctypes.windll.shcore.SetProcessDpiAwareness(1)

def setConsoleMainTitle(_text: str):

    os.system("title " + _text)

    return

def changeTitle(_title):
    pygame.display.set_caption(_title)
    
# 主程序
def main():
    setConsoleMainTitle("Mango RPG Python Ver 0.1")
    print("Welcome Mango RPG!")
    
    screen = Window(WIDTH,HEIGHT,TITLE)
    clock = pygame.time.Clock()
    
    

    while True:    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()
        
          
        
        clock.tick(FPS)


if __name__ == '__main__':
    main()
