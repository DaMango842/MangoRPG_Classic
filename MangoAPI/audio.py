import pygame


class Audio():
    
    def __init__():
        pygame.mixer.init()
    
    def playBGM(filename,vol:float=0.5):
        pygame.mixer.music.load(filename)
        pygame.mixer.music.set_volume(vol)
        pygame.mixer.music.play()
    
    def playSound(filename,vol:float=0.5):
        sound = pygame.mixer.Sound(filename)
        sound.set_volume(vol)    
        sound.play()