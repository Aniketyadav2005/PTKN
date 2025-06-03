from datetime import datetime
import sqlite3
import sys
from sqlobject import *
import json
from CommonFunction import *


class Auth0Users(SQLObject):
    auth0_user_id = StringCol(length=300, default=None)
    email = StringCol(length=50, default=None)
    email_verified = BoolCol(default=False)
    name = StringCol(length=300, default=None)
    nickname = StringCol(length=300, default=None)
    picture = StringCol(length=300, default=None)
    locale = StringCol(length=300, default=None)
    created_at = DateTimeCol(default=datetime.datetime.now())
    updated_at = DateTimeCol(default=None)
    user_metadata = StringCol(length=1000, default=None)
    app_metadata = StringCol(length=1000, default=None)
    ynDeleted = BoolCol(default=False)


def GetAuth0Users():
    try:
        Res = Auth0Users.select(AND(Auth0Users.q.ynDeleted == False))
        return Res
    except:
        print("error in Auth0Users.GetAuth0Users", sys.exc_info()[1])


def GetAuth0UsersById(Jid):
    try:
        row = Auth0Users.get(Jid)
        if Jid is None:
            return jsonify({"error": "Missing or invalid JSON in request body"}), 400
        return row
    except:
        print("error in Auth0Users.GetAuth0UsersById", sys.exc_info()[1])



def GetAuth0UsersByEmail(email):
    try:
        row = Auth0Users.select(AND(Auth0Users.q.email == email))
        return row
    except:
        print("error in Auth0Users.GetAuth0UsersByEmail", sys.exc_info()[1])


def GetAuth0UsersByAuth0_user_id(auth0_user_id):
    try:
        row = Auth0Users.select(AND(Auth0Users.q.auth0_user_id == auth0_user_id))
        return row
    except:
        print("error in Auth0Users.GetAuth0UsersByAuth0_user_id", sys.exc_info()[1])


def saveAuth0Users(JsonString):
    try:
        jstr = json.dumps(JsonString)
        obj = json.loads(jstr, object_hook=datetime_decoder)
        oRepository = Auth0Users(**obj)
        return oRepository
    except:
        print("error in Auth0Users.saveAuth0Users", sys.exc_info()[1])


def editAuth0Users(JsonString1):
    try:
        jstr = json.dumps(JsonString1)
        JsonString = json.loads(jstr, object_hook=datetime_decoder)
        oAuth0UsersRepository = Auth0Users.get(JsonString['id'])
        oAuth0UsersRepository.auth0_user_id = JsonString['auth0_user_id']
        oAuth0UsersRepository.email = JsonString['email']
        oAuth0UsersRepository.email_verified = JsonString['email_verified']
        oAuth0UsersRepository.name = JsonString['name']
        oAuth0UsersRepository.nickname = JsonString['nickname']
        oAuth0UsersRepository.picture = JsonString['picture']
        oAuth0UsersRepository.locale = JsonString['locale']
        oAuth0UsersRepository.created_at = JsonString['created_at']
        oAuth0UsersRepository.updated_at = datetime.datetime.now()
        oAuth0UsersRepository.user_metadata = JsonString['user_metadata']
        oAuth0UsersRepository.app_metadata = JsonString['app_metadata']
        oAuth0UsersRepository.ynDeleted = JsonString['ynDeleted']
        return oAuth0UsersRepository
    except:
        print("error in Auth0Users.editAuth0Users", sys.exc_info()[1])


def deleteAuth0Users(JsonString):
    try:
        oRepository = Auth0Users.get(JsonString['id'])
        oRepository.ynDeleted = True
        return oRepository
    except:
        print("error in Auth0Users.deleteAuth0Users", sys.exc_info()[1])


sqlhub.processConnection = connectionForURI('sqlite:./world.sqlite3')
Auth0Users.createTable(ifNotExists=True)