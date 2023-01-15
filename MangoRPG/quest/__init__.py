from enum import Enum
#------------我只是个占位符------------
from MangoRPG.items import *

class QuestType(Enum):
    none = 0
    Normal = 1
    Challenge = 2
    Special = 3
    #CleanEnemy = 4

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
    
class Quest(object):
    
    # 定义说明:
    # 定义时候可以不用'name='这些东西
    # 把测试任务和任务介绍测试还有物品获得的名称替换
    # Quest("测试任务",1,"任务介绍测试",0)
    def __init__(self,id:int,name:str,type:QuestType,desc:str,progress:QuestProgress,money:int,exp:int,item:Item | None,Kcount:int|None,MaxKcount:int|None):
        self.id = id
        self.name = name
        self.type = type
        self.desc = desc
        self.money = money
        self.exp = exp
        #self.attr = 0
        self.item = item
        self.count = Kcount
        self.Maxcount = MaxKcount
        self.progress = progress

Quest1 = Quest(1,"测试任务",1,"任务介绍测试",1,100,10,Test_Item,None,None)
Quest2 = Quest(2,"测试任务",1,"任务介绍测试",1,100,10,Test_Item,None,None)
QuestNoItem = Quest(200,"测试任务",1,"任务介绍测试",1,100,10,None,None,None)


thisQuestList = [
    Quest1,
    Quest2
]
