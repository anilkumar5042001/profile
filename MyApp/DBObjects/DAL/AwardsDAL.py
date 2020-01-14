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
            objAwardEntity.ShowInProfile=AwardItem[4]
            arrayItems.append(objAwardEntity)
        return arrayItems

    

    def GetAwardsByAssignTo(self,assignTo):
        cursor = connection.cursor()
        args = [assignTo]
        cursor.callproc('Awards_GetByAssignTo',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for AwardItem in res:
            objAwardEntity=AwardsEntity()
            objAwardEntity.AwardId=AwardItem[0]
            objAwardEntity.ProfileId=AwardItem[1]
            objAwardEntity.AwardTitle=AwardItem[2]
            objAwardEntity.AwardDescription=AwardItem[3]
            objAwardEntity.FirstName=AwardItem[4]
            objAwardEntity.LastName=AwardItem[5]
            objAwardEntity.ShowInProfile=AwardItem[6]
            objAwardEntity.ProfileImageName=AwardItem[7]
            objAwardEntity.CompanyName=AwardItem[8]
            objAwardEntity.IsNew=AwardItem[9]
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

    def GetAwardsNew(self,AssignTo):
        cursor = connection.cursor()
        args = [AssignTo]
        cursor.callproc('Awards_GetNew',args)
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

    def AwardsUpdateShowInProfile(self,AwardId,ShowInProfile):
        cursor = connection.cursor()
        args = [AwardId,ShowInProfile]
        cursor.callproc('Awards_UpdateShowInProfile',args)
        return 1

    def AwardsUpdateIsNew(self,AssignTo):
        cursor = connection.cursor()
        args = [AssignTo]
        cursor.callproc('Awards_UpdateIsNew',args)
        return 1

    def AwardsDelete(self,AwardId):
        cursor = connection.cursor()
        args = [AwardId]
        cursor.callproc('Awards_Delete',args)
        return 1

