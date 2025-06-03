from flask import Flask, render_template, Response, jsonify, request
from flask_cors import CORS, cross_origin
import json
import os
import sys
from countriesRepository import *
from CommonFunction import *


def GetCountries1():
    lst = GetCountries()
    list = []
    for s in lst:
        list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr


def GetCountriesById1():
    JsonString = request.get_json()
    Jid = JsonString['id']
    lst = GetCountriesById(Jid)
    return to_json(lst, Jid)


def GetCountriesByPhonecode1():
    JsonString = request.get_json()
    Jid = JsonString['phonecode']
    # print(Jid)
    lst = GetCountriesByPhonecode(Jid)
    # print(lst)
    list = []
    for s in lst:
        # print(s)
        if s != None:
            list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr


def GetCountriesByRegion_id1():
    JsonString = request.get_json()
    Jid = JsonString['region_id']
    # print(Jid)
    lst = GetCountriesByRegion_id(Jid)
    # print(lst)
    list = []
    for s in lst:
        # print(s)
        if s != None:
            list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr

