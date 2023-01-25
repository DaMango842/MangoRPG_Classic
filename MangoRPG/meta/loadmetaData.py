import sys
import json

def loadItemMetaData():
    with open("meta/item.json",'r',encoding='utf-8') as f:
         List = json.load(f)
    return List