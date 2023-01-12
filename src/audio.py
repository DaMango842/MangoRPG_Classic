import os
import sys

from pygame import mixer
#音频处理
class Audio():

    def __init__(self) -> None:
        pass

    def playMusic(filename,volume):
        mixer.music.load(filename)
        mixer.music.set_volume(volume)
        mixer.music.play()

    def playSound(filename,volume):
        mixer.Sound.play(filename)
        mixer.Sound.set_volume(volume)