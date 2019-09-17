from ..Entity.LanguageEntity import *
from django.db import connection

class LanguageDAL:
    def LanguageInsert(self,ProfileId,LanguageName,LanguageLevel):
        cursor=connection.cursor()
        args=[ProfileId,LanguageName,LanguageLevel]
        cursor.callproc('Language_Insert',args)
        return 1

    def GetLanguageByProfileId(self,ProfileId):
        cursor = connection.cursor()
        args = [ProfileId]
        cursor.callproc('GetLanguage_ByProfileId',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for LanguageItem in res:
            objLanguageEntity=LanguageEntity()
            objLanguageEntity.LanguageId=LanguageItem[0]
            objLanguageEntity.ProfileId=LanguageItem[1]
            objLanguageEntity.LanguageName=LanguageItem[2]
            objLanguageEntity.LanguageLevel=LanguageItem[3]
            arrayItems.append(objLanguageEntity)
        return arrayItems 

    def GetLanguageById(self,EducationId):
        cursor = connection.cursor()
        args = [EducationId]
        cursor.callproc('Language_GetById',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for LanguageItem in res:
            objLanguageEntity=LanguageEntity()
            objLanguageEntity.LanguageId=LanguageItem[0]
            objLanguageEntity.ProfileId=LanguageItem[1]
            objLanguageEntity.LanguageName=LanguageItem[2]
            objLanguageEntity.LanguageLevel=LanguageItem[3]
            arrayItems.append(objLanguageEntity)
        return arrayItems

    def LanguageUpdate(self,LanguageId,ProfileId,LanguageName,LanguageLevel):
        cursor = connection.cursor()
        args = [LanguageId,ProfileId,LanguageName,LanguageLevel]
        cursor.callproc('Language_Update',args)
        return 1

    def LanguageDelete(self,LanguageId):
        cursor = connection.cursor()
        args = [LanguageId]
        cursor.callproc('Language_Delete',args)
        return 1

