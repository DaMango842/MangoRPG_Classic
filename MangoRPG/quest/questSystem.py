from MangoRPG.exception import *
from MangoRPG.quest import *


from rich.console import Console
from rich.console import Group
from rich.text import Text
from rich.table import Table
from rich.panel import Panel
from rich.traceback import install
console = Console()
install(show_locals=True)


class QuestSystem(Quest):

    def __init__(self):
        self.__questList = []

    def addQuest(self,quest:Quest):
        self.__questList.append(quest)

    def removeQuest(self,quest:Quest):
        for quest in self.__questList:
            self.__questList.remove(quest)          

    def showQuestList(self):
        questTable = Table()
        questTable.add_column("名称")
        questTable.add_column("介绍")
        questTable.add_column("进度")

        for quest in self.__questList:
            questTable.add_row(
                f"{quest.name}",
                f"{quest.desc}",
                f"{quest.progress}"
            )
        NoQuestText = Text("暂时没有任务")     
        if len(self.__questList):
            console.print(Panel(questTable,title="任务"))
        else:
            console.print(Panel(NoQuestText,title="任务"))            
