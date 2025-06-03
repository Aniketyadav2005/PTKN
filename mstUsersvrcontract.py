from flask import Flask, render_template, Response, jsonify, request
from flask_cors import CORS, cross_origin
import json
import os
import sys
from mstUserRepository import *
from CommonFunction import *


def GetUser1():
    lst = GetUser()
    list = []
    for s in lst:
        list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr


def GetUserById1():
    JsonString = request.get_json()
    Jid = JsonString['id']
    lst = GetUserById(Jid)
    return to_json(lst, Jid)


def GetUserLogin1():
    JsonString = request.get_json()
    Jid = "0" # JsonString['id']
    UserName = JsonString['nvcharLoginName']
    Password = JsonString['nvcharPassword']
    lst = GetUserLogin(UserName, Password)
    list = []
    for s in lst:
        list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr


def saveUser1():
    JsonString = request.get_json()
    ret = saveUser(JsonString)
    return to_json(ret, ret.id)


def editUser1():
    JsonString = request.get_json()
    ret = editUser(JsonString)
    return to_json(ret, ret.id)


def deleteUser1():
    JsonString = request.get_json()
    ret = deleteUser(JsonString)
    return to_json(ret, ret.id)


def GetMstUserByNvcharContact1():
    JsonString = request.get_json()
    Jid = JsonString['nvcharContact']
    # print(Jid)
    lst = GetMstUserByNvcharContact(Jid)
    # print(lst)
    list = []
    for s in lst:
        # print(s)
        if s != None:
            list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr


def GetMstUserByNvcharEmail1():
    JsonString = request.get_json()
    Jid = JsonString['nvcharEmail']
    # print(Jid)
    lst = GetMstUserByNvcharEmail(Jid)
    # print(lst)
    list = []
    for s in lst:
        # print(s)
        if s != None:
            list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr
