from datetime import datetime
import sys
from sqlobject import *
import json
from CommonFunction import *
from sqlobject import *


# Define the table
class tblBusinessProfileTags(SQLObject):
    intBusinessProfileId = BigIntCol(default=None)
    intBusinessProfileTagsId = BigIntCol(default=None)
    intCatagoryId = BigIntCol(default=None)
    intCatagoryTagId = BigIntCol(default=None)
    nvcharDescription = StringCol(length=500, default=None)
    dtDateOfCreation = DateTimeCol(default=datetime.datetime.now())
    dtDateofModification = DateTimeCol(default=None)
    ynDeleted = BoolCol(default=False)

def GetBusinessProfileTags():
    try:
        return tblBusinessProfileTags.select(tblBusinessProfileTags.q.ynDeleted == False)
    except:
        print("error in MstBusinessTagsRepository.GetBusinessTags:", sys.exc_info()[1])


def GetBusinessProfileTagsById(Jid):
    try:
        return tblBusinessProfileTags.get(Jid)
    except:
        print("error in MstBusinessTagsRepository.GetBusinessTagsById:", sys.exc_info()[1])


def saveBusinessProfileTags(JsonString):
    try:
        jstr = json.dumps(JsonString)
        obj = json.loads(jstr, object_hook=datetime_decoder)
        return tblBusinessProfileTags(**obj)
    except:
        print("error in MstBusinessTagsRepository.saveBusinessTags:", sys.exc_info()[1])


def editBusinessProfileTags(JsonString1):
    try:
        jstr = json.dumps(JsonString1)
        JsonString = json.loads(jstr, object_hook=datetime_decoder)
        business = tblBusinessProfileTags.get(JsonString['id'])
        business.intBusinessProfileId = JsonString.get('intBusinessProfileId', business.intBusinessProfileId)
        business.intBusinessProfileTagsId = JsonString.get('intBusinessProfileTagsId', business.intBusinessProfileTagsId)
        business.intCatagoryId = JsonString.get('intCatagoryId', business.intCatagoryId)
        business.intCatagoryTagId = JsonString.get('intCatagoryTagId', business.intCatagoryTagId)
        business.nvcharDescription = JsonString.get('nvcharDescription', business.nvcharDescription)
        business.dtDateofModification = datetime.datetime.now()

        return business
    except Exception as e:
        print("error in MstBusinessTagsRepository.editBusinessTags:", e)
        return None


def deleteBusinessProfileTags(JsonString):
    try:
        business = tblBusinessProfileTags.get(JsonString['id'])
        business.ynDeleted = True
        return business
    except:
        print("error in MstBusinessTagsRepository.deleteBusinessTags:", sys.exc_info()[1])


# Connect to your SQLite database
sqlhub.processConnection = connectionForURI('sqlite:./world.sqlite3')

# Create the table (if it doesn't already exist)
tblBusinessProfileTags.createTable(ifNotExists=True)

