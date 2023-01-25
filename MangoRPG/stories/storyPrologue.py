import os
import sys
import time
from MangoRPG.dialogue import Dialogue
from MangoRPG.dialogue import DialogueRich
from MangoRPG.system import System
from MangoRPG.character.player import Player
from rich.console import Console

console=Console()

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

def PrologueIntro():
    #Audio.playMusic("assets/audio/music/prologue.mp3",0.45)
    Dialogue("",prologueText1,0.18)
    time.sleep(0.25)
    console.clear(True)
    Dialogue("",prologueText2,0.18)
    time.sleep(0.25)
    console.clear(True)
    Dialogue("",prologueText3,0.18)
    time.sleep(0.25)
    console.clear(True)
    Dialogue("",prologueText4,0.18)
    time.sleep(0.25)
    console.clear(True)
    Dialogue("",prologueText5,0.18)
    time.sleep(0.25)
    console.clear(True)
    Dialogue("",prologueText6,0.18)
    time.sleep(0.25)
    console.clear(True)
    Dialogue("",prologueText7,0.18)
    time.sleep(0.25)
    console.clear(True)
    System.Sleep(1)
    input("按任意键继续...")
    console.clear(True)
    System.Sleep(1)

def Prologue(who):
    DialogueRich("","序章",None,None,0.5)
    time.sleep(0.50)
    DialogueRich(who.Name,"我是谁?","#f02010","#ffffff",0.25)
    time.sleep(0.25)
    DialogueRich(who.Name,"这是什么地方?","#f02010","#ffffff",0.25)
    time.sleep(0.25)
    DialogueRich("???","看来有人醒过来了啊","#ffffff","#ffffff",0.25)
    time.sleep(0.25)
    DialogueRich(who.Name,"谁在这???","#f02010","#ffffff",0.25)
    time.sleep(0.25)
    DialogueRich("???","别惊慌,我不是你的敌人","#ffffff","#ffffff",0.25)
    time.sleep(0.25)
    DialogueRich("意识体","你可以称作我为意识体","#ffffff","#ffffff",0.25)
    time.sleep(0.25)
    DialogueRich(who.Name,"意识体...?","#f02010","#ffffff",0.25)
    time.sleep(0.25)
    DialogueRich("意识体","没错,这次你得在这次的故事中展开你的冒险了","#ffffff","#ffffff",0.25)
    time.sleep(0.25)
    DialogueRich("意识体","祝你好运...","#ffffff","#ffffff",0.25)
    time.sleep(0.25)
    DialogueRich("","说完就消失了。","#ffffff","#ffffff",0.5)
    time.sleep(0.25)
    DialogueRich(who.Name,"话说,为什么会有意识体存在?","#f02010","#ffffff",0.25)
    time.sleep(0.25)
    DialogueRich(who.Name,"这究竟发生了什么?","#f02010","#ffffff",0.25)
    time.sleep(0.25)
    DialogueRich(who.Name,"我必须出去看看","#f02010","#ffffff",0.25)
    time.sleep(0.25)
    DialogueRich("","记忆差不多就结束了","#ffffff","#ffffff",0.5)
    time.sleep(0.5)
    input("> 返回故事")
