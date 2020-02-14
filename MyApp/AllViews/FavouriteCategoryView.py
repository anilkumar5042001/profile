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
from ..DBObjects.BAL import FavouriteCategoryBAL
from ..DBObjects.Entity import FavouriteCategoryEntity

#{"ProfileId": "1","FavouriteCategoryName": "Movie"}
@csrf_exempt
@api_view(["POST"])
def FavouriteCategoryInsert(json_data):
        loaded_json = json.loads(json_data.body)
        strProfileId=loaded_json["ProfileId"]
        strFavouriteCategoryName=loaded_json["FavouriteCategoryName"]
        objFavouriteCategoryBAL=FavouriteCategoryBAL.FavouriteCategoryBAL()
        result=objFavouriteCategoryBAL.FavouriteCategoryInsert(strProfileId,strFavouriteCategoryName)
        return JsonResponse(result,safe=False)

#{"ProfileId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetFavouriteCategoryByProfileId(json_data):
        loaded_json = json.loads(json_data.body)
        objFavouriteCategoryBAL=FavouriteCategoryBAL.FavouriteCategoryBAL()
        strProfileId=loaded_json["ProfileId"]
        objFavouriteCategoryEntity=objFavouriteCategoryBAL.GetFavouriteCategoryByProfileId(strProfileId)
        result = json.dumps([ob.__dict__ for ob in objFavouriteCategoryEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"FavouriteCategoryId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetFavouriteCategoryById(json_data):
        loaded_json = json.loads(json_data.body)
        objFavouriteCategoryBAL=FavouriteCategoryBAL.FavouriteCategoryBAL()
        strFavouriteCategoryId=loaded_json["FavouriteCategoryId"]
        objFavouriteCategoryEntity=objFavouriteCategoryBAL.GetFavouriteCategoryById(strFavouriteCategoryId)
        result = json.dumps([ob.__dict__ for ob in objFavouriteCategoryEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)
#{"FavouriteCategoryId":"1","ProfileId": "1","FavouriteCategoryName": "Books"}
@csrf_exempt
@api_view(["POST"])
def FavouriteCategoryUpdate(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strFavouriteCategoryId=loaded_json["FavouriteCategoryId"]
        strProfileId=loaded_json["ProfileId"]
        strFavouriteCategoryName=loaded_json["FavouriteCategoryName"]
        objFavouriteCategoryBAL=FavouriteCategoryBAL.FavouriteCategoryBAL()
        result=objFavouriteCategoryBAL.FavouriteCategoryUpdate(strFavouriteCategoryId,strProfileId,strFavouriteCategoryName)
        return JsonResponse("1",safe=False)

#{"FavouriteCategoryId": "1"}
@csrf_exempt
@api_view(["POST"])
def FavouriteCategoryDelete(json_data):
        loaded_json = json.loads(json_data.body)
        objFavouriteCategoryBAL=FavouriteCategoryBAL.FavouriteCategoryBAL()
        strFavouriteCategoryId=loaded_json["FavouriteCategoryId"]
        objFavouriteCategoryEntity=objFavouriteCategoryBAL.FavouriteCategoryDelete(strFavouriteCategoryId)
        return JsonResponse("1",safe=False)