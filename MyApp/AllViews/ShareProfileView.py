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
from ..DBObjects.BAL import ShareProfileBAL
from ..DBObjects.Entity import ShareProfileEntity
import smtplib

#{"ProfileId": "1","EmailId":"anilkumar5042001@gmail.com","ExpiryDate":"2019-11-12","ProfileLink":"https://boring-rosalind-5ae0ce.netlify.com/login","SharedWith":"Addars","Message":"callme","ShareType":"Link"}
@csrf_exempt
@api_view(["POST"])
def ShareProfileInsert(json_data):
        loaded_json = json.loads(json_data.body)
        strProfileId=loaded_json["ProfileId"]
        strEmailId=loaded_json["EmailId"]
        strSharedWith=loaded_json["SharedWith"]
        strProfileLink=loaded_json["ProfileLink"]
        strMessage=loaded_json["Message"]
        strExpiryDate=loaded_json["ExpiryDate"]
        strShareType=loaded_json["ShareType"]
        objShareProfileBAL=ShareProfileBAL.ShareProfileBAL()
        result=objShareProfileBAL.ShareProfileInsert(strProfileId,strEmailId,strProfileLink,strExpiryDate,strSharedWith,strMessage,strShareType) 
        return JsonResponse(result,safe=False)

#{"ProfileLink": "24012020052208800285"}
@csrf_exempt
@api_view(["POST"])
def ShareProfileGetProfileIdByProfileLink(json_data):
        loaded_json = json.loads(json_data.body)
        strProfileLink=loaded_json["ProfileLink"]
        objShareProfileBAL=ShareProfileBAL.ShareProfileBAL()
        objShareProfile=objShareProfileBAL.ShareProfileGetProfileIdByProfileLink(strProfileLink)
        result= json.dumps(objShareProfile.__dict__)
        return JsonResponse(result,safe=False)

        # result = json.dumps([ob.__dict__ for ob in objShareProfile])
        # return JsonResponse(result,safe=False)    

