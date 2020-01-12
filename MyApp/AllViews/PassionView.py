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
from ..DBObjects.BAL import PassionBAL
from ..DBObjects.Entity import PassionEntity

#{"ProfileId": "1","PassionName": "to become data science","Description": "want to learn DataScience"}
@csrf_exempt
@api_view(["POST"])
def PassionInsert(json_data):
        loaded_json = json.loads(json_data.body)
        strProfileId=loaded_json["ProfileId"]
        strPassionName=loaded_json["PassionName"]
        strDescription=loaded_json["Description"]
        objPassionBAL=PassionBAL.PassionBAL()
        result=objPassionBAL.PassionInsert(strProfileId,strPassionName,strDescription)
        return JsonResponse(result,safe=False)

#{"ProfileId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetPassionByProfileId(json_data):
        loaded_json = json.loads(json_data.body)
        objPassionBAL=PassionBAL.PassionBAL()
        strProfileId=loaded_json["ProfileId"]
        objPassionEntity=objPassionBAL.GetPassionByProfileId(strProfileId)
        result = json.dumps([ob.__dict__ for ob in objPassionEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"PassionId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetPassionById(json_data):
        loaded_json = json.loads(json_data.body)
        objPassionBAL=PassionBAL.PassionBAL()
        strPassionId=loaded_json["PassionId"]
        objPassionEntity=objPassionBAL.GetPassionById(strPassionId)
        result = json.dumps([ob.__dict__ for ob in objPassionEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"PassionId":"1","ProfileId": "1","PassionName": "to become AI developer","Description": "want to learn AI"}
@csrf_exempt
@api_view(["POST"])
def PassionUpdate(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strPassionId=loaded_json["PassionId"]
        strProfileId=loaded_json["ProfileId"]
        strPassionName=loaded_json["PassionName"]
        strDescription=loaded_json["Description"]
        objPassionBAL=PassionBAL.PassionBAL()
        result=objPassionBAL.PassionUpdate(strPassionId,strProfileId,strPassionName,strDescription)
        return JsonResponse("1",safe=False)

#{"PassionId": "1"}
@csrf_exempt
@api_view(["POST"])
def PassionDelete(json_data):
        loaded_json = json.loads(json_data.body)
        objPassionBAL=PassionBAL.PassionBAL()
        strPassionId=loaded_json["PassionId"]
        objPassionEntity=objPassionBAL.PassionDelete(strPassionId)
        return JsonResponse("1",safe=False)

      

