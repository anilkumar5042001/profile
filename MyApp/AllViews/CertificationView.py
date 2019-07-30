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
from ..DBObjects.BAL import CertificationBAL
from ..DBObjects.Entity import CertificationEntity

#{"ProfileId": "1",CertificationName":"Haddop","Description":"I worked as a Test Engineer"}
@csrf_exempt
@api_view(["POST"])
def CertificationInsert(json_data):
        loaded_json = json.loads(json_data.body)
        strProfileId=loaded_json["ProfileId"]
        strCertificationName=loaded_json["CertificationName"]
        strDescription=loaded_json["Description"]
        objCertificationBAL=CertificationBAL.CertificationBAL()
        result=objCertificationBAL.CertificationInsert(strProfileId,strCertificationName,strDescription)
        return JsonResponse("1",safe=False)

@csrf_exempt
@api_view(["POST"])
def CertificationGetByProfileId(json_data):
        print('1')
        loaded_json = json.loads(json_data.body)
        print('2')
        strProfileId=loaded_json["ProfileId"]
        print('profileid is '+strProfileId )
        objCertificationBAL=CertificationBAL.CertificationBAL()
        objCertifications=objCertificationBAL.CertificationGetByProfileId(strProfileId)
        result = json.dumps([ob.__dict__ for ob in objCertifications])
        return JsonResponse(result,safe=False)    