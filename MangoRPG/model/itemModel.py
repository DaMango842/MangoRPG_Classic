#from src.items import Item
import sqlite3
import numpy as np

itemList = []

def convertToItem(name:str):
    with sqlite3.connect('database\\item.db') as db:
        data = db.execute('SELECT * FROM company where name = ?;',(name,))
        t = data.fetchone()
        l = list(t)
        return itemList.append(l)


if __name__ == '__main__':
    convertToItem("破旧木剑")
    convertToItem("破旧衣服")
    print(itemList)