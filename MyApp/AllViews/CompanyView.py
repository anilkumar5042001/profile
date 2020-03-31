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
from ..DBObjects.BAL import CompanyBAL
from ..DBObjects.Entity import CompanyEntity

@csrf_exempt
@api_view(["POST"])
def CompanyGetAll(json_data):
        # loaded_json = json.loads(json_data.body)
        objCompanyBAL=CompanyBAL.CompanyBAL()
        objCompanyEntity=objCompanyBAL.CompanyGetAll()
        result = json.dumps([ob.__dict__ for ob in objCompanyEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)












      

