from ..Entity.CertificationEntity import *
from django.db import connection


class CertificationDAL:
    def CertificationInsert(self,ProfileId,CertificationName,Description):
        cursor = connection.cursor()
        args = [ProfileId,CertificationName,Description]
        cursor.callproc('Certification_Insert',args)
        return 1

    def CertificationUpdate(self,CertificationId,CertificationName,Description):
        cursor = connection.cursor()
        args = [CertificationId,CertificationName,Description]
        cursor.callproc('Certification_Update',args)
        return 1

    def CertificationDelete(self,CertificationId):
        cursor = connection.cursor()
        args = [CertificationId]
        cursor.callproc('Certification_Delete',args)
        return 1

    def CertificationGetByProfileId(self,profileId):
        db_name = connection.settings_dict['NAME']
        cursor = connection.cursor()
        args = [profileId]
        cursor.callproc('Certification_GetByProfileId',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for certItem in res:
            objCertificationEntity=CertificationEntity()
            objCertificationEntity.CertificationId=certItem[0]
            objCertificationEntity.ProfileId=certItem[1]
            objCertificationEntity.CertificationName=certItem[2]
            objCertificationEntity.Description=certItem[3]
            arrayItems.append(objCertificationEntity)
        return arrayItems  
    
    def CertificationGetByCertificationId(self,certificationId):
        db_name = connection.settings_dict['NAME']
        cursor = connection.cursor()
        args = [certificationId]
        cursor.callproc('Certification_GetByCertificationId',args)
        certItem =  cursor.fetchall()
        
        objCertificationEntity=CertificationEntity()
        objCertificationEntity.CertificationId=certItem[0][0]
        objCertificationEntity.ProfileId=certItem[0][1]
        objCertificationEntity.CertificationName=certItem[0][2]
        objCertificationEntity.Description=certItem[0][3]
        
        return objCertificationEntity  

    
