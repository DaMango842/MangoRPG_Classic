from MangoRPG.enumerates import *

# class QuestType(Enum):
#     none = 0
#     Normal = 1
#     Challenge = 2
#     Special = 3
#     #CleanEnemy = 4

class QuestProgress(Enum):
    Locked = 1
    UnLocked = 2
    InProgress = 3
    Complete = 4
    TaskEnd = 5

class QuestReward(Enum):
    none = 0
    moneyExp = 1
    item = 2
    mExpItem = 3
    skill = 4
    