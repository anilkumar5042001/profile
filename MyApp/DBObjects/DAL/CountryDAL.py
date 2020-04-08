from ..Entity.CountryEntity import *
from django.db import connection

class CountryDAL:
    def GetAllCountries(self):
        cursor = connection.cursor()
        cursor.callproc('Country_GetAll')
        res =  cursor.fetchall()
        arrayItems=[]
        for CountryItem in res:
            objCountryEntity=CountryEntity()
            objCountryEntity.CountryId=CountryItem[0]
            objCountryEntity.Countrycode=CountryItem[1]
            objCountryEntity.CountryName=CountryItem[2]
            objCountryEntity.Flag=CountryItem[3]
            arrayItems.append(objCountryEntity)
        return arrayItems
    
    def GetCountryById(self,countryId):
        cursor = connection.cursor()
        args = [countryId]
        cursor.callproc('Country_GetById',args)
        res =  cursor.fetchall()
        objCountryEntityOne=CountryEntity()
        objCountryEntityOne.Countrycode=res[0][0]
        objCountryEntityOne.CountryName=res[0][1]
        return objCountryEntityOne

    def InsertCountry(self,countryCode,countryName):
        cursor = connection.cursor()
        args = [countryCode,countryName]
        cursor.callproc('Country_Insert',args)
        return 1
        
