from ..Entity.SkillCategoryEntity import *
from django.db import connection

class SkillCategoryDAL:
    def SkillsCategoryInsert(self,ProfileId,SkillCategoryName):
        cursor=connection.cursor()
        args=[ProfileId,SkillCategoryName]
        cursor.callproc('SkillsCategory_Insert',args)
        SkillCategoryItem=cursor.fetchall()
        objSkillCategoryId=SkillCategoryItem[0][0]
        return objSkillCategoryId

    def GetSkillsCategoryByProfileId(self,ProfileId):
        cursor = connection.cursor()
        args = [ProfileId]
        cursor.callproc('GetSkillsCategory_ByProfileId',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for SkillCategoryItem in res:
            objSkillCategoryEntity=SkillCategoryEntity()
            objSkillCategoryEntity.SkillCategoryId=SkillCategoryItem[0]
            objSkillCategoryEntity.ProfileId=SkillCategoryItem[1]
            objSkillCategoryEntity.SkillCategoryName=SkillCategoryItem[2]
            arrayItems.append(objSkillCategoryEntity)
        return arrayItems

    def GetSkillsCategoryById(self,SkillCategoryId):
        cursor = connection.cursor()
        args = [SkillCategoryId]
        cursor.callproc('SkillsCategory_GetById',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for SkillCategoryItem in res:
            objSkillCategoryEntity=SkillCategoryEntity()
            objSkillCategoryEntity.SkillCategoryId=SkillCategoryItem[0]
            objSkillCategoryEntity.ProfileId=SkillCategoryItem[1]
            objSkillCategoryEntity.SkillCategoryName=SkillCategoryItem[2]
            arrayItems.append(objSkillCategoryEntity)
        return arrayItems  

    def SkillsCategoryUpdate(self,SkillCategoryId,ProfileId,SkillCategoryName):
        cursor = connection.cursor()
        args = [SkillCategoryId,ProfileId,SkillCategoryName]
        cursor.callproc('SkillsCategory_Update',args)
        return 1

    def SkillsCategoryDelete(self,SkillCategoryId):
        cursor = connection.cursor()
        args = [SkillCategoryId]
        cursor.callproc('SkillsCategory_Delete',args)
        return 1

