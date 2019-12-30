# from django.shortcuts import render
# from django.http import Http404
# from django.http import JsonResponse
# from django.conf import settings
# import json
# from django.views.decorators.csrf import csrf_exempt
# from django.core import serializers
# from ..DBScripts.MySqlTable import MySqlTable
# from ..DBScripts.ExecOrder import ExecOrder
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from ..DBObjects.BAL import EventBAL
# from ..DBObjects.Entity import EventEntity

# #{"ProfileId": "1","PassionName": "Movie","Description": "VenkyMama"}
# @csrf_exempt
# @api_view(["POST"])
# def EventInsert(json_data):
#         loaded_json = json.loads(json_data.body)
#         strProfileId=loaded_json["ProfileId"]
#         strEventName=loaded_json["EventName"]
#         strDescription=loaded_json["Description"]
#         strEventCategoryId=loaded_json["EventCategoryId"]
#         obj EventBAL=EventBAL.EventBAL()
#         result=objEventBAL.EventInsert(strProfileId,EventCategoryId,strEventName,strDescription)
#         return JsonResponse("1",safe=False)

# #{"ProfileId": "1"}
# @csrf_exempt
# @api_view(["POST"])
# def GetEventByProfileId(json_data):
#         loaded_json = json.loads(json_data.body)
#         objEventBAL=EventBAL.EventBAL()
#         strProfileId=loaded_json["ProfileId"]
#         objEventEntity=objEventBAL.GetEventByProfileId(strProfileId)
#         result = json.dumps([ob.__dict__ for ob in objEventEntity])
#         # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

#         #result= json.dumps(objWorkHistoryEntity.__dict__)
#         return JsonResponse(result,safe=False)

# #{"StoryId": "1"}
# @csrf_exempt
# @api_view(["POST"])
# def GetEventById(json_data):
#         loaded_json = json.loads(json_data.body)
#         objEventBAL=EventBAL.EventBAL()
#         strEventId=loaded_json["EventId"]
#         objEventEntity=objEventBAL.GetEventById(strEventId)
#         result = json.dumps([ob.__dict__ for ob in objEventEntity])
#         # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

#         #result= json.dumps(objWorkHistoryEntity.__dict__)
#         return JsonResponse(result,safe=False)

# @csrf_exempt
# @api_view(["POST"])
# def EventUpdate(json_data):
#         loaded_json = json.loads(json_data.body)
#         strProfileId=loaded_json["ProfileId"]
#         strEventName=loaded_json["EventName"]
#         strDescription=loaded_json["Description"]
#         strEventCategoryId=loaded_json["EventCategoryId"]
#         obj EventBAL=EventBAL.EventBAL()
#         result=objEventBAL.EventInsert(strProfileId,EventCategoryId,strEventName,strDescription)
#         return JsonResponse("1",safe=False)
# #{"StoryId": "1"}
# @csrf_exempt
# @api_view(["POST"])
# def EventDelete(json_data):
#         loaded_json = json.loads(json_data.body)
#         objEventBAL=EventBAL.EventBAL()
#         strStoryId=loaded_json["EventId"]
#         objEventEntity=objEventBAL.EventDelete(strEventId)
#         return JsonResponse("1",safe=False)

      

