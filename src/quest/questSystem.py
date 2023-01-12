

#------------我只是个占位符------------
from src.quest import *
from src.system import System


class QuestSystem(Quest):


    def __init__(self,maxAmount:int=10):
        self.__lockedQuestList = []
        self.__unlockedQuestList = []
        self.__questList = []
        self.__questCompleteList = []
        self.maxQuestAmount = maxAmount

    

            

    def showQuest(self):
        System.Clear()
        print("<--------------------  任务列表  -------------------->")
        print()
        #if (len(self.__questList) > 0):
        #    for 

        print()
        print("<--------------------------------------------------->")