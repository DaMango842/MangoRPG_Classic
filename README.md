# MangoRPG_Classic 1.0 New
第一个作品项目源码

## 相关问题
相关问题请在[Issues](https://github.com/DaMango842/MangoRPG_Classic/issues)中说明
使用本项目进行开发时请阅读开源协议

---

## 如何游玩 - How to Play?
使用本项目需要相关依赖
- pygame
- rich

注: python 3.11用户请用
```bat
pip install pygame --pre
``` 
安装pygame

安装依赖:
```bat
pip install -r requirements.txt
```

然后打开**MangoRPG.py**而不是debugger.py
## 功能相关/功能使用
修改玩家的初始属性,请参考下面的代码中的
return Player(...)行
```python
#在player类的enterPlayerName()中
#----------------------------------------------------------------------------------------
    def enterPlayerName():
        #在这行中,你必须输入你的玩家名
        Name = input("-> ")
        #这里进行名字判定,如果为空,则使用固定名称,否则则是你输入的名称
        if (Name != ""):
            name = Name
        else:
            name = "Mango"
        #在这个位置修改除了name之外的参数
        #不能修改name这个值(因为name = 你输入的名字) 
        return Player(name,1,100,100,0,0,10,10,0,0,0,0,10)
#----------------------------------------------------------------------------------------        
```
使用新对话功能
```python
#从MangoRPG.dialogue 中导入 Dialogue或DialogueRich
from MangoRPG.dialogue import DialogueRich
#然后使用下面的内容
DialogueRich("test","Hello,world",None,None,0.12)
```
## 未来计划
已完成的计划:
- [x] 玩家类,玩家类定义
- [x] 起名系统
- [x] 敌人类,敌人类定义
- [x] 战斗系统
- [x] 物品系统
- [x] 初版背包系统
- [x] 对话系统

未完成的计划:
- [ ] 任务系统
- [ ] 商店系统
- [ ] 地图系统
- [ ] 探索系统
- [ ] 副本系统
- [ ] 多角色系统
- [ ] 模组化
- [ ] 第二版背包系统
- [ ] 第二版任务系统
- [ ] 第二版商店系统
- [ ] 第二版探索系统

未完成但是却在进行中:
- [ ] 数据储存(json)
- [ ] 数据储存(database)


### 底部信息
(C) 2022 - 2023 黑夜下的糖果酱 (Mango RPG) - 版权所有
