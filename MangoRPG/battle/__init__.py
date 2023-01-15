from MangoRPG.exception import *
from MangoRPG.character.player import *
from MangoRPG.enemiesGroup import *
from MangoRPG.dialogue import *
from MangoRPG.system import *

from rich import print
from rich.bar import Bar
from rich.console import Console
from enum import Enum
import random

class BattleTurn(Enum):
    playerTurn = 1
    enemyTurn = 2
    endTurn = 3

# currTurn = [
#     BattleTurn.playerTurn,
#     BattleTurn.enemyTurn,
#     BattleTurn.endTurn
# ]


class Battle():

    def __init__(self) -> None:
        pass

    def startBattle(who: Player):
        enemyCount = random.randint(0, 3)
        if enemyCount >= len(EnemyGroup):
            raise BattleError("敌人数量不合法!")
        enemy = EnemyGroup[enemyCount]
        Dialogue("", "敌人出现!!!\n", 0.25)

        global battleEnd
        global runaway
        battleEnd = False
        runaway = False

        currTurn = BattleTurn.playerTurn
        while (battleEnd != True):
            match (currTurn):
                case BattleTurn.playerTurn:
                    System.Clear()
                    print(f"敌人: {enemy.Name}")
                    System.Write("HP: ")
                    # Debugger!!!
                    # enemyHpBar = Bar(1,width=20,begin=float(enemy.Hp),end=float(enemy.HpMax),color='grey0',bgcolor='red')
                    # print(enemyHpBar)
                    print("%d / %d" % (enemy.Hp, enemy.HpMax))
                    print("")
                    print(f"名字: {who.Name}")
                    System.Write("HP: ")
                    # Debugger!!!
                    # playerHpBar = Bar(1,width=20,begin=float(who.Hp),end=float(who.HpMax),color='grey0',bgcolor='red')
                    # print(playerHpBar)
                    print("%d / %d" % (who.Hp, who.HpMax))
                    print("")
                    Dialogue("", "选择你的行动", 0.25)
                    print("")
                    print("攻击 | 技能 | 物品 | 逃跑")
                    pturn = input()
                    if pturn == "攻击" or pturn == "Attack" or pturn == "attack":
                        print("")
                        pDamage = who.Atk - enemy.Def
                        enemy.Hp -= pDamage
                        print(f" 你 对 {enemy.Name} 造成了 {pDamage} 点伤害!")
                        System.Sleep(1)
                        if (enemy.Hp > enemy.HpMax):
                            enemy.Hp = enemy.HpMax
                        if (enemy.Hp <= 0):
                            currTurn = BattleTurn.endTurn
                        else:
                            currTurn = BattleTurn.enemyTurn
                    elif pturn == "技能" or pturn == "Skill" or pturn == "skill":
                        print("")
                        print("暂未开放,技能暂未开发")
                        System.Sleep(1)
                        currTurn = BattleTurn.playerTurn
                    elif pturn == "物品" or pturn == "Item" or pturn == "item":
                        print("")
                        print("背包里没有物品")
                        System.Sleep(1)
                        currTurn = BattleTurn.playerTurn
                    elif pturn == "逃跑" or pturn == "Run" or pturn == "run":
                        fleeSuccess = random.randint(0, 100)
                        if (fleeSuccess >= 75):
                            Dialogue("", "逃跑成功!", 0.15)
                            System.Sleep(0.10)
                            runaway = True
                            currTurn = BattleTurn.endTurn
                        else:
                            Dialogue("", "逃跑失败!", 0.15)
                            System.Sleep(0.10)
                            currTurn = BattleTurn.endTurn       
                case BattleTurn.enemyTurn:
                    print("")
                    Dialogue("","敌人的回合!",0.30)
                    eDamage = enemy.Atk - who.Def
                    who.Hp -= eDamage
                    print("")
                    print(f"{enemy.Name}对 你 造成了 {eDamage} 点伤害!")
                    System.Sleep(1)
                    if (who.Hp > who.HpMax):
                        who.Hp = who.HpMax
                    if (who.Hp <= 0):
                        currTurn = BattleTurn.endTurn
                    else:
                        currTurn = BattleTurn.endTurn
                case BattleTurn.endTurn:
                    if (who.Hp <= 0):
                        who.Hp = 0
                        System.Clear()
                        Dialogue("","战斗失败!",0.30)
                        Player.GameOver()
                    elif (enemy.Hp <= 0):
                        enemy.Hp = 0
                        who.Money += enemy.Money
                        who.Exp += enemy.Exp
                        System.Clear()
                        Dialogue("",f"战斗胜利! 获得了{enemy.Money}金币和{enemy.Exp}点经验",0.30)
                        battleEnd = True
                    elif (runaway == True):
                        battleEnd = True    
                    else:
                        if (who.Hp > who.HpMax):
                            who.Hp = who.HpMax
                        currTurn = BattleTurn.playerTurn
                case _:
                    raise BattleError("错误的回合")            