from django.shortcuts import render
from django.http import Http404
from django.http import JsonResponse
from django.conf import settings
import json
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from ..DBScripts.MySqlTable import MySqlTable
from ..DBScripts.ExecOrder import ExecOrder
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..DBObjects.BAL import RegistrationBAL
from ..DBObjects.Entity import RegistrationEntity

#{"EmailId":"test@gmail.com","Password":"Test123"}
@csrf_exempt
@api_view(["POST"])
def RegistrationInsert(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strEmailId=loaded_json["EmailId"]
        strPassword=loaded_json["Password"]
        objRegistrationBAL=RegistrationBAL.RegistrationBAL()
        result=objRegistrationBAL.RegistrationInsert(strEmailId,strPassword)
        return JsonResponse(result,safe=False)

#{"RegistrationId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetRegistrationById(json_data):
        loaded_json = json.loads(json_data.body)
        objRegistrationBAL=RegistrationBAL.RegistrationBAL()
        strRegistrationId=loaded_json["RegistrationId"]
        objRegistrationEntity=objRegistrationBAL.GetRegistrationById(strRegistrationId)
        result = json.dumps([ob.__dict__ for ob in objRegistrationEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"RegistrationId": "1","EmailId":"test@google.com","Password":"test@456"}
@csrf_exempt
@api_view(["POST"])
def RegistrationUpdate(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strRegistrationId=loaded_json["RegistrationId"]
        strEmailId=loaded_json["EmailId"]
        strPassword=loaded_json["Password"]
        objRegistrationBAL=RegistrationBAL.RegistrationBAL()
        result=objRegistrationBAL.RegistrationUpdate(strRegistrationId,strEmailId,strPassword)
        return JsonResponse("1",safe=False)

      