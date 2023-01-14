from src.system import System 
from src.audio import Audio
from src.dialogue import Dialogue

prologueText1 = """
从前,这里曾是生机勃勃的世界,没有战争,没有混乱,
只有无尽的和平......
"""

prologueText2 = """
有一天,这种秩序被打破了...
天空开始浮现的影子,
正是魔王的手下。
这颗星球陷入危机之中...
"""
prologueText3 = """
但,希望可不是没有。
在这时候出现了4名勇士
他们没有名字,但他们的身份大有来头
\'战士\',\'法师\',\'骑士\'和\'忍士\'
"""
prologueText4 = """
四位勇士对战这个世界的魔王...
只见那一股强大的力量,就将魔王彻底击溃。
"""
prologueText5 = """
20年后...
"""
prologueText6 = """
艾卡罗特行星.
一个由神秘力量铸成的行星。
就在今日,新的势力正在发展...
"""
prologueText7 = """
就这样,让所有世间存在的规矩,被彻底动摇了......
"""

def Prologue():
    #Audio.playMusic("assets/audio/music/prologue.mp3",0.45)
    Dialogue("",prologueText1,0.18)
    input()
    System.Clear()
    Dialogue("",prologueText2,0.18)
    input()
    System.Clear()
    Dialogue("",prologueText3,0.18)
    input()
    System.Clear()
    Dialogue("",prologueText4,0.18)
    input()
    System.Clear()
    Dialogue("",prologueText5,0.18)
    input()
    System.Clear()
    Dialogue("",prologueText6,0.18)
    input()
    System.Clear()
    Dialogue("",prologueText7,0.18)
    input()
    System.Clear()
    System.Sleep(1)
    input("按任意键继续...")
    System.Clear()
    System.Sleep(1)
