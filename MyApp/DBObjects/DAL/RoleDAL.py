from ..Entity.RoleEntity import *
from django.db import connection

class RoleDAL:
    def RoleInsert(self,ProfileId,RoleName):
        cursor=connection.cursor()
        args=[ProfileId,RoleName]
        cursor.callproc('Role_Insert',args)
        RoleItem=cursor.fetchall()
        objRoleId=RoleItem[0][0]
        return objRoleId

    def GetRoleByProfileId(self,ProfileId):
        cursor = connection.cursor()
        args = [ProfileId]
        cursor.callproc('GetRole_ByProfileId',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for RoleItem in res:
            objRoleEntity=RoleEntity()
            objRoleEntity.RoleId=RoleItem[0]
            objRoleEntity.ProfileId=RoleItem[1]
            objRoleEntity.RoleName=RoleItem[2]
            arrayItems.append(objRoleEntity)
        return arrayItems

    def GetRoleByRoleId(self,RoleId):
        cursor = connection.cursor()
        args = [RoleId]
        cursor.callproc('GetRole_ByRoleId',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for RoleItem in res:
            objRoleEntity=RoleEntity()
            objRoleEntity.RoleId=RoleItem[0]
            objRoleEntity.ProfileId=RoleItem[1]
            objRoleEntity.RoleName=RoleItem[2]
            arrayItems.append(objRoleEntity)
        return arrayItems 

    def RoleUpdate(self,RoleId,ProfileId,RoleName):
        cursor = connection.cursor()
        args = [RoleId,ProfileId,RoleName]
        cursor.callproc('Role_Update',args)
        return 1
    
    def RoleDelete(self,RoleId):
        cursor = connection.cursor()
        args = [RoleId]
        cursor.callproc('Role_Delete',args)
        return 1


