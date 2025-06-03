import json
import os
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from regionscontract import *
from citiescontract import *
from countriescontract import *
from statescontract import *
from auth0_userscontract import *
from mstUsersvrcontract import *
from UserProfilecontract import *
from mstBusinessProfilecontract import *
from tblBusinessProfileTagscontract import *
from msCatagorycontract import *


app = Flask(__name__)
cors = CORS(app)

CORS(app, resources={r'/*': {'origins': '*'}})


# --------------------Regions-------------------------------------------------------------------------------
@app.route('/GetRegions', methods=['GET'])
@cross_origin()
def GetRegions():
    return GetRegions1()


@app.route('/GetRegionsById', methods=['POST'])
@cross_origin()
def GetRegionsById():
    return GetRegionsById1()


# --------------------cities-------------------------------------------------------------------------------
@app.route('/GetCities', methods=['GET'])
@cross_origin()
def GetCities():
    return GetCities1()


@app.route('/GetCitiesById', methods=['POST'])
@cross_origin()
def GetCitiesById():
    return GetCitiesById1()


@app.route('/GetCitiesByState_id', methods=['POST'])
@cross_origin()
def GetCitiesByState_id():
    return GetCitiesByState_id1()


@app.route('/GetCitiesByState_code', methods=['POST'])
@cross_origin()
def GetCitiesByState_code():
    return GetCitiesByState_code1()


@app.route('/GetCitiesByCountry_id', methods=['POST'])
@cross_origin()
def GetCitiesByCountry_id():
    return GetCitiesByCountry_id1()


@app.route('/GetCitiesByCountry_code', methods=['POST'])
@cross_origin()
def GetCitiesByCountry_code():
    return GetCitiesByCountry_code1()


# --------------------Countries-----------------------------------------------------------------------------


@app.route('/GetCountries', methods=['GET'])
@cross_origin()
def GetCountries():
    return GetCountries1()


@app.route('/GetCountriesById', methods=['POST'])
@cross_origin()
def GetCountriesById():
    return GetCountriesById1()


@app.route('/GetCountriesByPhonecode', methods=['POST'])
@cross_origin()
def GetCountriesByPhonecode():
    return GetCountriesByPhonecode1()


@app.route('/GetCountriesByRegion_id', methods=['POST'])
@cross_origin()
def GetCountriesByRegion_id():
    return GetCountriesByRegion_id1()


# -------------------------States-------------------------------------------------------------

@app.route('/GetStates', methods=['GET'])
@cross_origin()
def GetStates():
    return GetStates1()


@app.route('/GetStatesById', methods=['POST'])
@cross_origin()
def GetStatesById():
    return GetStatesById1()


@app.route('/GetStatesByCountry_id', methods=['POST'])
@cross_origin()
def GetStatesByCountry_id():
    return GetStatesByCountry_id1()


@app.route('/GetStatesByCountry_code', methods=['POST'])
@cross_origin()
def GetStatesByCountry_code():
    return GetStatesByCountry_code1()


# -----------------Auth0_Users--------------------------------------------------------------------------

@app.route('/GetAuth0Users', methods=['GET'])
@cross_origin()
def GetAuth0_Users():
    return GetAuth0Users1()


@app.route('/GetAuth0UsersById', methods=['POST'])
@cross_origin()
def GetAuth0UsersById():
    return GetAuth0UsersById1()


@app.route('/GetAuth0UsersByEmail', methods=['POST'])
@cross_origin()
def GetAuth0UsersByEmail():
    return GetAuth0UsersByEmail1()


@app.route('/GetAuth0UsersByAuth0_user_id', methods=['POST'])
@cross_origin()
def GetAuth0UsersByAuth0_user_id():
    return GetAuth0UsersByAuth0_user_id1()


@app.route('/saveAuth0Users', methods=['POST'])
@cross_origin()
def saveAuth0Users():
    return saveAuth0Users1()


@app.route('/editAuth0Users', methods=['POST'])
@cross_origin()
def editAuth0Users():
    return editAuth0Users1()


@app.route('/deleteAuth0Users', methods=['POST'])
@cross_origin()
def deleteAuth0Users():
    return deleteAuth0Users1()

# ---------------------------------MstUser---------------------------------------------------------------


@app.route('/GetUser', methods=['GET'])
@cross_origin()
def GetUser():
    return GetUser1()


@app.route('/GetUserById', methods=['POST'])
@cross_origin()
def GetUserById():
    return GetUserById1()


@app.route('/GetUserLogin', methods=['POST'])
@cross_origin()
def GetUserLogin():
    return GetUserLogin1()


@app.route('/saveUser', methods=['POST'])
@cross_origin()
def saveUser():
    return saveUser1()


@app.route('/editUser', methods=['POST'])
@cross_origin()
def editUser():
    return editUser1()


@app.route('/deleteUser', methods=['POST'])
@cross_origin()
def deleteUser():
    return deleteUser1()


@app.route('/GetMstUserByNvcharContact', methods=['POST'])
@cross_origin()
def GetMstUserByNvcharContact():
    return GetMstUserByNvcharContact1()


@app.route('/GetMstUserByNvcharEmail', methods=['POST'])
@cross_origin()
def GetMstUserByNvcharEmail():
    return GetMstUserByNvcharEmail1()

#------------------------------UserProfile------------------------------------

@app.route('/GetUserProfile', methods=['GET'])
@cross_origin()
def GetUserProfile():
    return GetUserProfile1()

@app.route('/GetUserProfileById', methods=['POST'])
@cross_origin()
def GetUserProfileById():
    return GetUserProfileById1()

@app.route('/GetUserProfileByCityId', methods=['POST'])
@cross_origin()
def GetUserProfileByCityId():
    return GetUserProfileByCityId1()

@app.route('/saveUserProfile', methods=['POST'])
@cross_origin()
def saveUserProfile():
    return saveUserProfile1()

@app.route('/editUserProfile', methods=['POST'])
@cross_origin()
def editUserProfile():
    return editUserProfile1()

@app.route('/deleteUserProfile', methods=['POST'])
@cross_origin()
def deleteUserProfile():
    return deleteUserProfile1()

#----------------------------- mstBusinessProfile ---------------------------------------------



@app.route('/GetBusinessProfile', methods=['GET'])
@cross_origin()
def GetBusinessProfile():
    return GetBusinessProfile1()

@app.route('/GetBusinessProfileById', methods=['POST'])
@cross_origin()
def GetBusinessProfileById():
    return GetBusinessProfileById1()

@app.route('/saveBusinessProfile', methods=['POST'])
@cross_origin()
def saveBusinessProfile():
    return saveBusinessProfile1()

@app.route('/editBusinessProfile', methods=['POST'])
@cross_origin()
def editBusinessProfile():
    return editBusinessProfile1()

@app.route('/deleteBusinessProfile', methods=['POST'])
@cross_origin()
def deleteBusinessProfile():
    return deleteBusinessProfile1()

#----------------------------------------tblBusinessProfileTags --------------------------------------

@app.route('/GetBusinessProfileTags', methods=['GET'])
@cross_origin()
def GetBusinessProfileTags():
    return GetBusinessProfileTags1()

@app.route('/GetBusinessProfileTagsById', methods=['POST'])
@cross_origin()
def GetBusinessProfileTagsById():
    return GetBusinessProfileTagsById1()

@app.route('/saveBusinessProfileTags', methods=['POST'])
@cross_origin()
def saveBusinessProfileTags():
    return saveBusinessProfileTags1()

@app.route('/editBusinessProfileTags', methods=['POST'])
@cross_origin()
def editBusinessProfileTags():
    return editBusinessProfileTags1()

@app.route('/deleteBusinessProfileTags', methods=['POST'])
@cross_origin()
def deleteBusinessProfileTags():
    return deleteBusinessProfileTags1()



#--------------------------------------------------- msCatagory -------------------------------------------------


@app.route('/GetmsCategory', methods=['GET'])
@cross_origin()
def GetmsCategory():
    return GetmsCategory1()

@app.route('/GetmsCategoryById', methods=['POST'])
@cross_origin()
def GetmsCategoryById():
    return GetmsCategoryById1()

@app.route('/savemsCategory', methods=['POST'])
@cross_origin()
def savemsCategory():
    return savemsCategory1()

@app.route('/editmsCategory', methods=['POST'])
@cross_origin()
def editmsCategory():
    return editmsCategory1()

@app.route('/deletemsCategory', methods=['POST'])
@cross_origin()
def deletemsCategory():
    return deletemsCategory1()










if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
