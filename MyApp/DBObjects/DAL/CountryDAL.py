from ..Entity.CountryEntity import *
from django.db import connection

class CountryDAL:
    def GetCountries(self):
        cursor = connection.cursor()
        cursor.callproc('Country_GetAll')
        res =  cursor.fetchall()
        countries=[]
        for r in res:
            objCountryEntityOne=CountryEntity()
            objCountryEntityOne.CountryId=r[0]
            objCountryEntityOne.Countrycode=r[1]
            objCountryEntityOne.CountryName=r[2]
            countries.append(objCountryEntityOne)
        return countries
    # def GetCountryById(self,countryId):
    #     objCountryEntityOne=CountryEntity()
    #     objCountryEntityOne.Countrycode="Ind"
    #     objCountryEntityOne.CountryName="India"
    #     return objCountryEntityOne
    def GetCountryById(self,countryId):
        cursor = connection.cursor()
        args = [1]
        cursor.callproc('Country_GetById',args)
        res =  cursor.fetchall()
        objCountryEntityOne=CountryEntity()
        objCountryEntityOne.Countrycode=res[0][0]
        objCountryEntityOne.CountryName=res[0][1]
        return objCountryEntityOne
        
