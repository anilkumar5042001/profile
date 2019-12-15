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
from ..DBObjects.BAL import SkillCategoryBAL
from ..DBObjects.Entity import SkillCategoryEntity

#{"ProfileId": "1","SkillCategoryName":"Best Developer"}
@csrf_exempt
@api_view(["POST"])
def SkillsCategoryInsert(json_data):
        loaded_json = json.loads(json_data.body)
        strProfileId=loaded_json["ProfileId"]
        strSkillCategoryName=loaded_json["SkillCategoryName"]
        objSkillCategoryBAL=SkillCategoryBAL.SkillCategoryBAL()
        result=objSkillCategoryBAL.SkillsCategoryInsert(strProfileId,strSkillCategoryName)
        return JsonResponse(result,safe=False)

#{"ProfileId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetSkillCategoryNameByProfileId(json_data):
        loaded_json = json.loads(json_data.body)
        strProfileId=loaded_json["ProfileId"]
        objSkillCategoryBAL=SkillCategoryBAL.SkillCategoryBAL()
        objSkillCategoryEntity=objSkillCategoryBAL.GetSkillsCategoryByProfileId(strProfileId)
        result = json.dumps([ob.__dict__ for ob in objSkillCategoryEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"SkillCategoryId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetSkillsCategoryById(json_data):
        loaded_json = json.loads(json_data.body)
        strSkillCategoryId=loaded_json["SkillCategoryId"]  
        objSkillCategoryBAL=SkillCategoryBAL.SkillCategoryBAL()      
        objSkillCategoryEntity=objSkillCategoryBAL.GetSkillsCategoryById(strSkillCategoryId)
        result = json.dumps([ob.__dict__ for ob in objSkillCategoryEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"SkillCategoryId":"2","ProfileId": "1","SkillCategoryName":"Best Developer"}
@csrf_exempt
@api_view(["POST"])
def SkillsCategoryUpdate(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strSkillCategoryId=loaded_json["SkillCategoryId"]
        strProfileId=loaded_json["ProfileId"]
        strSkillCategoryName=loaded_json["SkillCategoryName"]
        objSkillCategoryBAL=SkillCategoryBAL.SkillCategoryBAL()
        result=objSkillCategoryBAL.SkillsCategoryUpdate(strSkillCategoryId,strProfileId,strSkillCategoryName)
        return JsonResponse("1",safe=False)

#{"SkillCategoryId": "1"}
@csrf_exempt
@api_view(["POST"])
def SkillsCategoryDelete(json_data):
        loaded_json = json.loads(json_data.body)
        objSkillCategoryBAL=SkillCategoryBAL.SkillCategoryBAL()
        strSkillCategoryId=loaded_json["SkillCategoryId"]
        objSkillCategoryEntity=objSkillCategoryBAL.SkillsCategoryDelete(strSkillCategoryId)
        return JsonResponse("1",safe=False)

      

