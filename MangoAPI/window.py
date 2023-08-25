import pygame


class Window():
    
    def __init__(self,width,height,title:str|None = None,mflags = 0,depth = 0,display = 0,vsync = 0):
        self.width = width
        self.height = height
        self.title = title
        self.mflag = mflags
        self.depth = depth
        self.display = display
        self.vsync = vsync
        
        pygame.display.set_mode((width,height),mflags,depth,display,vsync)
        
        if not title:
            pass
        else:
            pygame.display.set_caption(title)
    
    def setWindowTitle(self,_title):
        self.title = _title
        pygame.display.set_caption(_title)
    
    def setWindowSize(self,width,height):
        pygame.display.set_mode((width,height))    