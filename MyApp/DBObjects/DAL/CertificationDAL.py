from ..Entity.CertificationEntity import *
from django.db import connection


class CertificationDAL:
    def CertificationInsert(self,ProfileId,CertificationName,Description):
        cursor = connection.cursor()
        args = [ProfileId,CertificationName,Description]
        cursor.callproc('Certification_Insert',args)
        return 1

    def CertificationGetByProfileId(self,ProfileId):
        cursor = connection.cursor()
        args = [ProfileId]
        cursor.callproc('Certification_GetByProfileId',args)
        return 1
