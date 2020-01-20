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

#{"ProfileId": "1","EmailId":"Best Developer@gmail","ExpiryDate":"2019-11-12","ProfileLink":"wwww.Nagukandivalas/htt.com","SharedWith":"Addars","Message":"callme"}
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
        objShareProfileBAL=ShareProfileBAL.ShareProfileBAL()
        result=objShareProfileBAL.ShareProfileInsert(strProfileId,strEmailId,strProfileLink,strExpiryDate,strSharedWith,strMessage) 
        return JsonResponse("1",safe=False)

