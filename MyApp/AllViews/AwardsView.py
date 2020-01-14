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
from ..DBObjects.BAL import AwardsBAL
from ..DBObjects.Entity import AwardsEntity

#{"ProfileId": "1","AwardTitle":"Best Developer","AwardDescription":"worked as a member","AssignTo":"2"}
@csrf_exempt
@api_view(["POST"])
def AwardsInsert(json_data):
        loaded_json = json.loads(json_data.body)
        strProfileId=loaded_json["ProfileId"]
        strAwardTitle=loaded_json["AwardTitle"]
        strAwardDescription=loaded_json["AwardDescription"]
        strAssignTo=loaded_json["AssignTo"]
        objAwardsBAL=AwardsBAL.AwardsBAL()
        result=objAwardsBAL.AwardsInsert(strProfileId,strAwardTitle,strAwardDescription,strAssignTo)
        return JsonResponse("1",safe=False)

#{"ProfileId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetAwardsByProfileId(json_data):
        loaded_json = json.loads(json_data.body)
        objAwardsBAL=AwardsBAL.AwardsBAL()
        strProfileId=loaded_json["ProfileId"]
        objAwardsEntity=objAwardsBAL.GetAwardsByProfileId(strProfileId)
        result = json.dumps([ob.__dict__ for ob in objAwardsEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"AssignTo": "1"}
@csrf_exempt
@api_view(["POST"])
def GetAwardsByAssignTo(json_data):
        loaded_json = json.loads(json_data.body)
        objAwardsBAL=AwardsBAL.AwardsBAL()
        strAssignTo=loaded_json["AssignTo"]
        objAwardsEntity=objAwardsBAL.GetAwardsByAssignTo(strAssignTo)
        result = json.dumps([ob.__dict__ for ob in objAwardsEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"AwardId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetAwardsById(json_data):
        loaded_json = json.loads(json_data.body)
        objAwardsBAL=AwardsBAL.AwardsBAL()
        strAwardId=loaded_json["AwardId"]
        objAwardsEntity=objAwardsBAL.GetAwardsById(strAwardId)
        result = json.dumps([ob.__dict__ for ob in objAwardsEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"AssignTo": "1"}
@csrf_exempt
@api_view(["POST"])
def GetAwardsNew(json_data):
        loaded_json = json.loads(json_data.body)
        objAwardsBAL=AwardsBAL.AwardsBAL()
        strAssignTo=loaded_json["AssignTo"]
        objAwardsEntity=objAwardsBAL.GetAwardsNew(strAssignTo)
        result = json.dumps([ob.__dict__ for ob in objAwardsEntity])
        return JsonResponse(result,safe=False)


#{"AwardId":"2","ProfileId": "1","AwardTitle":"Gujarathi","AwardDescription":"Low","AssignTo":"1"}
@csrf_exempt
@api_view(["POST"])
def AwardsUpdate(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strAwardId=loaded_json["AwardId"]
        strProfileId=loaded_json["ProfileId"]
        strAwardTitle=loaded_json["AwardTitle"]
        strAwardDescription=loaded_json["AwardDescription"]
        objAwardsBAL=AwardsBAL.AwardsBAL()
        result=objAwardsBAL.AwardsUpdate(strAwardId,strProfileId,strAwardTitle,strAwardDescription)
        return JsonResponse("1",safe=False)

#{"AwardId":"1","ShowInProfile": "1"}
@csrf_exempt
@api_view(["POST"])
def AwardsUpdateShowInProfile(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strAwardId=loaded_json["AwardId"]
        strShowInProfile=loaded_json["ShowInProfile"]
        objAwardsBAL=AwardsBAL.AwardsBAL()
        result=objAwardsBAL.AwardsUpdateShowInProfile(strAwardId,strShowInProfile)
        return JsonResponse("1",safe=False)


#{"ProfileId":"1"}
@csrf_exempt
@api_view(["POST"])
def AwardsUpdateIsNew(json_data):
        loaded_json = json.loads(json_data.body)
        strProfileId=loaded_json["ProfileId"]
        objAwardsBAL=AwardsBAL.AwardsBAL()
        result=objAwardsBAL.AwardsUpdateIsNew(strProfileId)
        return JsonResponse("1",safe=False)

#{"AwardId": "1"}
@csrf_exempt
@api_view(["POST"])
def AwardsDelete(json_data):
        loaded_json = json.loads(json_data.body)
        objAwardsBAL=AwardsBAL.AwardsBAL()
        strAwardId=loaded_json["AwardId"]
        objAwardsEntity=objAwardsBAL.AwardsDelete(strAwardId)
        return JsonResponse("1",safe=False)

      

