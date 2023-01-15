from MangoRPG.quest import *

class QuestSystem(Quest):

    def __init__(self,maxAmount:int=10):
        self.__lockedQuestList = []
        self.__unlockedQuestList = []
        self.__questList = []
        self.__questCompleteList = []
        self.maxQuestAmount = maxAmount  

    def showQuest(self):
        print("<--------------------  任务列表  -------------------->")
        print()
        #if (len(self.__questList) > 0):
        #    for 

        print()
        print("<--------------------------------------------------->")