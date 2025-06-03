from flask import Flask, render_template, Response, jsonify, request
from flask_cors import CORS, cross_origin
import json
import os
import sys
from regionsRepository import *
from CommonFunction import *


def GetRegions1():
    lst = GetRegions()
    list = []
    for s in lst:
        list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr


def GetRegionsById1():
    JsonString = request.get_json()
    Jid = JsonString['id']
    lst = GetRegionsById(Jid)
    return to_json(lst, Jid)
