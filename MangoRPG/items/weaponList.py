from MangoRPG.enumerates import ItemType
from MangoRPG.meta.loadmetaData import loadItemMetaData
from MangoRPG.items import *

item = loadItemMetaData()

Old_WoodenSword = Item(
    item['weapon']['0']['id'],
    item['weapon']['0']['name'],
    item['weapon']['0']['type'],
    item['weapon']['0']['desc'],
    item['weapon']['0']['price'],
    item['weapon']['0']['sellPrice'],
    item['weapon']['0']['Lv'],
    item['weapon']['0']['Hp'],
    item['weapon']['0']['Mana'],
    item['weapon']['0']['Atk'],
    item['weapon']['0']['Def'],
    item['weapon']['0']['Matk'],
    item['weapon']['0']['Mdef'],
    item['weapon']['0']['amount']
)

WoodenSword = Item(
    item['weapon']['1']['id'],
    item['weapon']['1']['name'],
    item['weapon']['1']['type'],
    item['weapon']['1']['desc'],
    item['weapon']['1']['price'],
    item['weapon']['1']['sellPrice'],
    item['weapon']['1']['Lv'],
    item['weapon']['1']['Hp'],
    item['weapon']['1']['Mana'],
    item['weapon']['1']['Atk'],
    item['weapon']['1']['Def'],
    item['weapon']['1']['Matk'],
    item['weapon']['1']['Mdef'],
    item['weapon']['1']['amount']
)