from ..Entity.AwardsEntity import *
from django.db import connection

class AwardsDAL:
    def AwardsInsert(self,ProfileId,AwardTitle,AwardDescription,AssignTo):
        cursor=connection.cursor()
        args=[ProfileId,AwardTitle,AwardDescription,AssignTo]
        cursor.callproc('Awards_Insert',args)
        return 1

    def GetAwardsByProfileId(self,ProfileId):
        cursor = connection.cursor()
        args = [ProfileId]
        cursor.callproc('GetAwards_ByProfileId',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for AwardItem in res:
            objAwardEntity=AwardsEntity()
            objAwardEntity.AwardId=AwardItem[0]
            objAwardEntity.ProfileId=AwardItem[1]
            objAwardEntity.AwardTitle=AwardItem[2]
            objAwardEntity.AwardDescription=AwardItem[3]
            arrayItems.append(objAwardEntity)
        return arrayItems

    def GetAwardsById(self,AwardId):
        cursor = connection.cursor()
        args = [AwardId]
        cursor.callproc('Awards_GetById',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for AwardItem in res:
            objAwardEntity=AwardsEntity()
            objAwardEntity.AwardId=AwardItem[0]
            objAwardEntity.ProfileId=AwardItem[1]
            objAwardEntity.AwardTitle=AwardItem[2]
            objAwardEntity.AwardDescription=AwardItem[3]
            arrayItems.append(objAwardEntity)
        return arrayItems  

    def AwardsUpdate(self,AwardId,ProfileId,AwardTitle,AwardDescription):
        cursor = connection.cursor()
        args = [AwardId,ProfileId,AwardTitle,AwardDescription]
        cursor.callproc('Awards_Update',args)
        return 1

    def AwardsDelete(self,AwardId):
        cursor = connection.cursor()
        args = [AwardId]
        cursor.callproc('Awards_Delete',args)
        return 1

