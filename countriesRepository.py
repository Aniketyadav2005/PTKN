from datetime import datetime
import sqlite3
import sys
from sqlobject import *
import json
from CommonFunction import *


class Countries(SQLObject):
    name = StringCol(length=100, default=None)
    iso3 = StringCol(length=50, default=None)
    numeric_code = StringCol(length=50, default=None)
    iso2 = StringCol(length=50, default=None)
    phonecode = StringCol(length=255, default=None)
    capital = StringCol(length=255, default=None)
    currency = StringCol(length=255, default=None)
    currency_name = StringCol(length=255, default=None)
    currency_symbol = StringCol(length=255, default=None)
    tld = StringCol(length=255, default=None)
    native = StringCol(length=255, default=None)
    region = StringCol(length=255, default=None)
    region_id = BigIntCol(default=None)
    subregion = StringCol(length=255, default=None)
    subregion_id = BigIntCol(default=None)
    nationality = StringCol(length=255, default=None)
    timezones = StringCol(length=500, default=None)
    translations = StringCol(length=500, default=None)
    latitude = FloatCol(default=None)
    longitude = FloatCol(default=None)
    emoji = StringCol(length=255, default=None)
    emojiU = StringCol(length=255, default=None)
    created_at = DateTimeCol(default=datetime.datetime.now())
    updated_at = DateTimeCol(default=None)
    flag = BigIntCol(default=None)
    wikiDataId = StringCol(length=50, default=None)


def GetCountries():
    try:
        Res = Countries.select()
        return Res
    except:
        print("error in Countries.Countries", sys.exc_info()[1])


def GetCountriesById(Jid):
    try:
        row = Countries.get(Jid)
        if Jid is None:
            return jsonify({"error": "Missing or invalid JSON in request body"}), 400
        return row
    except:
        print("error in Countries.GetCountriesById", sys.exc_info()[1])


def GetCountriesByPhonecode(phonecode):
    try:
        row = Countries.select(AND(Countries.q.phonecode == phonecode))
        return row
    except:
        print("error in Countries.GetCountriesByPhonecode", sys.exc_info()[1])


def GetCountriesByRegion_id(region_id):
    try:
        row = Countries.select(AND(Countries.q.region_id == region_id))
        return row
    except:
        print("error in Countries.GetCountriesByRegion_id", sys.exc_info()[1])

sqlhub.processConnection = connectionForURI('sqlite:./world.sqlite3')