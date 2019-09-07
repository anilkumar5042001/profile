from django.shortcuts import render
from django.http import Http404
from django.http import JsonResponse
from django.conf import settings
import json
from django.views.decorators.csrf import csrf_exempt
from .DBObjects.BAL import CountryBAL
from .DBObjects.Entity import CountryEntity
from django.core import serializers
from .DBScripts.MySqlTable import MySqlTable
from .DBScripts.ExecOrder import ExecOrder
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .DBObjects.BAL import UserProfileBAL
from .DBObjects.Entity import UserProfileEntity
from .DBObjects.BAL import WorkHistoryBAL
from .DBObjects.Entity import WorkHistoryEntity

#{"ProfileId": "1","CompanyName":"WebSynergies","Role":"Testing","Description":"I worked as a Test Engineer","City":"Hyd","Country":"India","StartMonth":"1","StartYear":"2016","EndMonth":"6","EndYear":"2019","CurrentlyWorking":"0"}
@csrf_exempt
@api_view(["POST"])
def WorkHistoryInsert(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strProfileId=loaded_json["ProfileId"]
        strCompanyName=loaded_json["CompanyName"]
        strRole=loaded_json["Role"]
        strDescription=loaded_json["Description"]
        strCity=loaded_json["City"]
        strCountry=loaded_json["Country"]
        strStartMonth=loaded_json["StartMonth"]
        strStartYear=loaded_json["StartYear"]
        strEndMonth=loaded_json["EndMonth"]
        strEndYear=loaded_json["EndYear"]
        strCurrentlyWorking=loaded_json["CurrentlyWorking"]
        objWorkHistoryBAL=WorkHistoryBAL.WorkHistoryBAL()
        result=objWorkHistoryBAL.WorkHistoryInsert(strProfileId,strCompanyName,strRole,strDescription,strCity,strCountry,strStartMonth,strStartYear,strEndMonth,strEndYear,strCurrentlyWorking)
        return JsonResponse("1",safe=False)

#{"WorkHistoryId": 1}
@csrf_exempt
@api_view(["POST"])
def GetWorkHistoryById(json_data):
        loaded_json = json.loads(json_data.body)
        objWorkHistoryBAL=WorkHistoryBAL.WorkHistoryBAL()
        strWorkHistoryId=loaded_json["WorkHistoryId"]
        objWorkHistoryEntity=objWorkHistoryBAL.WorkHistoryGetById(strWorkHistoryId)
        result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity])

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"ProfileId":"1","WorkHistoryId": "1","CompanyName": "Infosys", "Role": "SAP", "Description":"Changed my technology","City":"Banglore","Country":"India","StartMonth":"12","StartYear": "2015","EndMonth": "11","EndYear": "2018","CurrentlyWorking": "1"}
@csrf_exempt
@api_view(["POST"])
def WorkHistoryUpdate(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strProfileId=loaded_json["ProfileId"]
        strWorkHistoryId=loaded_json["WorkHistoryId"]
        strCompanyName=loaded_json["CompanyName"]
        strRole=loaded_json["Role"]
        strDescription=loaded_json["Description"]
        strCity=loaded_json["City"]
        strCountry=loaded_json["Country"]
        strStartMonth=loaded_json["StartMonth"]
        strStartYear=loaded_json["StartYear"]
        strEndMonth=loaded_json["EndMonth"]
        strEndYear=loaded_json["EndYear"]
        strCurrentlyWorking=loaded_json["CurrentlyWorking"]
        objWorkHistoryBAL=WorkHistoryBAL.WorkHistoryBAL()
        result=objWorkHistoryBAL.WorkHistoryUpdate(strProfileId,strWorkHistoryId,strCompanyName,strRole,strDescription,strCity,strCountry,strStartMonth,strStartYear,strEndMonth,strEndYear,strCurrentlyWorking)
        return JsonResponse("1",safe=False)