from item import Item

import sqlite3


mIconn = sqlite3.connect('database\\item.db')
mIc = mIconn.cursor()

sql = '''
    CREATE TABLE company
    (id int primary key not null,
    name text not null,
    type int not null,
    desc text not null,
    price int not null,
    sellPrice int not null,
    Lv int not null,
    Hp int not null,
    Mana int not null,
    Atk int not null,
    Def int not null,
    Matk int not null,
    Mdef int not null,
    amount int not null,
    salary real);
'''

sql1 = '''
    INSERT INTO company(id,name,type,desc,price,sellPrice,Lv,Hp,Mana,Atk,Def,Matk,Mdef,amount)
    VALUES (1,'破旧木剑',1,'一把破旧的木剑,已经很少有人用了。。。',10,5,1,0,0,5,0,0,0,1)
'''
sql2 = '''
    INSERT INTO company(id,name,type,desc,price,sellPrice,Lv,Hp,Mana,Atk,Def,Matk,Mdef,amount)
    VALUES (2,'破旧衣服',2,'一件只有农民才会穿的破旧衣服',2,0,1,0,0,0,5,0,0,1)
'''

mIc.execute(sql)
mIc.execute(sql1)
mIc.execute(sql2)