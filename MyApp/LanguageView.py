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
from .DBObjects.BAL import LanguageBAL
from .DBObjects.Entity import LanguageEntity

#{"ProfileId": "1","LanguageName":"Telugu","LanguageLevel":"High"}
@csrf_exempt
@api_view(["POST"])
def LanguageInsert(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strProfileId=loaded_json["ProfileId"]
        strLanguageName=loaded_json["LanguageName"]
        strLanguageLevel=loaded_json["LanguageLevel"]
        objLanguageBAL=LanguageBAL.LanguageBAL()
        result=objLanguageBAL.LanguageInsert(strProfileId,strLanguageName,strLanguageLevel)
        return JsonResponse("1",safe=False)

#{"ProfileId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetLanguageByProfileId(json_data):
        loaded_json = json.loads(json_data.body)
        objLanguageBAL=LanguageBAL.LanguageBAL()
        strProfileId=loaded_json["ProfileId"]
        objLanguageEntity=objLanguageBAL.GetLanguageByProfileId(strProfileId)
        result = json.dumps([ob.__dict__ for ob in objLanguageEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"LanguageId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetLanguageById(json_data):
        loaded_json = json.loads(json_data.body)
        objLanguageBAL=LanguageBAL.LanguageBAL()
        strLanguageId=loaded_json["LanguageId"]
        objLanguageEntity=objLanguageBAL.GetLanguageById(strLanguageId)
        result = json.dumps([ob.__dict__ for ob in objLanguageEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"LanguageId":"2","ProfileId": "1","LanguageName":"Gujarathi","LanguageLevel":"Low"}
@csrf_exempt
@api_view(["POST"])
def LanguageUpdate(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strLanguageId=loaded_json["LanguageId"]
        strProfileId=loaded_json["ProfileId"]
        strLanguageName=loaded_json["LanguageName"]
        strLanguageLevel=loaded_json["LanguageLevel"]
        objLanguageBAL=LanguageBAL.LanguageBAL()
        result=objLanguageBAL.LanguageUpdate(strLanguageId,strProfileId,strLanguageName,strLanguageLevel)
        return JsonResponse("1",safe=False)

#{"LanguageId": "1"}
@csrf_exempt
@api_view(["POST"])
def LanguageDelete(json_data):
        loaded_json = json.loads(json_data.body)
        objLanguageBAL=LanguageBAL.LanguageBAL()
        strLanguageId=loaded_json["LanguageId"]
        objLanguageEntity=objLanguageBAL.LanguageDelete(strLanguageId)
        return JsonResponse("1",safe=False)

      