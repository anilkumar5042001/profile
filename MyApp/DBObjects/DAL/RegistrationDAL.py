from ..Entity.RegistrationEntity import *
from django.db import connection

class RegistrationDAL:
    def RegistrationInsert(self,EmailId,Password):
        cursor=connection.cursor()
        args=[EmailId,Password]
        cursor.callproc('Registration_Insert',args)
        RegistrationItem=cursor.fetchall()
        objRegistrationId=RegistrationItem[0][0]
        return objRegistrationId

    def GetRegistrationeById(self,RegistrationId):
        cursor = connection.cursor()
        args = [RegistrationId]
        cursor.callproc('Registration_GetById',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for RegistrationItem in res:
            objRegistrationEntity=RegistrationEntity()
            objRegistrationEntity.RegistrationId=RegistrationItem[0]
            objRegistrationEntity.EmailId=RegistrationItem[1]
            objRegistrationEntity.Password=RegistrationItem[2]
            arrayItems.append(objRegistrationEntity)
        return arrayItems 

    def RegistrationUpdate(self,RegistrationId,EmailId,Password):
        cursor = connection.cursor()
        args = [RegistrationId,EmailId,Password]
        cursor.callproc('Registration_Update',args)
        return 1


