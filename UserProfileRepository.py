from datetime import datetime
import sqlite3
import sys
from sqlobject import *
import json
from CommonFunction import *


class UserProfile(SQLObject):
    intUserId = BigIntCol(default=None)
    intCityId = BigIntCol(default=None)
    nvcharUserAddress = StringCol(length=500, default=None)
    nvcharUserProfileTitle = StringCol(length=250, default=None)
    nvcharUserProfileDescription = StringCol(length=400, default=None)
    nvcharlocale = StringCol(length=250, default=None)
    nvcharAAdharNo = StringCol(length=250, default=None)
    dtDateofBirth = DateTimeCol(default=None)
    intVerificationStatus = BigIntCol(default=None)
    nvcharProfileImageUrl = StringCol(length=250, default=None)
    nvcharDescription = StringCol(length=500, default=None)
    dtDateofCreation = DateTimeCol(default=datetime.datetime.now())
    dtDateofModification = DateTimeCol(default=None)
    ynDeleted = BoolCol(default=False)


def GetUserProfile():
    try:
        Res = UserProfile.select(AND(UserProfile.q.ynDeleted == False))
        return Res
    except:
        print("error in GetUserProfileRepository.GetUserProfile", sys.exc_info()[1])


def GetUserProfileById(Jid):
    try:
        row = UserProfile.get(Jid)
        return row
    except:
        print("error in GetUserProfileRepository.GetUserProfileById", sys.exc_info()[1])


def GetUserProfileByCityId(intCityId):
    try:
        row = UserProfile.select(AND(UserProfile.q.intCityId == intCityId))
        return row
    except:
        print("error in GetUserProfileRepository.GetUserProfileByCityId", sys.exc_info()[1])


def saveUserProfile(JsonString):
    try:
        jstr = json.dumps(JsonString)
        obj = json.loads(jstr, object_hook=datetime_decoder)
        oRepository = UserProfile(**obj)
        return oRepository
    except:
        print("error in GetUserProfileRepository.saveUserProfile", sys.exc_info()[1])


def editUserProfile(JsonString1):
    try:
        jstr = json.dumps(JsonString1)
        JsonString = json.loads(jstr, object_hook=datetime_decoder)
        oMstUserProfileRepository = UserProfile.get(JsonString['id'])
        oMstUserProfileRepository.intUserId = JsonString['intUserId']
        oMstUserProfileRepository.intCityId = JsonString['intCityId']
        oMstUserProfileRepository.nvcharUserAddress = JsonString['nvcharUserAddress']
        oMstUserProfileRepository.nvcharUserProfileTitle = JsonString['nvcharUserProfileTitle']
        oMstUserProfileRepository.nvcharUserProfileDescription = JsonString['nvcharUserProfileDescription']
        oMstUserProfileRepository.nvcharlocale = JsonString['nvcharlocale']
        oMstUserProfileRepository.nvcharAAdharNo = JsonString['nvcharAAdharNo']
        oMstUserProfileRepository.dtDateofBirth = JsonString['dtDateofBirth']
        oMstUserProfileRepository.intVerificationStatus = JsonString['intVerificationStatus']
        oMstUserProfileRepository.nvcharProfileImageUrl = JsonString['nvcharProfileImageUrl']
        oMstUserProfileRepository.nvcharDescription = JsonString['nvcharDescription']
        oMstUserProfileRepository.dtDateofModification = datetime.datetime.now()
        return oMstUserProfileRepository
    except:
        print("error in GetUserProfileRepository.UserProfile", sys.exc_info()[1])


def deleteUserProfile(JsonString):
    try:
        oRepository = UserProfile.get(JsonString['id'])
        oRepository.ynDeleted = True
        return oRepository
    except:
        print("error in GetUserProfileRepository.deleteUserProfile", sys.exc_info()[1])


sqlhub.processConnection = connectionForURI('sqlite:./world.sqlite3')
UserProfile.createTable(ifNotExists=True)