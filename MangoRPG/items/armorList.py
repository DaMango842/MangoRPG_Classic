from MangoRPG.enumerates import ItemType
from MangoRPG.meta.loadmetaData import loadItemMetaData
from MangoRPG.items import *

item = loadItemMetaData()

Old_LeatherClothes = Item(
    item['armor']['0']['id'],
    item['armor']['0']['name'],
    item['armor']['0']['type'],
    item['armor']['0']['desc'],
    item['armor']['0']['price'],
    item['armor']['0']['sellPrice'],
    item['armor']['0']['Lv'],
    item['armor']['0']['Hp'],
    item['armor']['0']['Mana'],
    item['armor']['0']['Atk'],
    item['armor']['0']['Def'],
    item['armor']['0']['Matk'],
    item['armor']['0']['Mdef'],
    item['armor']['0']['amount']
)


armorList = [
    Old_LeatherClothes
]
