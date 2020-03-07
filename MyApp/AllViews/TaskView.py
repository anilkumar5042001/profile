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
from ..DBObjects.BAL import TaskBAL
from ..DBObjects.Entity import TaskEntity
from ..CommonMethods import CommonMethods


#{"ProfileId":"1","TaskTitle":"Test123","Description":"TestDescription","DueDate":"2019-11-12","AssignTo":"2","CreatedBy":"1","TaskStatus":"Open","TaskDuration":"1"}
@csrf_exempt
@api_view(["POST"])
def TaskInsert(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strProfileId=loaded_json["ProfileId"]
        strTaskTitle=loaded_json["TaskTitle"]
        strDescription=loaded_json["Description"]
        strDueDate=loaded_json["DueDate"]
        strAssignTo=loaded_json["AssignTo"]
        strCreatedBy=loaded_json["CreatedBy"]
        strTaskStatus=loaded_json["TaskStatus"]
        strTaskDuration=loaded_json["TaskDuration"]
        objTaskBAL=TaskBAL.TaskBAL()
        result=objTaskBAL.TaskInsert(strProfileId,strTaskTitle,strDescription,strDueDate,strAssignTo,strCreatedBy,strTaskStatus,strTaskDuration)
        return JsonResponse(result,safe=False)

#{"TaskId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetTaskByTaskId(json_data):
        loaded_json = json.loads(json_data.body)
        objTaskBAL=TaskBAL.TaskBAL()    
        strTaskId=loaded_json["TaskId"]    
        objTaskEntity=objTaskBAL.GetTaskByTaskId(strTaskId)
        result = json.dumps([ob.__dict__ for ob in objTaskEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"ProfileId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetTaskByProfileId(json_data):
        loaded_json = json.loads(json_data.body)
        objTaskBAL=TaskBAL.TaskBAL()    
        strProfileId=loaded_json["ProfileId"]    
        objTaskEntity=objTaskBAL.GetTaskByProfileId(strProfileId)
        result = json.dumps([ob.__dict__ for ob in objTaskEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"AssignTo": "1"}
@csrf_exempt
@api_view(["POST"])
def GetTaskByAssignTo(json_data):
        loaded_json = json.loads(json_data.body)
        objTaskBAL=TaskBAL.TaskBAL()
        objCommonMethods=CommonMethods()       
        strAssignTo=loaded_json["AssignTo"]
        objTaskEntity=objTaskBAL.GetTaskByAssignTo(strAssignTo)
        result = json.dumps([ob.__dict__ for ob in objTaskEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"TaskId":"1","ProfileId":"2","TaskTitle":"Test1234","Description":"TestDescriptionOne","DueDate":"2019-11-16","AssignTo":"1","CreatedBy":"2","TaskStatus":"Close","TaskDuration":"2"}
@csrf_exempt
@api_view(["POST"])
def TaskUpdate(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strTaskId=loaded_json["TaskId"]
        strProfileId=loaded_json["ProfileId"]
        strTaskTitle=loaded_json["TaskTitle"]
        strDescription=loaded_json["Description"]
        strDueDate=loaded_json["DueDate"]
        strAssignTo=loaded_json["AssignTo"]
        strCreatedBy=loaded_json["CreatedBy"]
        strTaskStatus=loaded_json["TaskStatus"]
        strTaskDuration=loaded_json["TaskDuration"]
        objTaskBAL=TaskBAL.TaskBAL()
        result=objTaskBAL.TaskUpdate(strTaskId,strProfileId,strTaskTitle,strDescription,strDueDate,strAssignTo,strCreatedBy,strTaskStatus,strTaskDuration)
        return JsonResponse("1",safe=False)

#{"TaskId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetUserNameForAssignTo(id):
        objTaskBAL=TaskBAL.TaskBAL()        
        objTaskEntity=objTaskBAL.GetUserNameForAssignTo()
        result = json.dumps([ob.__dict__ for ob in objTaskEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"TaskId": "1"}
@csrf_exempt
@api_view(["POST"])
def TaskDelete(json_data):
        loaded_json = json.loads(json_data.body)
        objTaskBAL=TaskBAL.TaskBAL()  
        strTaskId=loaded_json["TaskId"]
        objTaskEntity=objTaskBAL.TaskDelete(strTaskId)
        return JsonResponse("1",safe=False)


@csrf_exempt
@api_view(["POST"])
def GetAllTasks(id):
        # loaded_json = json.loads(json_data.body)
        objTaskBAL=TaskBAL.TaskBAL()     
        objTaskEntity=objTaskBAL.GetAllTasks()
        result = json.dumps([ob.__dict__ for ob in objTaskEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)


      