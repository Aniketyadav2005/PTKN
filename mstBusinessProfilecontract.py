from flask import Flask, render_template, Response, jsonify, request
from flask_cors import CORS, cross_origin
import json
import os
import sys
from mstBusinessProfileRepository import *
from CommonFunction import *


def GetBusinessProfile1():
    lst = GetBusinessProfile()
    list = []
    for s in lst:
        list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr


def GetBusinessProfileById1():
    JsonString = request.get_json()
    Jid = JsonString['id']
    lst = GetBusinessProfileById(Jid)
    return to_json(lst, Jid)


def saveBusinessProfile1():
    JsonString = request.get_json()
    ret = saveBusinessProfile(JsonString)
    return to_json(ret, ret.id)


def editBusinessProfile1():
    JsonString = request.get_json()
    ret = editBusinessProfile(JsonString)
    return to_json(ret, ret.id)


def deleteBusinessProfile1():
    JsonString = request.get_json()
    ret = deleteBusinessProfile(JsonString)
    return to_json(ret, ret.id)
