from MangoRPG.character.enemies import Enemy 

enemyDummy = Enemy("训练木偶",0,100,100,0,0,0,0,None,False)
enemy1 = Enemy("史莱姆",1,20,20,12,2,4,2,None,False)
enemy2 = Enemy("哥布林",1,24,24,14,4,6,4,None,False)
enemy3 = Enemy("恶鸟",1,28,28,5,16,8,5,None,False)
enemy4 = Enemy("树妖",2,32,32,8,18,9,6,None,False)
enemy5 = Enemy("黄树妖",2,34,34,20,7,10,6,None,False)
enemy6 = Enemy("腐烂意志",2,48,48,22,10,14,7,None,False)
enemy7 = Enemy("泥人",3,78,78,24,14,16,8,None,False)
enemy8 = Enemy("魔化守卫",3,100,100,26,16,20,10,None,False)
enemy9 = Enemy("魔化居民",3,120,120,28,20,25,15,None,False)
enemyBoss = Enemy("魔石",5,150,150,30,20,50,40,None,True)
enemy10 = Enemy("???",4,48,48,4,8,10,8,None,False)

EnemyListsLv1 = [
    enemy1,
    enemy2,
    enemy3
]

EnemyListsLv2 = [
    enemy4,
    enemy5,
    enemy6
]

EnemyListsLv3 = [
    enemy7,
    enemy8,
    enemy9
]



