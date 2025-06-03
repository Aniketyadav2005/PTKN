from flask import Flask, render_template, Response, jsonify, request
from flask_cors import CORS, cross_origin
import json
import os
import sys
from auth0_usersRepository import *
from CommonFunction import *


def GetAuth0Users1():
    lst = GetAuth0Users()
    list = []
    for s in lst:
        list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr


def GetAuth0UsersById1():
    JsonString = request.get_json()
    Jid = JsonString['id']
    lst = GetAuth0UsersById(Jid)
    return to_json(lst, Jid)


def GetAuth0UsersByEmail1():
    JsonString = request.get_json()
    Jid = JsonString['email']
    # print(Jid)
    lst = GetAuth0UsersByEmail(Jid)
    # print(lst)
    list = []
    for s in lst:
        # print(s)
        if s != None:
            list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr


def GetAuth0UsersByAuth0_user_id1():
    JsonString = request.get_json()
    Jid = JsonString['auth0_user_id']
    # print(Jid)
    lst = GetAuth0UsersByAuth0_user_id(Jid)
    # print(lst)
    list = []
    for s in lst:
        # print(s)
        if s != None:
            list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr


def saveAuth0Users1():
    JsonString = request.get_json()
    ret = saveAuth0Users(JsonString)
    return to_json(ret, ret.id)


def editAuth0Users1():
    JsonString = request.get_json()
    ret = editAuth0Users(JsonString)
    return to_json(ret, ret.id)


def deleteAuth0Users1():
    JsonString = request.get_json()
    ret = deleteAuth0Users(JsonString)
    return to_json(ret, ret.id)
