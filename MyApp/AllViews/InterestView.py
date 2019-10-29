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
from ..DBObjects.BAL import InterestBAL
from ..DBObjects.Entity import InterestEntity

#{"ProfileId": "1","InterestName":"Interest in c,c++"}
@csrf_exempt
@api_view(["POST"])
def InterestInsert(json_data):
        loaded_json = json.loads(json_data.body)
        strProfileId=loaded_json["ProfileId"]
        strInterestName=loaded_json["InterestName"]
        objInterestBAL=InterestBAL.InterestBAL()
        result=objInterestBAL.InterestInsert(strProfileId,strInterestName)
        return JsonResponse("1",safe=False)

#{"ProfileId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetInterestByProfileId(json_data):
        loaded_json = json.loads(json_data.body)
        objInterestBAL=InterestBAL.InterestBAL()
        strProfileId=loaded_json["ProfileId"]
        objInterestEntity=objInterestBAL.GetInterestByProfileId(strProfileId)
        result = json.dumps([ob.__dict__ for ob in objInterestEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"InterestId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetInterestById(json_data):
        loaded_json = json.loads(json_data.body)
        objInterestBAL=InterestBAL.InterestBAL()
        strInterestId=loaded_json["InterestId"]
        objInterestEntity=objInterestBAL.GetInterestById(strInterestId)
        result = json.dumps([ob.__dict__ for ob in objInterestEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"InterestId":"1","ProfileId": "1","InterestName":".net"}
@csrf_exempt
@api_view(["POST"])
def InterestUpdate(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strInterestId=loaded_json["InterestId"]
        strProfileId=loaded_json["ProfileId"]
        strInterestName=loaded_json["InterestName"]
        objInterestBAL=InterestBAL.InterestBAL()
        result=objInterestBAL.InterestUpdate(strInterestId,strProfileId,strInterestName)
        return JsonResponse("1",safe=False)

#{"InterestId": "1"}
@csrf_exempt
@api_view(["POST"])
def InterestDelete(json_data):
        loaded_json = json.loads(json_data.body)
        objInterestBAL=InterestBAL.InterestBAL()
        strInterestId=loaded_json["InterestId"]
        objInterestEntity=objInterestBAL.InterestDelete(strInterestId)
        return JsonResponse("1",safe=False)
