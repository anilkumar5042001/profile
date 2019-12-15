from ..Entity.SkillsEntity import *
from django.db import connection

class SkillsDAL:
    def SkillsInsert(self,ProfileId,SkillCategoryId,SkillName):
        cursor=connection.cursor()
        args=[ProfileId,SkillCategoryId,SkillName]
        cursor.callproc('Skills_Insert',args)
        SkillItem=cursor.fetchall()
        objSkillId=SkillItem[0][0]
        return objSkillId

    def GetSkillsByProfileId(self,ProfileId):
        cursor = connection.cursor()
        args = [ProfileId]
        cursor.callproc('GetSkills_ByProfileId',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for SkillItem in res:
            objSkillsEntity=SkillsEntity()
            objSkillsEntity.SkillId=SkillItem[0]
            objSkillsEntity.ProfileId=SkillItem[1]
            objSkillsEntity.SkillCategoryId=SkillItem[2]
            objSkillsEntity.SkillName=SkillItem[3]
            arrayItems.append(objSkillsEntity)
        return arrayItems

    def GetSkillsById(self,SkillId):
        cursor = connection.cursor()
        args = [SkillId]
        cursor.callproc('Skills_GetById',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for SkillItem in res:
            objSkillsEntity=SkillsEntity()
            objSkillsEntity.SkillId=SkillItem[0]
            objSkillsEntity.ProfileId=SkillItem[1]
            objSkillsEntity.SkillCategoryId=SkillItem[2]
            objSkillsEntity.SkillName=SkillItem[3]
            arrayItems.append(objSkillsEntity)
        return arrayItems  

    def SkillsUpdate(self,SkillId,ProfileId,SkillCategoryId,SkillName):
        cursor = connection.cursor()
        args = [SkillId,ProfileId,SkillCategoryId,SkillName]
        cursor.callproc('Skills_Update',args)
        return 1

    def SkillsDelete(self,SkillId):
        cursor = connection.cursor()
        args = [SkillId]
        cursor.callproc('Skills_Delete',args)
        return 1