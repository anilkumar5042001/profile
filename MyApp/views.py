from django.shortcuts import render
from django.http import Http404
from django.http import JsonResponse
from django.conf import settings
import json
from .demo import GetCountry
from django.views.decorators.csrf import csrf_exempt
from .DBObjects.BAL import CountryBAL
from .DBObjects.Entity import CountryEntity
from django.core import serializers
from .DBScripts.MySqlTable import MySqlTable
from .DBScripts.ExecOrder import ExecOrder


#from django.db import connection


# import demo

# Create your views here.
#@api_view(["POST"])
@csrf_exempt
def IdealWeight(heightdata):
        #return JsonResponse(GetCountry(),safe=False)
        #return JsonResponse(GetCountry(),safe=False)
        objCountryBAL=CountryBAL.CountryBAL()
        objCountryEntity=objCountryBAL.GetCountryById("1")
        objCountries=objCountryBAL.GetCountries()

        # return JsonResponse(objCountryEntity[1].CountryName,safe=False)
        # return JsonResponse(json.dumps(objCountryEntity),safe=False)
        
        
        #return JsonResponse(data,safe=False)
        #return HttpResponse(data, content_type="application/json")
       # strAbc= json.dumps(objCountryEntity.__dict__)

        strAbc = json.dumps([ob.__dict__ for ob in objCountries])
        #strAbc  = json.dumps(objCountryEntity)
 
        # A python list as a JSON string
        print('hello'+strAbc)
        
        return JsonResponse(strAbc,safe=False)        


@csrf_exempt
def GetCountryById(id):
        objCountryBAL=CountryBAL.CountryBAL()
        objCountryEntity=objCountryBAL.GetCountryById(id)
        result= json.dumps(objCountryEntity.__dict__)
        return JsonResponse(result,safe=False)        

@csrf_exempt
def GetCountries(id):
        objCountryBAL=CountryBAL.CountryBAL()
        objCountries=objCountryBAL.GetCountries()
        result = json.dumps([ob.__dict__ for ob in objCountries])
        return JsonResponse(result,safe=False)        


