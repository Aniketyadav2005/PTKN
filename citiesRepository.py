from datetime import datetime
import sqlite3
import sys
from sqlobject import *
import json
from CommonFunction import *


class Cities(SQLObject):
    name = StringCol(length=100, default=None)
    state_id = BigIntCol(default=None)
    state_code = StringCol(length=100, default=None)
    country_id = BigIntCol(default=None)
    country_code = StringCol(length=50, default=None)
    latitude = FloatCol(default=None)
    longitude = FloatCol(default=None)
    created_at = DateTimeCol(default=datetime.datetime.now())
    updated_at = DateTimeCol(default=None)
    flag = BigIntCol(default=None)
    wikiDataId = StringCol(length=50, default=None)


def GetCities():
    try:
        Res = Cities.select()
        return Res
    except:
        print("error in Cities.GetCities", sys.exc_info()[1])


def GetCitiesById(Jid):
    try:
        row = Cities.get(Jid)
        if Jid is None:
            return jsonify({"error": "Missing or invalid JSON in request body"}), 400
        return row
    except:
        print("error in Cities.GetCitiesById", sys.exc_info()[1])


def GetCitiesByState_id(state_id):
    try:
        row = Cities.select(AND(Cities.q.state_id == state_id))
        return row
    except:
        print("error in Cities.GetCitiesByState_id", sys.exc_info()[1])


def GetCitiesByState_code(state_code):
    try:
        row = Cities.select(AND(Cities.q.state_code == state_code))
        return row
    except:
        print("error in Cities.GetCitiesByState_code", sys.exc_info()[1])


def GetCitiesByCountry_id(country_id):
    try:
        row = Cities.select(AND(Cities.q.country_id == country_id))
        return row
    except:
        print("error in Cities.GetCitiesByCountry_id", sys.exc_info()[1])


def GetCitiesByCountry_code(country_code):
    try:
        row = Cities.select(AND(Cities.q.country_code == country_code))
        return row
    except:
        print("error in Cities.GetCitiesByCountry_code", sys.exc_info()[1])


sqlhub.processConnection = connectionForURI('sqlite:./world.sqlite3')
Cities.createTable(ifNotExists=True)