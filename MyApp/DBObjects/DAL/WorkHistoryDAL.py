from ..Entity.WorkHistoryEntity import *
from django.db import connection


class WorkHistoryDAL:
    def WorkHistoryInsert(self,ProfileId,CompanyName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking):
        cursor = connection.cursor()
        args = [ProfileId,CompanyName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking]
        cursor.callproc('WorkHistory_Insert',args)
        return 1
    
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
            objProjectHighlightsEntity.ProjectHighlightsId=ProjectHighlightsItem[0]
            objProjectHighlightsEntity.WorkHistoryId=ProjectHighlightsItem[1]
            objProjectHighlightsEntity.ProjectHighlightsDescription=ProjectHighlightsItem[2]
            arrayItems.append(objProjectHighlightsEntity)
        return arrayItems 

    def ProjectHighlightsUpdate(self,ProjectHighlightsId,WorkHistoryId,ProjectHighlightsDescription):
        cursor = connection.cursor()
        args = [ProjectHighlightsId,WorkHistoryId,ProjectHighlightsDescription]
        cursor.callproc('ProjectHighlights_Update',args)
        return 1

    def ResponsibilitiesInsert(self,ResponsibilitiesId,WorkHistoryId,ResponsibilitiesDescription):
        cursor = connection.cursor()
        args = [ResponsibilitiesId,WorkHistoryId,ResponsibilitiesDescription]
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
            objResponsibilitiesEntity.ResponsibilitiesDescription=ResponsibilitiesItem[2]
            arrayItems.append(objResponsibilitiesEntity)
        return arrayItems 

    def ResponsibilitiesUpdate(self,ResponsibilitiesId,WorkHistoryId,ResponsibilitiesDescription):
        cursor = connection.cursor()
        args = [ResponsibilitiesId,WorkHistoryId,ResponsibilitiesDescription]
        cursor.callproc('Responsibilities_Update',args)
        return 1

        

    
        




        
