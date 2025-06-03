from flask import Flask, render_template, Response, jsonify, request
from flask_cors import CORS, cross_origin
import json
import os
import sys
from mstBusinessProfileRepository import *  # Assumes you renamed the repository to match
from CommonFunction import *
from tblBusinessProfileTagsRepository import *


def GetBusinessProfileTags1():
    lst = GetBusinessProfileTags()
    list = []
    for s in lst:
        list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr


def GetBusinessProfileTagsById1():
    JsonString = request.get_json()
    Jid = JsonString['id']
    lst = GetBusinessProfileTagsById(Jid)
    return to_json(lst, Jid)


def saveBusinessProfileTags1():
    JsonString = request.get_json()
    ret = saveBusinessProfileTags(JsonString)
    return to_json(ret, ret.id)


def editBusinessProfileTags1():
    JsonString = request.get_json()
    ret = editBusinessProfileTags(JsonString)
    return to_json(ret, ret.id)


def deleteBusinessProfileTags1():
    JsonString = request.get_json()
    ret = deleteBusinessProfileTags(JsonString)
    return to_json(ret, ret.id)
