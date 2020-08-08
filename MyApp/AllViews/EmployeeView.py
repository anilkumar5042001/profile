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
from ..DBObjects.BAL import EmployeeBAL
from ..DBObjects.Entity import InterestEntity

# #{"ProfileId": "1","InterestName":"Interest in c,c++"}
# @csrf_exempt
# @api_view(["POST"])
# def EmployeeInsert(json_data):
#         loaded_json = json.loads(json_data.body)
#         strEmployeeFileName=loaded_json["EmployeeFileName"]
#         objEmployeeBAL=EmployeeBAL.EmployeeBAL()
#         result=objEmployeeBAL.InsertEmployee(strEmployeeFileName)
#         return JsonResponse("1",safe=False)

#{"ProfileId": "1","ManagerId":"1","RoleId": "1","HrId": "1","EUID":"avdrf233"}
@csrf_exempt
@api_view(["POST"])
def EmployeeInsert(json_data):
        loaded_json = json.loads(json_data.body)
        strProfileId=loaded_json["ProfileId"]
        strManagerId=loaded_json["ManagerId"]
        strRoleId=loaded_json["RoleId"]
        strHrId=loaded_json["HrId"]
        strEUID=loaded_json["EUID"]
        objEmployeeBAL=EmployeeBAL.EmployeeBAL()
        result=objEmployeeBAL.EmployeeInsert(strProfileId,strManagerId,strRoleId,strHrId,strEUID)
        return JsonResponse(result,safe=False)

#{"ProfileId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetEmployeeByProfileId(json_data):
        loaded_json = json.loads(json_data.body)
        objEmployeeBAL=EmployeeBAL.EmployeeBAL()
        strProfileId=loaded_json["ProfileId"]
        objEmployeeEntity=objEmployeeBAL.GetEmployeeByProfileId(strProfileId)
        result = json.dumps([ob.__dict__ for ob in objEmployeeEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"EmployeeId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetEmployeeByEmployeeId(json_data):
        loaded_json = json.loads(json_data.body)
        objEmployeeBAL=EmployeeBAL.EmployeeBAL()
        strEmployeeId=loaded_json["EmployeeId"]
        objEmployeeEntity=objEmployeeBAL.GetEmployeeByEmployeeId(strEmployeeId)
        result = json.dumps([ob.__dict__ for ob in objEmployeeEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"ManagerId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetEmployeeByManagerId(json_data):
        loaded_json = json.loads(json_data.body)
        objEmployeeBAL=EmployeeBAL.EmployeeBAL()
        strManagerId=loaded_json["ManagerId"]
        objEmployeeEntity=objEmployeeBAL.GetEmployeeByManagerId(strManagerId)
        result = json.dumps([ob.__dict__ for ob in objEmployeeEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)
    
    #{"ProfileId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetEmployeeByRoleId(json_data):
        loaded_json = json.loads(json_data.body)
        objEmployeeBAL=EmployeeBAL.EmployeeBAL()
        strRoleId=loaded_json["RoleId"]
        objEmployeeEntity=objEmployeeBAL.GetEmployeeByRoleId(strRoleId)
        result = json.dumps([ob.__dict__ for ob in objEmployeeEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

    #{"ProfileId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetEmployeeByHrId(json_data):
        loaded_json = json.loads(json_data.body)
        objEmployeeBAL=EmployeeBAL.EmployeeBAL()
        strHrId=loaded_json["HrId"]
        objEmployeeEntity=objEmployeeBAL.GetEmployeeByHrId(strHrId)
        result = json.dumps([ob.__dict__ for ob in objEmployeeEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

@csrf_exempt
@api_view(["POST"])
def EmployeeGetAll(json_data):
        # loaded_json = json.loads(json_data.body)
        objEmployeeBAL=EmployeeBAL.EmployeeBAL()
        objEmployeeEntity=objEmployeeBAL.EmployeeGetAll()
        result = json.dumps([ob.__dict__ for ob in objEmployeeEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"EmployeeId":"1","ProfileId": "1","ManagerId":"1","RoleId": "3","HrId": "4","EUID":"abcd5678"}
@csrf_exempt
@api_view(["POST"])
def EmployeeUpdate(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strEmployeeId=loaded_json["EmployeeId"]
        strProfileId=loaded_json["ProfileId"]
        strManagerId=loaded_json["ManagerId"]
        strRoleId=loaded_json["RoleId"]
        strHrId=loaded_json["HrId"]    
        strEUID=loaded_json["EUID"]   
        objEmployeeBAL=EmployeeBAL.EmployeeBAL()
        result=objEmployeeBAL.EmployeeUpdate(strEmployeeId,strProfileId,strManagerId,strRoleId,strHrId,strEUID)
        return JsonResponse("1",safe=False)

#{"FavouriteId": "1"}
@csrf_exempt
@api_view(["POST"])
def EmployeeDelete(json_data):
        loaded_json = json.loads(json_data.body)
        objEmployeeBAL=EmployeeBAL.EmployeeBAL()
        strEmployeeId=loaded_json["EmployeeId"]
        objEmployeeEntity=objEmployeeBAL.EmployeeDelete(strEmployeeId)
        return JsonResponse("1",safe=False)
