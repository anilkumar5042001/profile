from django.shortcuts import render
from django.http import Http404
from django.http import JsonResponse
from django.conf import settings
import json
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from ..DBScripts.MySqlTable import MySqlTable
from ..DBScripts.ExecOrder import ExecOrder
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..DBObjects.BAL import EventsBAL
from ..DBObjects.Entity import EventsEntity
from ..CommonMethods import CommonMethods


#{"ProfileId": "1","EventCategoryId":"1","EventName": "Sankranthi","Description": "Farmers festival"}
@csrf_exempt
@api_view(["POST"])
def EventInsert(json_data):
        loaded_json = json.loads(json_data.body)
        strProfileId=loaded_json["ProfileId"]
        strEventCategoryId=loaded_json["EventCategoryId"]
        strEventName=loaded_json["EventName"]
        strDescription=loaded_json["Description"]    
        objEventBAL=EventsBAL.EventBAL()
        result=objEventBAL.EventInsert(strProfileId,strEventCategoryId,strEventName,strDescription)
        return JsonResponse(result,safe=False)

#{"ProfileId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetEventByProfileId(json_data):
        loaded_json = json.loads(json_data.body)
        objEventBAL=EventsBAL.EventBAL()
        strProfileId=loaded_json["ProfileId"]
        objEventEntity=objEventBAL.GetEventByProfileId(strProfileId)
        result = json.dumps([ob.__dict__ for ob in objEventEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"EventId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetEventById(json_data):
        loaded_json = json.loads(json_data.body)
        objEventBAL=EventsBAL.EventBAL()
        strEventId=loaded_json["EventId"]
        objEventEntity=objEventBAL.GetEventById(strEventId)
        result = json.dumps([ob.__dict__ for ob in objEventEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"EventId":"1","ProfileId": "1","EventCategoryId":"1","EventName": "Ugadhi","Description": "Telugu New Year"}
@csrf_exempt
@api_view(["POST"])
def EventUpdate(json_data):
        loaded_json = json.loads(json_data.body)
        strEventId=loaded_json["EventId"]
        strProfileId=loaded_json["ProfileId"]
        strEventCategoryId=loaded_json["EventCategoryId"]
        strEventName=loaded_json["EventName"]
        strDescription=loaded_json["Description"]        
        objEventBAL=EventsBAL.EventBAL()
        result=objEventBAL.EventUpdate(strEventId,strProfileId,strEventCategoryId,strEventName,strDescription)
        return JsonResponse("1",safe=False)

#{"EventId": "1"}
@csrf_exempt
@api_view(["POST"])
def EventDelete(json_data):
        loaded_json = json.loads(json_data.body)
        objEventBAL=EventsBAL.EventBAL()
        strEventId=loaded_json["EventId"]
        objEventEntity=objEventBAL.EventDelete(strEventId)
        return JsonResponse("1",safe=False)

      

