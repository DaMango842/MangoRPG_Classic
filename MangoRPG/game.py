
from MangoRPG import *
from MangoRPG.stories.storyPrologue import *
from MangoRPG.items.weaponList import *
from MangoRPG.items.armorList import *
from MangoRPG.items.itemList import *



console = Console()

class Game():
    def __init__(self):
        pass

    def TitleLogo():
        textLogo = Text(justify="center")
        textLogo.append("MangoRPG (")
        textLogo.append(f"{versionStr}", style="#00afff")
        textLogo.append(")")
        warningLogo = Text(justify="center")
        warningLogo.append("警告! 本Demo暂未完成,虽然可玩,但可能会有bug!",style="#ff0000")
        TEXT_GROUP = Group(
            textLogo,
            Text("(C) 2022 ~ 2023 黑夜下的糖果酱", justify="center"),
            warningLogo,
        )

        LOGO_PANEL = Panel(TEXT_GROUP, title="Mango RPG")
        console.print(LOGO_PANEL)

    def TitleLogo_Debug():
        textLogo = Text(justify="center")
        textLogo.append("MangoRPG (")
        textLogo.append(f"Debug", style="#ff0f0f")
        textLogo.append(")")
        TEXT_GROUP = Group(
            textLogo,
            Text("(C) 2022 ~ 2023 黑夜下的糖果酱", justify="center"),
        )

        LOGO_PANEL = Panel(TEXT_GROUP, title="Mango RPG")
        console.print(LOGO_PANEL)

    title: str = "Mango RPG"
    version: str = versionStr
    isPrologueIntroSeen: bool = False

    # 用法:
    # Game.Title()
    def Title():
        textTitle = Text(justify="center")
        textTitle.append(f"{Game.title} ")
        textTitle.append("(")
        textTitle.append(f"{Game.version}")
        textTitle.append(")")
        text2Title = Text(justify="center")
        text2Title.append("(C) ")
        text2Title.append("2022 ")
        text2Title.append("~ ")
        text2Title.append("2023 ")
        text2Title.append("黑夜下的糖果酱")
        TITLE_GROUP = Group(
            textTitle,
            text2Title,
            Text("", justify="center"),
            Text("", justify="center"),
            Text("[S]Start    [L]Load    [N]Settings    [Q]Exit", justify="center"),
            Text("", justify="center"),
        )
        TITLE_PANEL = Panel(TITLE_GROUP, title="Mango RPG",subtitle="Made By Rich")
        console.print(TITLE_PANEL)
        option = input("-> ")
        while (True):
            if option in ['start', 'Start', 'START']:
                Game.Start("start")
            elif option in ['load', 'Load', 'LOAD']:
                Game.Start("load")
            elif option in ['setting', 'Setting', 'SETTING']:
                print("设置未在这个版本上启用! \n")
                input("> ")
                Game.Title()
            elif option in ['exit', 'Exit', 'EXIT', 'quit', 'Quit', 'QUIT']:
                sys.exit(0)
            else:
                print("请输入一个正确的命令")
                Game.Title()

    def Start(Type: str):
        if (Type in ['start', 'Start', 'START']):
            global player
            System.Clear()
            Game.Start("playing")
            pass
        elif (Type in ['load', 'Load', 'LOAD']):
            global player
            if (os.path.exists('player.save')):
                try:
                    with open('player.save', 'r', encoding='utf-8') as f:
                        data = f.read().split('\n')
                    player = Player(data[0])
                    player.Lv = int(data[1])
                    player.Hp = int(data[2])
                    player.HpMax = int(data[3])
                    player.Mana = int(data[4])
                    player.ManaMax = int(data[5])
                    player.Atk = int(data[6])
                    player.Def = int(data[7])
                    player.Matk = int(data[8])
                    player.Mdef = int(data[9])
                    player.Money = int(data[10])
                    player.Exp = int(data[11])
                    player.nextExp = int(data[12])
                    player.currWeapon = str(data[13])
                    player.currArmor = str(data[14])
                    player.career = str(data[15])
                    player.defeatEnemies = int(data[18])
                    player.trainerWon = bool(data[19])    
                    player.isSeenPrologue = bool(data[20])
                    
                    Game.isPrologueIntroSeen = True
                    print("读取存档成功!")
                    input("> ")
                    Game.Start("playing")
                    pass
                except Exception as e:
                    raise GameError(f"错误:读取存档时出错!   {e}")        
            else:
                print("错误! 无法找到存档,已为你重新开始")
                Game.Start("playing")   
                             
            if player.Name == "":
                Dialogue("", "输入你的新名字", 0.25)
                player = Player.enterPlayerName()
            else:
                pass

        elif (Type in ['playing', 'Playing', 'PLAYING']):
            # 如果未看序章开场,则会在新游戏开始后观看(暂时没法跳过,抱歉)
            if (Game.isPrologueIntroSeen == False):
                #PrologueIntro()
                Game.isPrologueIntroSeen = True
                player = Player("","无", 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 10)
                System.Clear()
            if (player.Name == ""):
                Dialogue("", "输入你的新名字", 0.25)
                player = Player.enterPlayerName()
                player.Inventory.addItem(Old_WoodenSword)
                player.Inventory.addItem(Old_LeatherClothes)
                System.Clear()
            else:
                pass
            while (player.gameOver != True):
                console.clear(True)
                if (player.Hp <= 0):
                    player.gameOver = True
                    player.GameOver()
                #菜单
                textMenuGroup = Group(
                    Text(" [C]探索 "),
                    Text(" [M]商店 "),
                    Text("--(B)状态--(I)背包--(S)保存--(P)任务--(Q)退出--")
                )
                textMenuPanel = Panel(textMenuGroup, title="菜单", subtitle=None)
                console.print(textMenuPanel)
                #player.Inventory.addItem(Old_WoodenSword)
                option = input("-> ")
                if option in ['探索', 'c', 'C']:
                    print("由于某些原因,探索暂不开放")
                    # 战斗系统维修中
                    print("但你可以游玩战斗部分")
                    Battle.startBattle(player)
                elif option in ['副本', 'f', 'F']:
                    pass
                elif option in ['任务', 'p', 'P', 'quest', 'Quest', 'QUEST']:
                    player.openQuestMenu()
                elif option in ['背包', 'i', 'I', 'inventory', 'Inventory', 'INVENTORY']:
                    player.openInventory()
                elif option in ['状态', 'b', 'B', 'stats', 'Stats', 'STATS']:
                    console.clear(True)
                    player.playerStats()
                elif option in ['保存', 's', 'S', 'save', 'Save', 'SAVE']:
                    player.saveGame()
                elif option in ['商店', 'm', 'M', 'shop', 'Shop', 'SHOP']:
                    print("商店将会在0.2版本开放")
                    # soption = input("选择商店类型")
                    # if soption in ['购买', 'buy', 'Buy']:
                    #     BuyShop().Open(player)
                    # elif soption in ['收购', 'sell', 'Sell']:
                    #     SellShop().Open(player)
                    # else:
                    #     print("")
                elif option in ['退出', 'q', 'Q', 'exit', 'Exit', 'EXIT', 'quit', 'Quit', 'QUIT']:
                    sys.exit(0)
                else:
                    print("请输入正确的命令")

            return
        else:
            pass

        # player.inventory.addItem(Old_Wooden_Sword)
        # player.OpenInventory()

        # Battle.startBattle(player)
    #关于界面
    def aboutMenu():
        print("")
        input("按任意键返回标题")
        Game.Title()
    #Credits界面
    def credits():
        print("")
        input()
        Game.Title()
