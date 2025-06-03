from datetime import datetime
import sqlite3
import sys
from sqlobject import *
import json
from CommonFunction import *
from sqlobject import *
import datetime

class msCategory(SQLObject):
    inCatagoryId = IntCol(default=None)
    nvcharCatagoryName = StringCol(length=255, default=None)
    nvcharDescription = StringCol(length=500, default=None)
    dtDateofCreation = DateTimeCol(default=datetime.datetime.now())
    dtDateofModification = DateTimeCol(default=None)
    ynDeleted = BoolCol(default=False)



def GetmsCategory():
    try:
        return msCategory.select(msCategory.q.ynDeleted == False)
    except:
        print("error in msCategoryRepository.GetBusiness:", sys.exc_info()[1])


def GetmsCategoryById(Jid):
    try:
        return msCategory.get(Jid)
    except:
        print("error in msCategoryRepository.GetBusinessById:", sys.exc_info()[1])


def savemsCategory(JsonString):
    try:
        jstr = json.dumps(JsonString)
        obj = json.loads(jstr, object_hook=datetime_decoder)
        return msCategory(**obj)
    except:
        print("error in msCategoryRepository.saveBusiness:", sys.exc_info()[1])


def editmsCategory(JsonString1):
    try:
        jstr = json.dumps(JsonString1)
        JsonString = json.loads(jstr, object_hook=datetime_decoder)
        business = msCategory.get(JsonString['id'])

        business.intUserId = JsonString['intUserId']
        business.intCityId = JsonString['intCityId']
        business.intBusinessCatagoryId = JsonString['intBusinessCatagoryId']
        business.nvcharBusinessProfileTitle = JsonString['nvcharBusinessProfileTitle']
        business.nvcharBusinessProfileDescription = JsonString['nvcharBusinessProfileDescription']
        business.nvcharlocale = JsonString['nvcharlocale']
        business.nvcharPAN = JsonString['nvcharPAN']
        business.nvcharAAdharNo = JsonString['nvcharAAdharNo']
        business.nvcharGSTNo = JsonString['nvcharGSTNo']
        business.intVerificationStatus = JsonString['intVerificationStatus']
        business.nvcharProfileImageUrl = JsonString['nvcharProfileImageUrl']
        business.nvcharDescription = JsonString['nvcharDescription']
        business.dtDateofModification = datetime.datetime.now()

        return business
    except:
        print("error in MstBusinessProfileRepository.editBusinessProfile:", sys.exc_info()[1])


def deleteBusinessProfile(JsonString):
    try:
        business = MstBusinessProfile.get(JsonString['id'])
        business.ynDeleted = True
        return business
    except:
        print("error in MstBusinessProfileRepository.deleteBusiness:", sys.exc_info()[1])


# Connect to your SQLite database
sqlhub.processConnection = connectionForURI('sqlite:./world.sqlite3')

# Create the table (if it doesn't already exist)
MstBusinessProfile.createTable(ifNotExists=True)