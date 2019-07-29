from ..Entity.WorkHistoryEntity import *
from django.db import connection


class WorkHistoryDAL:
    def WorkHistoryInsert(self,ProfileId,CompanyName,Role,Description,City,Country,StartDate,EndDate):
        cursor = connection.cursor()
        args = [ProfileId,CompanyName,Role,Description,City,Country,StartDate,EndDate]
        cursor.callproc('WorkHistory_Insert',args)
        return 1
    
    def WorkHistoryGetById(self,WorkHistoryId):
        cursor = connection.cursor()
        args = [WorkHistoryId]
        cursor.callproc('WorkHistory_GetById',args)
        return 1
