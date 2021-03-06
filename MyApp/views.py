from django.shortcuts import render
from django.http import Http404
from django.http import JsonResponse
from django.conf import settings
import json
from django.views.decorators.csrf import csrf_exempt
from .DBObjects.BAL import CountryBAL
from .DBObjects.Entity import CountryEntity
from django.core import serializers
from .DBScripts.MySqlTable import MySqlTable
from .DBScripts.ExecOrder import ExecOrder
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .DBObjects.BAL import UserProfileBAL
from .DBObjects.Entity import UserProfileEntity
from .DBObjects.BAL import ProjectsBAL
from .DBObjects.Entity import ProjectEntity
from .DBObjects.BAL import WorkHistoryBAL
from .DBObjects.Entity import WorkHistoryEntity


from rest_framework.parsers import MultiPartParser



from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response



from .serializers import FileSerializer


#from snippets.models import Snippet
#from snippets.serializers import SnippetSerializer



#from django.db import connection


# import demo

# Create your views here.
#@api_view(["POST"])

#@api_view(["POST"])

class FileView(APIView):

  parser_classes = (MultiPartParser, FormParser)

  def post(self, request, *args, **kwargs):

    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
class FileUploadView(APIView):
    parser_class = (FileUploadParser)

    def post(self, request, *args, **kwargs):

      file_serializer = FileSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def FileUploadViewHell(heightdata):
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
@api_view(["POST"])
def CountryGetAll(json_data):
        # loaded_json = json.loads(json_data.body)
        objCountryBAL=CountryBAL.CountryBAL()
        objCountryEntity=objCountryBAL.CountryGetAll()
        result = json.dumps([ob.__dict__ for ob in objCountryEntity])
        # result = json.dumps([ob.__dict__ for ob in objWorkHistoryEntity]) this is basically convert in to Json format

        #result= json.dumps(objWorkHistoryEntity.__dict__)
        return JsonResponse(result,safe=False)


#{"CountryCode": "uk", "ContryName": "unitr"}
@csrf_exempt
@api_view(["POST"])
def InsertCountry(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strCountryCode=loaded_json["CountryCode"]
        strContryName=loaded_json["ContryName"]
        objCountryBAL=CountryBAL.CountryBAL()
        result=objCountryBAL.InsertCountry(strCountryCode,strContryName)
        return JsonResponse("1",safe=False)    

#{"ProfileId": 1}
@csrf_exempt
@api_view(["POST"])
def GetUserProfileById(json_data):
        loaded_json = json.loads(json_data.body)
        objUserProfileBAL=UserProfileBAL.UserProfileBAL()
        profileId=loaded_json["ProfileId"]
        objUserProfileEntity=objUserProfileBAL.GetUserProfileById(profileId)
        result= json.dumps(objUserProfileEntity.__dict__)
        return JsonResponse(result,safe=False) 

#{"CompanyDomain": "core.co.uk"}
@csrf_exempt
@api_view(["POST"])
def UserProfileGetByCompanyDomain(json_data):
        loaded_json = json.loads(json_data.body)
        objUserProfileBAL=UserProfileBAL.UserProfileBAL()
        companyDomain=loaded_json["CompanyDomain"]
        objUserProfileEntity=objUserProfileBAL.UserProfileGetByCompanyDomain(companyDomain)
        result = json.dumps([ob.__dict__ for ob in objUserProfileEntity])
        return JsonResponse(result,safe=False) 

#{"ProfileId": 1}
@csrf_exempt
@api_view(["POST"])
def ExecuteDBScripts(json_data):
        loaded_json = json.loads(json_data.body)
        objExecOrder=ExecOrder
        objExecOrder.scriptsOrder('self')
        return JsonResponse("success",safe=False) 
        
#{"FirstName": "Test", "LastName": "Three", "EmailId":"testthree@gmail.com","PhoneNumber":"0","Education":"JNTU","Designation":"Software Engg","City":"Hyderabad","Country":"India","AboutMe":"I am mad","Password":"Test123","CompanyDomain":"SharePoint","RegGuid":"ABC1234","ActivationCode":"2345678","IsActivated":"1","CountryId":"1"}
@csrf_exempt
@api_view(["POST"])
def UserProfileInsert(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strFirstName=loaded_json["FirstName"]
        strLastName=loaded_json["LastName"]
        strEmailId=loaded_json["EmailId"]
        strPhoneNumber=loaded_json["PhoneNumber"]
        strEducation=loaded_json["Education"]
        strDesignation=loaded_json["Designation"]
        strCity=loaded_json["City"]
        strCountry=loaded_json["Country"]
        strAboutMe=loaded_json["AboutMe"]
        strPassword=loaded_json["Password"]
        strCompanyDomain=loaded_json["CompanyDomain"]
        strRegGuid=loaded_json["RegGuid"]
        strActivationCode=loaded_json["ActivationCode"]
        strIsActivated=loaded_json["IsActivated"]
        strCountryId=loaded_json["CountryId"]
        objUserProfileBAL=UserProfileBAL.UserProfileBAL()
        result=objUserProfileBAL.UserProfileInsert(strFirstName,strLastName,strEmailId,strPhoneNumber,strEducation,strDesignation,strCity,strCountry,strAboutMe,strPassword,strCompanyDomain,strRegGuid,strActivationCode,strIsActivated,strCountryId)
        return JsonResponse(result,safe=False)

@csrf_exempt
@api_view(["POST"])
def UploadFile(binaryData):
        print(binaryData)
        return JsonResponse("1",safe=False)

#{"ProfileId":"1","FirstName": "Test", "LastName": "Three", "EmailId":"testthree@gmail.com","AboutMe":"test","PhoneNumber":"0","Education":"JNTU","Designation":"Software Engg","City":"Banglore","Country":"India","RegGuid":"FGH34567","ActivationCode":"8765432","IsActivated":"0","CountryId":"2"}
@csrf_exempt
@api_view(["POST"])
def UserProfileUpdate(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strProfileId=loaded_json["ProfileId"]
        strFirstName=loaded_json["FirstName"]
        strLastName=loaded_json["LastName"]
        strEmailId=loaded_json["EmailId"]
        strPhoneNumber=loaded_json["PhoneNumber"]
        strEducation=loaded_json["Education"]
        strDesignation=loaded_json["Designation"]
        strCity=loaded_json["City"]
        strCountry=loaded_json["Country"]
        strAboutMe=loaded_json["AboutMe"]  
        strProfileImageName=loaded_json["ProfileImageName"] 
        strCountryId=loaded_json["CountryId"] 
        objUserProfileBAL=UserProfileBAL.UserProfileBAL()
        result=objUserProfileBAL.UserProfileUpdate(strProfileId,strFirstName,strLastName,strEmailId,strPhoneNumber,strEducation,strDesignation,strCity,strCountry,strAboutMe,strProfileImageName,strCountryId)
        return JsonResponse("1",safe=False)

#{"ProfileId":"1","CompanyDomain":"Core@co.uk"}
@csrf_exempt
@api_view(["POST"])
def UserProfileUpdateDomainName(json_data):
        loaded_json = json.loads(json_data.body)
        strProfileId=loaded_json["ProfileId"]
        strCompanyDomain=loaded_json["CompanyDomain"]
        objUserProfileBAL=UserProfileBAL.UserProfileBAL()
        result=objUserProfileBAL.UserProfileUpdateDomainName(strProfileId,strCompanyDomain)
        return JsonResponse("1",safe=False)

#{"FirstName": "Test", "LastName": "Three", "EmailId":"testthree@gmail.com","PhoneNumber":"0"}
@csrf_exempt
@api_view(["POST"])
def ProjectInsert(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strProjectName=loaded_json["ProjectName"]
        strLastName=loaded_json["LastName"]
        strEmailId=loaded_json["EmailId"]
        strPhoneNumber=loaded_json["PhoneNumber"]
        objUserProfileBAL=UserProfileBAL.UserProfileBAL()
        result=objUserProfileBAL.UserProfileInsert(strFirstName,strLastName,strEmailId,strPhoneNumber)
        return JsonResponse("1",safe=False)

#{"EmailId":"testthree@gmail.com","Password":"Test123"}
@csrf_exempt
@api_view(["POST"])
def UserLoginCheckCredentials(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strEmailId=loaded_json["EmailId"]
        strPassword=loaded_json["Password"]      
        objUserProfileBAL=UserProfileBAL.UserProfileBAL()
        objUserProfileEntity=objUserProfileBAL.UserLoginCheckCredentials(strEmailId,strPassword)
        result= json.dumps(objUserProfileEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"EmailId":"testthree@gmail.com"}
@csrf_exempt
@api_view(["POST"])
def UserProfileGetProfileIdByEmailId(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strEmailId=loaded_json["EmailId"]
        objUserProfileBAL=UserProfileBAL.UserProfileBAL()
        objUserProfileEntity=objUserProfileBAL.UserProfileGetProfileIdByEmailId(strEmailId)
        result= json.dumps(objUserProfileEntity.__dict__)
        return JsonResponse(result,safe=False)

#{"RegGuid":"ABC1234","ActivationCode":"1234"}
@csrf_exempt
@api_view(["POST"])
def UserProfileUpdateRegCode(json_data):
        loaded_json = json.loads(json_data.body)
        print(loaded_json)
        strRegGuid=loaded_json["RegGuid"]
        strActivationCode=loaded_json["ActivationCode"]      
        objUserProfileBAL=UserProfileBAL.UserProfileBAL()
        objUserProfileEntity=objUserProfileBAL.UserProfileUpdateRegCode(strRegGuid,strActivationCode)
        result= json.dumps(objUserProfileEntity.__dict__)
        return JsonResponse(result,safe=False)


