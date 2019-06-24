from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
#from .demo import GetCountry
# import demo

# Create your views here.
@api_view(["POST"])
def IdealWeight(heightdata):
        return JsonResponse("Hello world",safe=False)
        #return JsonResponse(GetCountry(),safe=False)

