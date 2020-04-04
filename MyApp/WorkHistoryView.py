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

#{"ProfileId": "1","ProjectName":"FujiFilm","Role":"Testing","Description":"I worked as a Test Engineer","City":"Hyd","Country":"India","StartMonth":"1","StartYear":"2016","EndMonth":"6","EndYear":"2019","CurrentlyWorking":"0","CompanyEmailId":"anilkumar5042001@gmail.com","CompanyId":"1"}
@csrf_exempt
@api_view(["POST"])
def WorkHistoryInsert(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strProfileId=loaded_json["ProfileId"]
        strProjectName=loaded_json["ProjectName"]
        strRole=loaded_json["Role"]
        strDescription=loaded_json["Description"]
        strCity=loaded_json["City"]
        strCountry=loaded_json["Country"]
        strStartMonth=loaded_json["StartMonth"]
        strStartYear=loaded_json["StartYear"]
        strEndMonth=loaded_json["EndMonth"]
        strEndYear=loaded_json["EndYear"]
        strCurrentlyWorking=loaded_json["CurrentlyWorking"]
        strCompanyEmailId=loaded_json["CompanyEmailId"]
        strCompanyId=loaded_json["CompanyId"]
        objWorkHistoryBAL=WorkHistoryBAL.WorkHistoryBAL()
        result=objWorkHistoryBAL.WorkHistoryInsert(strProfileId,strProjectName,strRole,strDescription,strCity,strCountry,strStartMonth,strStartYear,strEndMonth,strEndYear,strCurrentlyWorking,strCompanyEmailId,strCompanyId)
        return JsonResponse(result,safe=False)

#{"WorkHistoryId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetWorkHistoryById(json_data):
        loaded_json = json.loads(json_data.body)
        objWorkHistoryBAL=WorkHistoryBAL.WorkHistoryBAL()
        strWorkHistoryId=loaded_json["WorkHistoryId"]
        objWorkHistoryEntity=objWorkHistoryBAL.WorkHistoryGetById(strWorkHistoryId)
        result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"ProfileId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetWorkHistoryByProfileId(json_data):
        loaded_json = json.loads(json_data.body)
        objWorkHistoryBAL=WorkHistoryBAL.WorkHistoryBAL()
        strProfileId=loaded_json["ProfileId"]
        objWorkHistoryEntity=objWorkHistoryBAL.GetWorkHistoryByProfileId(strProfileId)
        result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"ProfileId": "1","CompanyId":"1"}
@csrf_exempt
@api_view(["POST"])
def GetWorkHistoryByProfileIdAndCompanyId(json_data):
        loaded_json = json.loads(json_data.body)
        objWorkHistoryBAL=WorkHistoryBAL.WorkHistoryBAL()
        strProfileId=loaded_json["ProfileId"]
        companyId=loaded_json["CompanyId"]
        objWorkHistoryEntity=objWorkHistoryBAL.GetWorkHistoryByProfileIdAndCompanyId(strProfileId,companyId)
        result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)


#{"ProfileId":"1","WorkHistoryId": "1","ProjectName":"RSM","Role": "SAP", "Description":"Changed my technology","City":"Banglore","Country":"India","StartMonth":"12","StartYear": "2015","EndMonth": "11","EndYear": "2018","CurrentlyWorking": "1","CompanyEmailId":"test123@google.com","CompanyId":"2"}
@csrf_exempt
@api_view(["POST"])
def WorkHistoryUpdate(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strProfileId=loaded_json["ProfileId"]
        strWorkHistoryId=loaded_json["WorkHistoryId"]
        strProjectName=loaded_json["ProjectName"]
        strRole=loaded_json["Role"]
        strDescription=loaded_json["Description"]
        strCity=loaded_json["City"]
        strCountry=loaded_json["Country"]
        strStartMonth=loaded_json["StartMonth"]
        strStartYear=loaded_json["StartYear"]
        strEndMonth=loaded_json["EndMonth"]
        strEndYear=loaded_json["EndYear"]
        strCurrentlyWorking=loaded_json["CurrentlyWorking"]
        strCompanyEmailId=loaded_json["CompanyEmailId"]
        strCompanyId=loaded_json["CompanyId"]
        objWorkHistoryBAL=WorkHistoryBAL.WorkHistoryBAL()
        result=objWorkHistoryBAL.WorkHistoryUpdate(strProfileId,strWorkHistoryId,strProjectName,strRole,strDescription,strCity,strCountry,strStartMonth,strStartYear,strEndMonth,strEndYear,strCurrentlyWorking,strCompanyEmailId,strCompanyId)
        return JsonResponse(result,safe=False)

#{"WorkHistoryId": "1"}
@csrf_exempt
@api_view(["POST"])
def WorkHistoryDelete(json_data):
        loaded_json = json.loads(json_data.body)
        objWorkHistoryBAL=WorkHistoryBAL.WorkHistoryBAL()
        strWorkHistoryId=loaded_json["WorkHistoryId"]
        objWorkHistoryEntity=objWorkHistoryBAL.WorkHistoryDelete(strWorkHistoryId)
        return JsonResponse("1",safe=False)

#{"WHGuid":"ABC1234","VerificationCode":"1234"}
@csrf_exempt
@api_view(["POST"])
def WorkHistoryUpdateVerificationCode(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strWHGuid=loaded_json["WHGuid"]
        strVerificationCode=loaded_json["VerificationCode"]      
        objWorkHistoryBAL=WorkHistoryBAL.WorkHistoryBAL()
        objWorkHistoryEntity=objWorkHistoryBAL.WorkHistoryUpdateVerificationCode(strWHGuid,strVerificationCode)
        result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"WorkHistoryId":"1","Description":"Worked hard in deadline"}
@csrf_exempt
@api_view(["POST"])
def ProjectHighlightsInsert(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strWorkHistoryId=loaded_json["WorkHistoryId"]
        strProjectHighlightsDescription=loaded_json["Description"]
        objWorkHistoryBAL=WorkHistoryBAL.WorkHistoryBAL()
        result=objWorkHistoryBAL.ProjectHighlightsInsert(strWorkHistoryId,strProjectHighlightsDescription)
        return JsonResponse("1",safe=False)

#{"WorkHistoryId": 1}
@csrf_exempt
@api_view(["POST"])
def GetProjectHighlightsById(json_data):
        loaded_json = json.loads(json_data.body)
        objWorkHistoryBAL=WorkHistoryBAL.WorkHistoryBAL()
        strWorkHistoryId=loaded_json["WorkHistoryId"]
        objProjectHighlightsEntity=objWorkHistoryBAL.ProjectHighlightsGetById(strWorkHistoryId)
        result = json.dumps([ob.__dict__ for ob in objProjectHighlightsEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"HighlightId": "1","WorkHistoryId":"1","Description":"Successfully finished the project on time"}
@csrf_exempt
@api_view(["POST"])
def ProjectHighlightsUpdate(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strHighlightId=loaded_json["HighlightId"]
        strWorkHistoryId=loaded_json["WorkHistoryId"]
        strProjectHighlightsDescription=loaded_json["Description"]
        objWorkHistoryBAL=WorkHistoryBAL.WorkHistoryBAL()
        result=objWorkHistoryBAL.ProjectHighlightsUpdate(strHighlightId,strWorkHistoryId,strProjectHighlightsDescription)
        return JsonResponse("1",safe=False)

#{"HighlightId": "1"}
@csrf_exempt
@api_view(["POST"])
def ProjectHighlightsDelete(json_data):
        loaded_json = json.loads(json_data.body)
        objWorkHistoryBAL=WorkHistoryBAL.WorkHistoryBAL()
        strHighlightId=loaded_json["HighlightId"]
        objWorkHistoryEntity=objWorkHistoryBAL.ProjectHighlightsDelete(strHighlightId)
        return JsonResponse("1",safe=False)

#{"WorkHistoryId": "1"}
@csrf_exempt
@api_view(["POST"])
def ProjectHighlightsDeleteByWorkHistoryId(json_data):
        loaded_json = json.loads(json_data.body)
        objWorkHistoryBAL=WorkHistoryBAL.WorkHistoryBAL()
        strWorkHistoryId=loaded_json["WorkHistoryId"]
        objWorkHistoryEntity=objWorkHistoryBAL.ProjectHighlightsDeleteByWorkHistoryId(strWorkHistoryId)
        return JsonResponse("1",safe=False)

#{"WorkHistoryId":"1","Description":"Worked as Team Lead"}
@csrf_exempt
@api_view(["POST"])
def ResponsibilitiesInsert(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strWorkHistoryId=loaded_json["WorkHistoryId"]
        strDescription=loaded_json["Description"]
        objWorkHistoryBAL=WorkHistoryBAL.WorkHistoryBAL()
        result=objWorkHistoryBAL.ResponsibilitiesInsert(strWorkHistoryId,strDescription)
        return JsonResponse("1",safe=False)

#{"WorkHistoryId": 1}
@csrf_exempt
@api_view(["POST"])
def GetResponsibilitiesById(json_data):
        loaded_json = json.loads(json_data.body)
        objWorkHistoryBAL=WorkHistoryBAL.WorkHistoryBAL()
        strWorkHistoryId=loaded_json["WorkHistoryId"]
        objResponsibilitiesEntity=objWorkHistoryBAL.ResponsibilitiesGetById(strWorkHistoryId)
        result = json.dumps([ob.__dict__ for ob in objResponsibilitiesEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"ResponsibilitiesId": "1","WorkHistoryId":"1","Description":"Started working as PM"}
@csrf_exempt
@api_view(["POST"])
def ResponsibilitiesUpdate(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strResponsibilitiesId=loaded_json["ResponsibilitiesId"]
        strWorkHistoryId=loaded_json["WorkHistoryId"]
        strResponsibilitiesDescription=loaded_json["Description"]
        objWorkHistoryBAL=WorkHistoryBAL.WorkHistoryBAL()
        result=objWorkHistoryBAL.ResponsibilitiesUpdate(strResponsibilitiesId,strWorkHistoryId,strResponsibilitiesDescription)
        return JsonResponse("1",safe=False)

#{"ResponsibilitiesId": "1"}
@csrf_exempt
@api_view(["POST"])
def ResponsibilitiesDelete(json_data):
        loaded_json = json.loads(json_data.body)
        objWorkHistoryBAL=WorkHistoryBAL.WorkHistoryBAL()
        strResponsibilitiesId=loaded_json["ResponsibilitiesId"]
        objWorkHistoryEntity=objWorkHistoryBAL.ResponsibilitiesDelete(strResponsibilitiesId)
        return JsonResponse("1",safe=False)

#{"WorkHistoryId": "1"}
@csrf_exempt
@api_view(["POST"])
def ResponsibilitiesDeleteByWorkHistoryId(json_data):
        loaded_json = json.loads(json_data.body)
        objWorkHistoryBAL=WorkHistoryBAL.WorkHistoryBAL()
        strWorkHistoryId=loaded_json["WorkHistoryId"]
        objWorkHistoryEntity=objWorkHistoryBAL.ResponsibilitiesDeleteByWorkHistoryId(strWorkHistoryId)
        return JsonResponse("1",safe=False)