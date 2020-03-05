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
from ..DBObjects.BAL import TaskCommentBAL
from ..DBObjects.Entity import TaskCommentEntity
import smtplib

#{"ProfileId": "1","TaskId":"1","Comment":"Need to complete TaskComments", "CommentedBy":"1", "CommentedOn":"2020.03.01"}
@csrf_exempt
@api_view(["POST"])
def TaskCommentInsert(json_data):
        loaded_json = json.loads(json_data.body)
        strProfileId=loaded_json["ProfileId"]
        strTaskId=loaded_json["TaskId"]
        strComment=loaded_json["Comment"]
        strCommentedBy=loaded_json["CommentedBy"]
        strCommentedOn=loaded_json["CommentedOn"]
        objTaskCommentBAL=TaskCommentBAL.TaskCommentBAL()
        result=objTaskCommentBAL.TaskCommentInsert(strProfileId,strTaskId,strComment,strCommentedBy,strCommentedOn)
        return JsonResponse(result,safe=False)

#{"TaskId":"1"}
@csrf_exempt
@api_view(["POST"])
def TaskCommentUpdateIsNew(json_data):
        loaded_json = json.loads(json_data.body)
        strTaskId=loaded_json["TaskId"]
        objTaskCommentBAL=TaskCommentBAL.TaskCommentBAL()
        result=objTaskCommentBAL.TaskCommentUpdateIsNew(strTaskId)
        return JsonResponse(result,safe=False)

#{"ProfileId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetTaskCommentByProfileId(json_data):
        loaded_json = json.loads(json_data.body)
        objTaskCommentBAL=TaskCommentBAL.TaskCommentBAL()
        strProfileId=loaded_json["ProfileId"]
        objTaskCommentEntity=objTaskCommentBAL.GetTaskCommentByProfileId(strProfileId)
        result = json.dumps([ob.__dict__ for ob in objTaskCommentEntity])
        #result = json.dumps([ob.__dict__ for ob in objAmountDetailsEntity]) this is basically convert in to Json format
        #result= json.dumps(objAmountDetailsEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"TaskId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetTaskCommentByTaskId(json_data):
        loaded_json = json.loads(json_data.body)
        objTaskCommentBAL=TaskCommentBAL.TaskCommentBAL()
        strTaskId=loaded_json["TaskId"]
        objTaskCommentEntity=objTaskCommentBAL.GetTaskCommentByTaskId(strTaskId)
        result = json.dumps([ob.__dict__ for ob in objTaskCommentEntity])
        #result = json.dumps([ob.__dict__ for ob in objAmountDetailsEntity]) this is basically convert in to Json format
        #result= json.dumps(objAmountDetailsEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"TaskCommentId": "1"}
@csrf_exempt
@api_view(["POST"])
def TaskCommentDelete(json_data):
        loaded_json = json.loads(json_data.body)
        objTaskCommentBAL=TaskCommentBAL.TaskCommentBAL()
        strTaskCommentId=loaded_json["TaskCommentId"]
        objTaskCommentEntity=objTaskCommentBAL.TaskCommentDelete(strTaskCommentId)
        return JsonResponse("1",safe=False)


