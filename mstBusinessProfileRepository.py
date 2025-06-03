from datetime import datetime
import sys
from sqlobject import *
import json
from CommonFunction import *



class MstBusinessProfile(SQLObject):
    intUserId = BigIntCol(default=None)
    intCityId = BigIntCol(default=None)
    intBusinessCatagoryId = BigIntCol(default=None)
    nvcharBusinessProfileTitle = StringCol(length=250, default=None)
    nvcharBusinessProfileDescription = StringCol(length=400, default=None)
    nvcharlocale = StringCol(length=250, default=None)
    nvcharPAN = StringCol(length=50, default=None)
    nvcharAAdharNo = StringCol(length=50, default=None)
    nvcharGSTNo = StringCol(length=50, default=None)
    intVerificationStatus = IntCol(default=0)
    nvcharProfileImageUrl = StringCol(length=250, default=None)
    nvcharDescription = StringCol(length=500, default=None)
    dtDateOfCreation = DateTimeCol(default=datetime.datetime.now())
    dtDateofModification = DateTimeCol(default=None)
    ynDeleted = BoolCol(default=False)





def GetBusinessProfile():
    try:
        return MstBusinessProfile.select(MstBusinessProfile.q.ynDeleted == False)
    except:
        print("error in MstBusinessRepository.GetBusiness:", sys.exc_info()[1])


def GetBusinessProfileById(Jid):
    try:
        return MstBusinessProfile.get(Jid)
    except:
        print("error in MstBusinessRepository.GetBusinessById:", sys.exc_info()[1])


def saveBusinessProfile(JsonString):
    try:
        jstr = json.dumps(JsonString)
        obj = json.loads(jstr, object_hook=datetime_decoder)
        return MstBusinessProfile(**obj)
    except:
        print("error in MstBusinessRepository.saveBusiness:", sys.exc_info()[1])


def editBusinessProfile(JsonString1):
    try:
        jstr = json.dumps(JsonString1)
        JsonString = json.loads(jstr, object_hook=datetime_decoder)
        business = MstBusinessProfile.get(JsonString['id'])

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