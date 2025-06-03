from datetime import datetime
import sqlite3
import sys
from sqlobject import *
import json
from CommonFunction import *
from sqlobject.sqlbuilder import LEFTJOINOn


class Regions(SQLObject):
    name = StringCol(length=100, default=None)
    translations = StringCol(length=300, default=None)
    created_at = DateTimeCol(default=datetime.datetime.now())
    updated_at = DateTimeCol(default=None)
    flag = BigIntCol(default=None)
    wikiDataId = StringCol(length=50, default=None)


def GetRegions():
    try:
        Res =Regions.select()
        return Res
    except:
        print("error in regions.GetRegions", sys.exc_info()[1])


def GetRegionsById(Jid):
    try:
        row = Regions.get(Jid)
        return row
    except:
        print("error in regions.GetRegionsById", sys.exc_info()[1])


sqlhub.processConnection = connectionForURI('sqlite:./world.sqlite3')
#regions.createTable(ifNotExists=True)