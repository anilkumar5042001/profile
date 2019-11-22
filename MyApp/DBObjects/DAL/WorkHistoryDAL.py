from ..Entity.WorkHistoryEntity import *
from django.db import connection


class WorkHistoryDAL:
    def WorkHistoryInsert(self,ProfileId,CompanyName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking):
        cursor = connection.cursor()
        args = [ProfileId,CompanyName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking]
        cursor.callproc('WorkHistory_Insert',args)
        workHistoryItem =  cursor.fetchall()
        workHistoryId=workHistoryItem[0][0]
        return workHistoryId
        
    
    def CertificationGetByProfileId(self,profileId):
        db_name = connection.settings_dict['NAME']
        cursor = connection.cursor()
        args = [profileId]
        cursor.callproc('Certification_GetByProfileId',args)

    def WorkHistoryUpdate(self,ProfileId,WorkHistoryId,CompanyName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking):
        cursor = connection.cursor()
        args = [ProfileId,WorkHistoryId,CompanyName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking]
        cursor.callproc('WorkHistory_Update',args)
        return 1
        
    
    def GetWorkHistoryByProfileId(self,ProfileId):
        cursor = connection.cursor()
        args = [ProfileId]
        cursor.callproc('GetWorkHistory_ByProfileId',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for WorkHistoryItem in res:
            objWorkHistoryEntity=WorkHistoryEntity()
            objWorkHistoryEntity.ProfileId=WorkHistoryItem[0]
            objWorkHistoryEntity.WorkHistoryId=WorkHistoryItem[1]
            objWorkHistoryEntity.CompanyName=WorkHistoryItem[2]
            objWorkHistoryEntity.Role=WorkHistoryItem[3]
            objWorkHistoryEntity.Description=WorkHistoryItem[4]
            objWorkHistoryEntity.City=WorkHistoryItem[5]
            objWorkHistoryEntity.Country=WorkHistoryItem[6]
            objWorkHistoryEntity.StartMonth=WorkHistoryItem[7]
            objWorkHistoryEntity.StartYear=WorkHistoryItem[8]
            objWorkHistoryEntity.EndMonth=WorkHistoryItem[9]
            objWorkHistoryEntity.EndYear=WorkHistoryItem[10]            
            objWorkHistoryEntity.CurrenltyWorking=WorkHistoryItem[11]
            arrayItems.append(objWorkHistoryEntity)
        return arrayItems 

    def WorkHistoryGetById(self,WorkHistoryId):
        cursor = connection.cursor()
        args = [WorkHistoryId]
        cursor.callproc('WorkHistory_GetById',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for WorkHistoryItem in res:
            objWorkHistoryEntity=WorkHistoryEntity()
            objWorkHistoryEntity.ProfileId=WorkHistoryItem[0]
            objWorkHistoryEntity.WorkHistoryId=WorkHistoryItem[1]
            objWorkHistoryEntity.CompanyName=WorkHistoryItem[2]
            objWorkHistoryEntity.Role=WorkHistoryItem[3]
            objWorkHistoryEntity.Description=WorkHistoryItem[4]
            objWorkHistoryEntity.City=WorkHistoryItem[5]
            objWorkHistoryEntity.Country=WorkHistoryItem[6]
            objWorkHistoryEntity.StartMonth=WorkHistoryItem[7]
            objWorkHistoryEntity.StartYear=WorkHistoryItem[8]
            objWorkHistoryEntity.EndMonth=WorkHistoryItem[9]
            objWorkHistoryEntity.EndYear=WorkHistoryItem[10]            
            objWorkHistoryEntity.CurrenltyWorking=WorkHistoryItem[11]
            arrayItems.append(objWorkHistoryEntity)
        return arrayItems

    def GetWorkHistoryByProfileIdAndCompanyName(self,ProfileId,CompanyName):
        cursor = connection.cursor()
        args = [ProfileId,CompanyName]
        cursor.callproc('GetWorkHistory_ByProfileIdAndCompanyName',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for WorkHistoryItem in res:
            objWorkHistoryEntity=WorkHistoryEntity()
            objWorkHistoryEntity.ProfileId=WorkHistoryItem[0]
            objWorkHistoryEntity.WorkHistoryId=WorkHistoryItem[1]
            objWorkHistoryEntity.CompanyName=WorkHistoryItem[2]
            objWorkHistoryEntity.Role=WorkHistoryItem[3]
            objWorkHistoryEntity.Description=WorkHistoryItem[4]
            objWorkHistoryEntity.City=WorkHistoryItem[5]
            objWorkHistoryEntity.Country=WorkHistoryItem[6]
            objWorkHistoryEntity.StartMonth=WorkHistoryItem[7]
            objWorkHistoryEntity.StartYear=WorkHistoryItem[8]
            objWorkHistoryEntity.EndMonth=WorkHistoryItem[9]
            objWorkHistoryEntity.EndYear=WorkHistoryItem[10]            
            objWorkHistoryEntity.CurrenltyWorking=WorkHistoryItem[11]
            arrayItems.append(objWorkHistoryEntity)
        return arrayItems  

    def WorkHistoryDelete(self,WorkHistoryId):
        cursor = connection.cursor()
        args = [WorkHistoryId]
        cursor.callproc('WorkHistory_Delete',args)
        return 1

    def ProjectHighlightsInsert(self,WorkHistoryId,ProjectHighlightsDescription):
        cursor = connection.cursor()
        args = [WorkHistoryId,ProjectHighlightsDescription]
        cursor.callproc('ProjectHighlights_Insert',args)
        return 1

    def ProjectHighlightsGetById(self,WorkHistoryId):
        cursor = connection.cursor()
        args = [WorkHistoryId]
        cursor.callproc('ProjectHighlights_GetById',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for ProjectHighlightsItem in res:
            objProjectHighlightsEntity=ProjectHighlightsEntity()
            objProjectHighlightsEntity.HighlightId=ProjectHighlightsItem[0]
            objProjectHighlightsEntity.WorkHistoryId=ProjectHighlightsItem[1]
            objProjectHighlightsEntity.Description=ProjectHighlightsItem[2]
            arrayItems.append(objProjectHighlightsEntity)
        return arrayItems 

    def ProjectHighlightsUpdate(self,HighlightId,WorkHistoryId,Description):
        cursor = connection.cursor()
        args = [HighlightId,WorkHistoryId,Description]
        cursor.callproc('ProjectHighlights_Update',args)
        return 1

    def ProjectHighlightsDelete(self,HighlightId):
        cursor = connection.cursor()
        args = [HighlightId]
        cursor.callproc('ProjectHighlights_Delete',args)
        return 1

    def ProjectHighlightsDeleteByWorkHistoryId(self,WorkHistoryId):
        cursor = connection.cursor()
        args = [WorkHistoryId]
        cursor.callproc('ProjectHighlightsDelete_ByWorkHistoryId',args)
        return 1

    def ResponsibilitiesInsert(self,WorkHistoryId,Description):
        cursor = connection.cursor()
        args = [WorkHistoryId,Description]
        cursor.callproc('Responsibilities_Insert',args)
        return 1

    def ResponsibilitiesGetById(self,WorkHistoryId):
        cursor = connection.cursor()
        args = [WorkHistoryId]
        cursor.callproc('Responsibilities_GetById',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for ResponsibilitiesItem in res:
            objResponsibilitiesEntity=ResponsibilitiesEntity()
            objResponsibilitiesEntity.ResponsibilitiesId=ResponsibilitiesItem[0]
            objResponsibilitiesEntity.WorkHistoryId=ResponsibilitiesItem[1]
            objResponsibilitiesEntity.Description=ResponsibilitiesItem[2]
            arrayItems.append(objResponsibilitiesEntity)
        return arrayItems 

    def ResponsibilitiesUpdate(self,ResponsibilitiesId,WorkHistoryId,Description):
        cursor = connection.cursor()
        args = [ResponsibilitiesId,WorkHistoryId,Description]
        cursor.callproc('Responsibilities_Update',args)
        return 1

    def ResponsibilitiesDelete(self,ResponsibilitiesId):
        cursor = connection.cursor()
        args = [ResponsibilitiesId]
        cursor.callproc('Responsibilities_Delete',args)
        return 1

    def ResponsibilitiesDeleteByWorkHistoryId(self,WorkHistoryId):
        cursor = connection.cursor()
        args = [WorkHistoryId]
        cursor.callproc('ResponsibilitiesDelete_ByWorkHistoryId',args)
        return 1

        

    
        




        
