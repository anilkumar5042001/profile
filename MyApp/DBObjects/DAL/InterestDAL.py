from ..Entity.InterestEntity import *
from django.db import connection

class InterestDAL: 
    def InterestInsert(self,ProfileId,InterestName):
        cursor = connection.cursor()
        args = [ProfileId,InterestName]
        cursor.callproc('Interest_Insert',args)
        return 1

    def GetInterestById(self,InterestId):
        cursor = connection.cursor()
        args=[InterestId]
        cursor.callproc('Interest_GetById',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for InterestItem in res:
            objInterestEntity=InterestEntity()
            objInterestEntity.InterestId=InterestItem[0]
            objInterestEntity.ProfileId=InterestItem[1]
            objInterestEntity.InterestName=InterestItem[2]
            arrayItems.append(objInterestEntity)
        return arrayItems

    def GetInterestByProfileId(self,ProfileId):
        cursor=connection.cursor()
        args=[ProfileId]
        cursor.callproc('GetInterest_ByProfileId',args)
        res=cursor.fetchall()
        arrayItems=[]
        for InterestItem in res:
            objInterestEntity=InterestEntity()
            objInterestEntity.InterestId=InterestItem[0]
            objInterestEntity.ProfileId=InterestItem[1]
            objInterestEntity.InterestName=InterestItem[2]
            arrayItems.append(objInterestEntity)
        return arrayItems

    def InterestUpdate(self,InterestId,ProfileId,InterestName):
        cursor = connection.cursor()
        args=[InterestId,ProfileId,InterestName]
        cursor.callproc('Interest_Update',args)
        return 1

    def InterestDelete(self,InterestId):
        cursor = connection.cursor()
        args=[InterestId]
        cursor.callproc('Interest_Delete',args)
        return 1

