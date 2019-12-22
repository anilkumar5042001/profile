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
from ..DBObjects.BAL import FavouriteBAL
from ..DBObjects.Entity import FavouriteEntity

#{"ProfileId": "1","FavouriteCategoryId":"1","FavouriteName": "Movie","FavouriteLink": "VenkyMama"}
@csrf_exempt
@api_view(["POST"])
def FavouriteInsert(json_data):
        loaded_json = json.loads(json_data.body)
        strProfileId=loaded_json["ProfileId"]
        strFavouriteCategoryId=loaded_json["FavouriteCategoryId"]
        strFavouriteName=loaded_json["FavouriteName"]
        strFavouriteLink=loaded_json["FavouriteLink"]
        objFavouriteBAL=FavouriteBAL.FavouriteBAL()
        result=objFavouriteBAL.FavouriteInsert(strProfileId,strFavouriteCategoryId,strFavouriteName,strFavouriteLink)
        return JsonResponse(result,safe=False)

#{"ProfileId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetFavouriteByProfileId(json_data):
        loaded_json = json.loads(json_data.body)
        objFavouriteBAL=FavouriteBAL.FavouriteBAL()
        strProfileId=loaded_json["ProfileId"]
        objFavouriteEntity=objFavouriteBAL.GetFavouriteByProfileId(strProfileId)
        result = json.dumps([ob.__dict__ for ob in objFavouriteEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"FavouriteId": "1"}
@csrf_exempt
@api_view(["POST"])
def GetFavouriteById(json_data):
        loaded_json = json.loads(json_data.body)
        objFavouriteBAL=FavouriteBAL.FavouriteBAL()
        strFavouriteId=loaded_json["FavouriteId"]
        objFavouriteEntity=objFavouriteBAL.GetFavouriteById(strFavouriteId)
        result = json.dumps([ob.__dict__ for ob in objFavouriteEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"FavouriteId":"1","ProfileId": "1","FavouriteCategoryId":"1","FavouriteName": "HindiMovie","FavouriteLink": "Dabaang3"}
@csrf_exempt
@api_view(["POST"])
def FavouriteUpdate(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strFavouriteId=loaded_json["FavouriteId"]
        strProfileId=loaded_json["ProfileId"]
        strFavouriteCategoryId=loaded_json["FavouriteCategoryId"]
        strFavouriteName=loaded_json["FavouriteName"]
        strFavouriteLink=loaded_json["FavouriteLink"]       
        objFavouriteBAL=FavouriteBAL.FavouriteBAL()
        result=objFavouriteBAL.FavouriteUpdate(strFavouriteId,strProfileId,strFavouriteCategoryId,strFavouriteName,strFavouriteLink)
        return JsonResponse("1",safe=False)

#{"FavouriteId": "1"}
@csrf_exempt
@api_view(["POST"])
def FavouriteDelete(json_data):
        loaded_json = json.loads(json_data.body)
        objFavouriteBAL=FavouriteBAL.FavouriteBAL()
        strFavouriteId=loaded_json["FavouriteId"]
        objFavouriteEntity=objFavouriteBAL.FavouriteDelete(strFavouriteId)
        return JsonResponse("1",safe=False)