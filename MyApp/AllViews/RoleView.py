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
from ..DBObjects.BAL import RoleBAL
from ..DBObjects.Entity import RoleEntity

#{"ProfileId":"1","RoleName":"Test1"}
@csrf_exempt
@api_view(["POST"])
def RoleInsert(json_data):
        loaded_json = json.loads(json_data.body)
        strProfileId=loaded_json["ProfileId"]
        strRoleName=loaded_json["RoleName"]
        objRoleBAL=RoleBAL.RoleBAL()
        result=objRoleBAL.RoleInsert(strProfileId,strRoleName)
        return JsonResponse(result,safe=False)

#{"ProfileId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetRoleByProfileId(json_data):
        loaded_json = json.loads(json_data.body)
        objRoleBAL=RoleBAL.RoleBAL()
        strProfileId=loaded_json["ProfileId"]
        objRoleEntity=objRoleBAL.GetRoleByProfileId(strProfileId)
        result = json.dumps([ob.__dict__ for ob in objRoleEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"RoleId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetRoleByRoleId(json_data):
        loaded_json = json.loads(json_data.body)
        objRoleBAL=RoleBAL.RoleBAL()
        strRoleId=loaded_json["RoleId"]
        objRoleEntity=objRoleBAL.GetRoleByRoleId(strRoleId)
        result = json.dumps([ob.__dict__ for ob in objRoleEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"RoleId":"1","ProfileId": "1","RoleName":"Test2"}
@csrf_exempt
@api_view(["POST"])
def RoleUpdate(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strRoleId=loaded_json["RoleId"]
        strProfileId=loaded_json["ProfileId"]
        strRoleName=loaded_json["RoleName"]
        objRoleBAL=RoleBAL.RoleBAL()
        result=objRoleBAL.RoleUpdate(strRoleId,strProfileId,strRoleName)
        return JsonResponse("1",safe=False)

#{"RoleId": "1"}
@csrf_exempt
@api_view(["POST"])
def RoleDelete(json_data):
        loaded_json = json.loads(json_data.body)
        objRoleBAL=RoleBAL.RoleBAL()
        strRoleId=loaded_json["RoleId"]
        objRoleEntity=objRoleBAL.RoleDelete(strRoleId)
        return JsonResponse("1",safe=False)

      

