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