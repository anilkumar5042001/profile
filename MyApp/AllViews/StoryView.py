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
from ..DBObjects.BAL import StoryBAL
from ..DBObjects.Entity import StoryEntity

#{"ProfileId": "1","StoryCategoryId":"1","StoryTitle": "Test","Description": "VenkyMama","Thumbnail":"testOne.jpg","IsPublished":"0"}
@csrf_exempt
@api_view(["POST"])
def StoryInsert(json_data):
        loaded_json = json.loads(json_data.body)
        strProfileId=loaded_json["ProfileId"]
        strStoryTitle=loaded_json["StoryTitle"]
        strStoryCategoryId=loaded_json["StoryCategoryId"]
        strDescription=loaded_json["Description"]
        strThumbnail=loaded_json["Thumbnail"]
        strIsPublished=loaded_json["IsPublished"]       
        objStoryBAL=StoryBAL.StoryBAL()
        result=objStoryBAL.StoryInsert(strProfileId,strStoryCategoryId,strStoryTitle,strDescription,strThumbnail,strIsPublished)
        return JsonResponse(result,safe=False)

#{"ProfileId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetStoryByProfileId(json_data):
        loaded_json = json.loads(json_data.body)
        objStoryBAL=StoryBAL.StoryBAL()
        strProfileId=loaded_json["ProfileId"]
        objStoryEntity=objStoryBAL.GetStoryByProfileId(strProfileId)
        result = json.dumps([ob.__dict__ for ob in objStoryEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"StoryId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetStoryById(json_data):
        loaded_json = json.loads(json_data.body)
        objStoryBAL=StoryBAL.StoryBAL()
        strStoryId=loaded_json["StoryId"]
        objStoryEntity=objStoryBAL.GetStoryById(strStoryId)
        result = json.dumps([ob.__dict__ for ob in objStoryEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

# {"ProfileId": "1","StoryCategoryId":"2","StoryTitle": "TestStoryTitle","Description": "TestStoryDescription","Thumbnail":"testTwo.jpg","IsPublished":"1"}
@csrf_exempt
@api_view(["POST"])
def StoryUpdate(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strStoryId=loaded_json["StoryId"]
        strProfileId=loaded_json["ProfileId"]
        strStoryCategoryId=loaded_json["StoryCategoryId"]
        strStoryTitle=loaded_json["StoryTitle"]       
        strDescription=loaded_json["Description"]
        strThumbnail=loaded_json["Thumbnail"]
        strIsPublished=loaded_json["IsPublished"]        
        objStoryBAL=StoryBAL.StoryBAL()
        result=objStoryBAL.StoryUpdate(strStoryId,strProfileId,strStoryCategoryId,strStoryTitle,strDescription,strThumbnail,strIsPublished)
        return JsonResponse("1",safe=False)

#{"StoryId": "1"}
@csrf_exempt
@api_view(["POST"])
def StoryDelete(json_data):
        loaded_json = json.loads(json_data.body)
        objStoryBAL=StoryBAL.StoryBAL()
        strStoryId=loaded_json["StoryId"]
        objStoryEntity=objStoryBAL.StoryDelete(strStoryId)
        return JsonResponse("1",safe=False)

      

