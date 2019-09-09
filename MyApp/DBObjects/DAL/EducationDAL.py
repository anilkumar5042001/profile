from ..Entity.EducationEntity import *
from django.db import connection

class WorkHistoryDAL:
    def EducationInsert(self,EducationId,ProfileId,NameOfInstitution,CourseName,StartYear,EndYear):
        cursor = connection.cursor()
        args = [EducationId,ProfileId,NameOfInstitution,CourseName,StartYear,EndYear]
        cursor.callproc('Education_Insert',args)
        return 1
