from datetime import datetime
import sqlite3
import sys
from sqlobject import *
import json
from CommonFunction import *


class MstUser(SQLObject):
    nvcharUserName = StringCol(length=250, default=None)
    nvcharLoginName = StringCol(length=50, default=None)
    nvcharPassword = StringCol(length=50, default=None)
    nvcharContact = StringCol(length=50, default=None)
    nvcharEmail = StringCol(length=50, default=None)
    ncharUserRole = StringCol(length=50, default=None)
    nvcharDescription = StringCol(length=500, default=None)
    dtDateOfCreation = DateTimeCol(default=datetime.datetime.now())
    dtDateOfModification = DateTimeCol(default=None)
    ynDeleted = BoolCol(default=False)


def GetUser():
    try:
        Res = MstUser.select(AND(MstUser.q.ynDeleted == False))
        return Res
    except:
        print("error in MstUserRepository.GetUser", sys.exc_info()[1])


def GetUserById(Jid):
    try:
        row = MstUser.get(Jid)
        return row
    except:
        print("error in MstUserRepository.GetUserById", sys.exc_info()[1])


def GetUserLogin(UserName, Password):
    try:
        Res = MstUser.select(AND(MstUser.q.ynDeleted == False, MstUser.q.nvcharLoginName == UserName, MstUser.q.nvcharPassword == Password))
        return Res
    except:
        print("error in MstUserRepository.GetUserLogin", sys.exc_info()[1])


def saveUser(JsonString):
    try:
        jstr = json.dumps(JsonString)
        obj = json.loads(jstr, object_hook=datetime_decoder)
        oRepository = MstUser(**obj)
        return oRepository
    except:
        print("error in MstUserRepository.saveUser", sys.exc_info()[1])


def editUser(JsonString1):
    try:
        jstr = json.dumps(JsonString1)
        JsonString = json.loads(jstr, object_hook=datetime_decoder)
        oMstUserRepository = MstUser.get(JsonString['id'])
        oMstUserRepository.nvcharUserName = JsonString['nvcharUserName']
        oMstUserRepository.nvcharLoginName = JsonString['nvcharLoginName']
        oMstUserRepository.nvcharPassword = JsonString['nvcharPassword']
        oMstUserRepository.nvcharContact = JsonString['nvcharContact']
        oMstUserRepository.nvcharEmail = JsonString['nvcharEmail']
        oMstUserRepository.ncharUserRole = JsonString['ncharUserRole']
        oMstUserRepository.nvcharDescription = JsonString['nvcharDescription']
        oMstUserRepository.dtDateOfModification = datetime.datetime.now()
        return oMstUserRepository
    except:
        print("error in MstUserRepository.editUser", sys.exc_info()[1])


def deleteUser(JsonString):
    try:
        oRepository = MstUser.get(JsonString['id'])
        oRepository.ynDeleted = True
        return oRepository
    except:
        print("error in MstUserRepository.deleteUser", sys.exc_info()[1])


def GetMstUserByNvcharContact(nvcharContact):
    try:
        row = MstUser.select(AND(MstUser.q.ynDeleted == False, MstUser.q.nvcharContact == nvcharContact))
        return row
    except:
        print("error in MstUserRepository.GetMstUserByNvcharContact", sys.exc_info()[1])


def GetMstUserByNvcharEmail(nvcharEmail):
    try:
        row = MstUser.select(AND(MstUser.q.ynDeleted == False, MstUser.q.nvcharEmail == nvcharEmail))
        return row
    except:
        print("error in MstUserRepository.GetMstUserByNvcharContact", sys.exc_info()[1])


sqlhub.processConnection = connectionForURI('sqlite:./world.sqlite3')
MstUser.createTable(ifNotExists=True)