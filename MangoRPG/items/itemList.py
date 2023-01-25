from MangoRPG.enumerates import ItemType
from MangoRPG.meta.loadmetaData import loadItemMetaData
from MangoRPG.items import *

item = loadItemMetaData()

TestItem = Item(
    999,
    "测试物品",
    4,
    "就只是用来测试的",
    0,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    1
)
