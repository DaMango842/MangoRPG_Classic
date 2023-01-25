#------------我只是个占位符------------
from MangoRPG.enumerates.QuestType import *
from MangoRPG.items.weaponList import *
from MangoRPG.items.armorList import *
from MangoRPG.items.itemList import *

class Quest(object):
    
    # 定义说明:
    # 定义时候可以不用'name='这些东西
    # 把测试任务和任务介绍测试还有物品获得的名称替换
    # Quest("测试任务",1,"任务介绍测试",0)
    def __init__(self,id:int,name:str,desc:str,progress:QuestProgress,money:int,exp:int,item:Item | None,Kcount:int|None,MaxKcount:int|None):
        self.id = id
        self.name = name
        self.desc = desc
        self.money = money
        self.exp = exp
        #self.attr = 0
        self.item = item
        self.count = Kcount
        self.Maxcount = MaxKcount
        self.progress = progress

Quest1 = Quest(1,"测试任务","任务介绍测试",1,100,10,TestItem,None,None)
Quest2 = Quest(2,"测试任务","任务介绍测试",1,100,10,TestItem,None,None)
QuestNoItem = Quest(200,"测试任务","任务介绍测试",1,100,10,None,None,None)


thisQuestList = [
    Quest1,
    Quest2
]
