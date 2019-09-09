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
from .DBObjects.BAL import EducationBAL
from .DBObjects.Entity import EducationEntity

#{"EducationId":"1","ProfileId": "1","NameOfInstitution":"St.Xaviers High School","CourseName":"10th Standard","StartYear":"1995","EndYear":"1996"}
@csrf_exempt
@api_view(["POST"])
def EducationInsert(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strEducationId=loaded_json["EducationId"]
        strProfileId=loaded_json["ProfileId"]
        strNameOfInstitution=loaded_json["NameOfInstitution"]
        strCourseName=loaded_json["CourseName"]
        strStartYear=loaded_json["StartYear"]
        strEndYear=loaded_json["EndYear"]
        objEducationBAL=EducationBAL.EducationBAL()
        result=objEducationBAL.EducationInsert(strEducationId,strProfileId,strNameOfInstitution,strCourseName,strStartYear,strEndYear)
        return JsonResponse("1",safe=False)