from flask import Flask, render_template, Response, jsonify, request
from flask_cors import CORS, cross_origin
import json
import os
import sys
from citiesRepository import *
from CommonFunction import *


def GetCities1():
    lst = GetCities()
    list = []
    for s in lst:
        list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr


def GetCitiesById1():
    JsonString = request.get_json()
    Jid = JsonString['id']
    lst = GetCitiesById(Jid)
    return to_json(lst, Jid)


def GetCitiesByState_id1():
    JsonString = request.get_json()
    Jid = JsonString['state_id']
    # print(Jid)
    lst = GetCitiesByState_id(Jid)
    # print(lst)
    list = []
    for s in lst:
        # print(s)
        if s != None:
            list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr


def GetCitiesByState_code1():
    JsonString = request.get_json()
    Jid = JsonString['state_code']
    # print(Jid)
    lst = GetCitiesByState_code(Jid)
    # print(lst)
    list = []
    for s in lst:
        # print(s)
        if s != None:
            list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr


def GetCitiesByCountry_id1():
    JsonString = request.get_json()
    Jid = JsonString['country_id']
    # print(Jid)
    lst = GetCitiesByCountry_id(Jid)
    # print(lst)
    list = []
    for s in lst:
        # print(s)
        if s != None:
            list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr


def GetCitiesByCountry_code1():
    JsonString = request.get_json()
    Jid = JsonString['country_code']
    # print(Jid)
    lst = GetCitiesByCountry_code(Jid)
    # print(lst)
    list = []
    for s in lst:
        # print(s)
        if s != None:
            list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr