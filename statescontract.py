from flask import Flask, render_template, Response, jsonify, request
from flask_cors import CORS, cross_origin
import json
import os
import sys
from statesRepository import *
from CommonFunction import *


def GetStates1():
    lst = GetStates()
    list = []
    for s in lst:
        list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr


def GetStatesById1():
    JsonString = request.get_json()
    Jid = JsonString['id']
    lst = GetStatesById(Jid)
    return to_json(lst, Jid)


def GetStatesByCountry_id1():
    JsonString = request.get_json()
    Jid = JsonString['country_id']
    # print(Jid)
    lst = GetStatesByCountry_id(Jid)
    # print(lst)
    list = []
    for s in lst:
        # print(s)
        if s != None:
            list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr


def GetStatesByCountry_code1():
    JsonString = request.get_json()
    Jid = JsonString['country_code']
    # print(Jid)
    lst = GetStatesByCountry_code(Jid)
    # print(lst)
    list = []
    for s in lst:
        # print(s)
        if s != None:
            list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr