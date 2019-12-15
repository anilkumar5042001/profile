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
from ..DBObjects.BAL import SkillsBAL
from ..DBObjects.Entity import SkillsEntity

#{"ProfileId": "1",SkillCategoryId":"1"SkillName":".Net"}
@csrf_exempt
@api_view(["POST"])
def SkillsInsert(json_data):
        loaded_json = json.loads(json_data.body)
        strProfileId=loaded_json["ProfileId"]
        strSkillCategoryId=loaded_json["SkillCategoryId"]
        strSkillName=loaded_json["SkillName"]
        objSkillsBAL=SkillsBAL.SkillsBAL()
        result=objSkillsBAL.SkillsInsert(strProfileId,strSkillCategoryId,strSkillName)
        return JsonResponse(result,safe=False)

#{"ProfileId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetSkillsByProfileId(json_data):
        loaded_json = json.loads(json_data.body)
        strProfileId=loaded_json["ProfileId"]
        objSkillsBAL=SkillsBAL.SkillsBAL()
        objSkillsEntity=objSkillsBAL.GetSkillsByProfileId(strProfileId)
        result = json.dumps([ob.__dict__ for ob in objSkillsEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"SkillId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetSkillsById(json_data):
        loaded_json = json.loads(json_data.body)
        strSkillId=loaded_json["SkillId"]  
        objSkillsBAL=SkillsBAL.SkillsBAL()      
        objSkillsEntity=objSkillsBAL.GetSkillsById(strSkillId)
        result = json.dumps([ob.__dict__ for ob in objSkillsEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"SkillId":"1","SkillCategoryId":"2","ProfileId": "1","SkillName":"Python"}
@csrf_exempt
@api_view(["POST"])
def SkillsUpdate(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strSkillId=loaded_json["SkillId"]
        strSkillCategoryId=loaded_json["SkillCategoryId"]
        strProfileId=loaded_json["ProfileId"]
        strSkillName=loaded_json["SkillName"]
        objSkillsBAL=SkillsBAL.SkillsBAL()
        result=objSkillsBAL.SkillsUpdate(strSkillId,strProfileId,strSkillCategoryId,strSkillName)
        return JsonResponse("1",safe=False)

#{"SkillId": "1"}
@csrf_exempt
@api_view(["POST"])
def SkillsDelete(json_data):
        loaded_json = json.loads(json_data.body)
        objSkillsBAL=SkillsBAL.SkillsBAL()
        strSkillId=loaded_json["SkillId"]
        objSkillsEntity=objSkillsBAL.SkillsDelete(strSkillId)
        return JsonResponse("1",safe=False)

      

