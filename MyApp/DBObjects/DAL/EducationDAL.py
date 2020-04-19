from ..Entity.EducationEntity import *
from django.db import connection

class EducationDAL:
    def EducationInsert(self,ProfileId,NameOfInstitution,Degree,StartYear,EndYear,EducationDescription):
        cursor = connection.cursor()
        args = [ProfileId,NameOfInstitution,Degree,StartYear,EndYear,EducationDescription]
        cursor.callproc('Education_Insert',args)
        return 1

    def GetEducationById(self,EducationId):
        cursor = connection.cursor()
        args = [EducationId]
        cursor.callproc('Education_GetById',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for EducationItem in res:
            objEducationEntity=EducationEntity()
            objEducationEntity.EducationId=EducationItem[0]
            objEducationEntity.ProfileId=EducationItem[1]
            objEducationEntity.NameOfInstitution=EducationItem[2]
            objEducationEntity.Degree=EducationItem[3]
            objEducationEntity.StartYear=EducationItem[4]
            objEducationEntity.EndYear=EducationItem[5]
            objEducationEntity.EducationDescription=EducationItem[6]
            arrayItems.append(objEducationEntity)
        return arrayItems

    def GetEducationByProfileId(self,ProfileId):
        cursor = connection.cursor()
        args = [ProfileId]
        cursor.callproc('Education_ByProfileId',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for EducationItem in res:
            objEducationEntity=EducationEntity()
            objEducationEntity.EducationId=EducationItem[0]
            objEducationEntity.ProfileId=EducationItem[1]
            objEducationEntity.NameOfInstitution=EducationItem[2]
            objEducationEntity.Degree=EducationItem[3]
            objEducationEntity.StartYear=EducationItem[4]
            objEducationEntity.EndYear=EducationItem[5]
            objEducationEntity.EducationDescription=EducationItem[6]
            arrayItems.append(objEducationEntity)
        return arrayItems 

    def EducationUpdate(self,EducationId,ProfileId,NameOfInstitution,Degree,StartYear,EndYear,EducationDescription):
        cursor = connection.cursor()
        args = [EducationId,ProfileId,NameOfInstitution,Degree,StartYear,EndYear,EducationDescription]
        cursor.callproc('Education_Update',args)
        return 1

    def EducationDelete(self,EducationId):
        cursor = connection.cursor()
        args = [EducationId]
        cursor.callproc('Education_Delete',args)
        return 1
