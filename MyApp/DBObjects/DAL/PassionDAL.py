from ..Entity.PassionEntity import *
from django.db import connection

class PassionDAL:
    def PassionInsert(self,ProfileId,PassionName,Description):
        cursor = connection.cursor()
        args = [ProfileId,PassionName,Description]
        cursor.callproc('Passion_Insert',args)
        PassionItem=cursor.fetchall()
        objPassionId=PassionItem[0][0]
        return objPassionId

    def GetPassionById(self,PassionId):
        cursor = connection.cursor()
        args = [PassionId]
        cursor.callproc('GetPassion_ById',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for PassionItem in res:
            objPassionEntity=PassionEntity()
            objPassionEntity.PassionId=PassionItem[0]
            objPassionEntity.ProfileId=PassionItem[1]
            objPassionEntity.PassionName=PassionItem[2]
            objPassionEntity.Description=PassionItem[3]
            arrayItems.append(objPassionEntity)
        return arrayItems

    def GetPassionByProfileId(self,ProfileId):
        cursor = connection.cursor()
        args = [ProfileId]
        cursor.callproc('GetPassion_ByProfileId',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for PassionItem in res:
            objPassionEntity=PassionEntity()
            objPassionEntity.PassionId=PassionItem[0]
            objPassionEntity.ProfileId=PassionItem[1]
            objPassionEntity.PassionName=PassionItem[2]
            objPassionEntity.Description=PassionItem[3]
            arrayItems.append(objPassionEntity)
        return arrayItems 

    def PassionUpdate(self,PassionId,ProfileId,PassionName,Description):
        cursor = connection.cursor()
        args = [PassionId,ProfileId,PassionName,Description]
        cursor.callproc('Passion_Update',args)
        return 1

    def PassionDelete(self,PassionId):
        cursor = connection.cursor()
        args = [PassionId]
        cursor.callproc('Passion_Delete',args)
        return 1
