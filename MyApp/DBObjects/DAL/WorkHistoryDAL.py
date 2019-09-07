from ..Entity.WorkHistoryEntity import *
from django.db import connection


class WorkHistoryDAL:
    def WorkHistoryInsert(self,ProfileId,CompanyName,Role,Description,City,Country,StartDate,EndDate,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking):
        cursor = connection.cursor()
        args = [ProfileId,CompanyName,Role,Description,City,Country,StartDate,EndDate,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking]
        cursor.callproc('WorkHistory_Insert',args)
        return 1
    
    def CertificationGetByProfileId(self,profileId):
        db_name = connection.settings_dict['NAME']
        cursor = connection.cursor()
        args = [profileId]
        cursor.callproc('Certification_GetByProfileId',args)
        
    
    def WorkHistoryGetById(self,WorkHistoryId):
        cursor = connection.cursor()
        args = [WorkHistoryId]
        cursor.callproc('WorkHistory_GetById',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for WorkHistoryItem in res:
            objWorkHistoryEntity=WorkHistoryEntity()
            objWorkHistoryEntity.ProfileId=WorkHistoryItem[0]
            #objWorkHistoryEntity.WorkHistoryId=WorkHistoryItem[1]
            objWorkHistoryEntity.CompanyName=WorkHistoryItem[1]
            objWorkHistoryEntity.Role=WorkHistoryItem[2]
            objWorkHistoryEntity.Description=WorkHistoryItem[3]
            objWorkHistoryEntity.City=WorkHistoryItem[4]
            objWorkHistoryEntity.Country=WorkHistoryItem[5]
            #objWorkHistoryEntity.StartDate=WorkHistoryItem[6]
            #objWorkHistoryEntity.EndDate=WorkHistoryItem[7]
            arrayItems.append(objWorkHistoryEntity)
        return arrayItems 
        




        
