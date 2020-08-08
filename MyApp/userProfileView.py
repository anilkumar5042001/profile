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
from .DBObjects.BAL import ProjectsBAL
from .DBObjects.Entity import ProjectEntity

#{"ProfileId": 1}
@csrf_exempt
@api_view(["POST"])
def GetUserProfileAboutMeById(json_data):
        loaded_json = json.loads(json_data.body)
        objUserProfileBAL=UserProfileBAL.UserProfileBAL()
        profileId=loaded_json["ProfileId"]
        objUserProfileEntity=objUserProfileBAL.GetUserProfileById(profileId)
        result= json.dumps(objUserProfileEntity.__dict__)
        return JsonResponse(result,safe=False) 

#{"ProfileId":"1","FirstName": "Test", "LastName": "Three", "EmailId":"testthree@gmail.com","PhoneNumber":"0","Education":"JNTU","Designation":"Software Engg"}
@csrf_exempt
@api_view(["POST"])
def UserProfileUpdateAboutMe(json_data):
        loaded_json = json.loads(json_data.body)
        strProfileId=loaded_json["ProfileId"]
        strAboutMe=loaded_json["AboutMe"]
        objUserProfileBAL=UserProfileBAL.UserProfileBAL()
        result=objUserProfileBAL.UserProfileUpdateAboutMe(strProfileId,strAboutMe)
        return JsonResponse("1",safe=False)

@csrf_exempt
@api_view(["POST"])
def UserProfileGetAll(json_data):
        # loaded_json = json.loads(json_data.body)
        objUserProfileBAL=UserProfileBAL.UserProfileBAL()
        objUserProfileEntity=objUserProfileBAL.UserProfileGetAll()
        result = json.dumps([ob.__dict__ for ob in objUserProfileEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)