from flask import Flask, render_template, Response, jsonify, request
from flask_cors import CORS, cross_origin
import json
import os
import sys
from UserProfileRepository import *
from CommonFunction import *


def GetUserProfile1():
    lst = GetUserProfile()
    list = []
    for s in lst:
        list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr


def GetUserProfileById1():
    JsonString = request.get_json()
    Jid = JsonString['id']
    lst = GetUserProfileById(Jid)
    return to_json(lst, Jid)


def GetUserProfileByCityId1():
    JsonString = request.get_json()
    print("Received JSON:", JsonString)  # Debug line
    if 'intCityId' not in JsonString:
        return jsonify({"error": "Missing key 'intCityId' in JSON body"}), 400
    Jid = JsonString['intCityId']
    lst = GetUserProfileByCityId(Jid)
    list = []
    for s in lst:
        if s is not None:
            list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr


def saveUserProfile1():
    JsonString = request.get_json()
    ret = saveUserProfile(JsonString)
    return to_json(ret, ret.id)

def editUserProfile1():
    JsonString = request.get_json()
    ret = editUserProfile(JsonString)
    return to_json(ret, ret.id)


def deleteUserProfile1():
    JsonString = request.get_json()
    ret = deleteUserProfile(JsonString)
    return to_json(ret, ret.id)


