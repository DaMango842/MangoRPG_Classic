from MangoRPG.exception import *
from MangoRPG.character.player import Player
from MangoRPG.enemiesList import *
from MangoRPG.dialogue import *
from MangoRPG.system import *
from MangoRPG.stories.storyPrologue import Prologue
from rich import print
from rich.bar import Bar
from rich.console import Console
from enum import Enum
import numpy as np

console = Console()

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
        enemyCountLowerLv5 = np.random.randint(0, 2)
        if who.trainerWon != True:
            enemy = enemyDummy
        else:
            if (who.Lv >= 1):
                if enemyCountLowerLv5 >= len(EnemyListsLv1):
                    raise BattleError("敌人数量不合法!")
                else:
                    enemy = EnemyListsLv1[enemyCountLowerLv5]
            elif (who.Lv >= 2):
                if enemyCountLowerLv5 >= len(EnemyListsLv2):
                    raise BattleError("敌人数量不合法!")
                else:
                    enemy = EnemyListsLv2[enemyCountLowerLv5]
            elif (who.Lv >= 3):
                if enemyCountLowerLv5 >= len(EnemyListsLv3):
                    raise BattleError("敌人数量不合法!")
                else:
                    enemy = EnemyListsLv3[enemyCountLowerLv5]
            elif (who.Lv >= 5):
                isBossBattleCount = np.random(1,100)
                if isBossBattleCount >= 75:
                    enemy = enemyBoss
                else:
                    if enemyCountLowerLv5 >= len(EnemyListsLv3):
                        raise BattleError("敌人数量不合法!")
                    else:
                        enemy = EnemyListsLv3[enemyCountLowerLv5]               
        if (who.trainerWon == True and not who.isSeenPrologue):
            Prologue(who)
            
        if (who.defeatEnemies == 20):
            pass
        elif (who.defeatEnemies == 40):
            pass
        else:
            pass
        Dialogue("", "敌人出现!!!\n", 0.25)

        global battleEnd
        global runaway
        battleEnd = False
        runaway = False

        enemy.Hp = enemy.HpMax

        currTurn = BattleTurn.playerTurn
        while (battleEnd != True):
            match (currTurn):
                case BattleTurn.playerTurn:
                    console.clear()
                    print(f"敌人: {enemy.Name}")
                    console.print("HP: ")
                    # Debugger!!!
                    # enemyHpBar = Bar(1,width=20,begin=float(enemy.Hp),end=float(enemy.HpMax),color='grey0',bgcolor='red')
                    # print(enemyHpBar)
                    print("%d / %d" % (enemy.Hp, enemy.HpMax))
                    print("")
                    print(f"名字: {who.Name}")
                    console.print("HP: ")
                    # Debugger!!!
                    # playerHpBar = Bar(1,width=20,begin=float(who.Hp),end=float(who.HpMax),color='grey0',bgcolor='red')
                    # print(playerHpBar)
                    print("%d / %d" % (who.Hp, who.HpMax))
                    print("")
                    DialogueRich("", "选择你的行动","#ffffff","#ffffff", 0.25)
                    print("")
                    print("攻击 | 技能 | 物品 | 逃跑")
                    pturn = input()
                    if pturn == "攻击" or pturn == "Attack" or pturn == "attack":
                        print("")
                        pDamage = who.Atk - enemy.Def
                        enemy.Hp -= pDamage
                        print(f" 你 对 {enemy.Name} 造成了 {pDamage} 点伤害!")
                        time.sleep(1)
                        if (enemy.Hp > enemy.HpMax):
                            enemy.Hp = enemy.HpMax
                        if (enemy.Hp <= 0):
                            currTurn = BattleTurn.endTurn
                        else:
                            currTurn = BattleTurn.enemyTurn
                    elif pturn == "技能" or pturn == "Skill" or pturn == "skill":
                        print("")
                        print("暂未开放,技能暂未开发")
                        time.sleep(1)
                        currTurn = BattleTurn.playerTurn
                    elif pturn == "物品" or pturn == "Item" or pturn == "item":
                        print("")
                        print("背包里没有物品")
                        time.sleep(1)
                        currTurn = BattleTurn.playerTurn
                    elif pturn == "逃跑" or pturn == "Run" or pturn == "run":
                        fleeSuccess = np.random.randint(0, 100)
                        if (fleeSuccess >= 75):
                            DialogueRich("", "逃跑成功!","#ffffff","#ffffff", 0.15)
                            time.sleep(0.10)
                            runaway = True
                            currTurn = BattleTurn.endTurn
                        else:
                            DialogueRich("", "逃跑失败!","#ffffff","#ffffff", 0.15)
                            time.sleep(0.10)
                            currTurn = BattleTurn.endTurn
                case BattleTurn.enemyTurn:
                    print("")
                    DialogueRich("", "敌人的回合!","#ffffff","#ffffff", 0.30)
                    eDamage = enemy.Atk - who.Def
                    who.Hp -= eDamage
                    print("")
                    print(f"{enemy.Name}对 你 造成了 {eDamage} 点伤害!")
                    time.sleep(1)
                    if (who.Hp > who.HpMax):
                        who.Hp = who.HpMax
                    if (who.Hp <= 0):
                        currTurn = BattleTurn.endTurn
                    else:
                        currTurn = BattleTurn.endTurn
                case BattleTurn.endTurn:
                    if (who.Hp <= 0):
                        who.Hp = 0
                        console.clear()
                        #DialogueRich("", "战斗失败!","#ffffff","#ffffff", 0.30)
                        Player.GameOver()
                    elif (enemy.Hp <= 0):
                        enemy.Hp = 0
                        if (enemy.Name == "训练木偶"):
                            who.defeatEnemies == 0
                            who.trainerWon == True
                        else:
                            who.defeatEnemies += 1
                        who.Money += enemy.Money
                        who.Exp += enemy.Exp
                        console.clear()
                        DialogueRich(
                            "", f"战斗胜利! 获得了{enemy.Money}金币和{enemy.Exp}点经验","#ffffff","#ffffff", 0.30)
                        who.levelUp()
                        battleEnd = True
                    elif (runaway == True):
                        battleEnd = True
                    else:
                        if (who.Hp > who.HpMax):
                            who.Hp = who.HpMax
                        currTurn = BattleTurn.playerTurn
                case _:
                    raise BattleError("错误的回合")
