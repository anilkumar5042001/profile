from ..Entity.WorkHistoryEntity import *
from django.db import connection


class WorkHistoryDAL:
    def WorkHistoryInsert(self,ProfileId,ProjectName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking,CompanyEmailId,WHGuid,VerificationCode,IsVerified,CompanyId):
        cursor = connection.cursor()
        args = [ProfileId,ProjectName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking,CompanyEmailId,WHGuid,VerificationCode,IsVerified,CompanyId]
        cursor.callproc('WorkHistory_Insert',args)
        workHistoryItem =  cursor.fetchall()
        workHistoryId=workHistoryItem[0][0]
        return workHistoryId
        
    
    def CertificationGetByProfileId(self,profileId):
        db_name = connection.settings_dict['NAME']
        cursor = connection.cursor()
        args = [profileId]
        cursor.callproc('Certification_GetByProfileId',args)

    def WorkHistoryUpdate(self,ProfileId,WorkHistoryId,ProjectName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking,CompanyEmailId,CompanyId):
        cursor = connection.cursor()
        args = [ProfileId,WorkHistoryId,ProjectName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking,CompanyEmailId,CompanyId]
        cursor.callproc('WorkHistory_Update',args)
        return 1
        
    
    def GetWorkHistoryByProfileId(self,ProfileId):
        cursor = connection.cursor()
        args = [ProfileId]
        cursor.callproc('WorkHistory_GetByProfileId',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for WorkHistoryItem in res:
            objWorkHistoryEntity=WorkHistoryEntity()
            objWorkHistoryEntity.ProfileId=WorkHistoryItem[0]
            objWorkHistoryEntity.WorkHistoryId=WorkHistoryItem[1]
            objWorkHistoryEntity.CompanyName=WorkHistoryItem[2]
            objWorkHistoryEntity.ProjectName=WorkHistoryItem[3]
            objWorkHistoryEntity.Role=WorkHistoryItem[4]
            objWorkHistoryEntity.Description=WorkHistoryItem[5]
            objWorkHistoryEntity.City=WorkHistoryItem[6]
            objWorkHistoryEntity.Country=WorkHistoryItem[7]
            objWorkHistoryEntity.StartMonth=WorkHistoryItem[8]
            objWorkHistoryEntity.StartYear=WorkHistoryItem[9]
            objWorkHistoryEntity.EndMonth=WorkHistoryItem[10]
            objWorkHistoryEntity.EndYear=WorkHistoryItem[11]            
            objWorkHistoryEntity.CurrentlyWorking=WorkHistoryItem[12]
            objWorkHistoryEntity.CompanyEmailId=WorkHistoryItem[13]
            objWorkHistoryEntity.WHGuid=WorkHistoryItem[14]
            objWorkHistoryEntity.VerificationCode=WorkHistoryItem[15]
            objWorkHistoryEntity.IsVerified=WorkHistoryItem[16]
            objWorkHistoryEntity.CompanyId=WorkHistoryItem[17]
            objWorkHistoryEntity.Logo=WorkHistoryItem[18]
            objWorkHistoryEntity.DomainName=WorkHistoryItem[19]
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
            objWorkHistoryEntity.ProjectName=WorkHistoryItem[3]
            objWorkHistoryEntity.Role=WorkHistoryItem[4]
            objWorkHistoryEntity.Description=WorkHistoryItem[5]
            objWorkHistoryEntity.City=WorkHistoryItem[6]
            objWorkHistoryEntity.Country=WorkHistoryItem[7]
            objWorkHistoryEntity.StartMonth=WorkHistoryItem[8]
            objWorkHistoryEntity.StartYear=WorkHistoryItem[9]
            objWorkHistoryEntity.EndMonth=WorkHistoryItem[10]
            objWorkHistoryEntity.EndYear=WorkHistoryItem[11]            
            objWorkHistoryEntity.CurrentlyWorking=WorkHistoryItem[12]
            objWorkHistoryEntity.CompanyEmailId=WorkHistoryItem[13]
            objWorkHistoryEntity.WSGuid=WorkHistoryItem[14]
            objWorkHistoryEntity.VerificationCode=WorkHistoryItem[15]
            objWorkHistoryEntity.IsVerified=WorkHistoryItem[16]
            objWorkHistoryEntity.CompanyId=WorkHistoryItem[17]
            arrayItems.append(objWorkHistoryEntity)

        cursor.close() 
        return arrayItems

    def GetWorkHistoryByProfileIdAndCompanyId(self,ProfileId,CompanyId):
        cursor = connection.cursor()
        args = [ProfileId,CompanyId]
        cursor.callproc('WorkHistory_ByProfileIdAndCompanyId',args)
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
            objWorkHistoryEntity.CurrentlyWorking=WorkHistoryItem[11]
            objWorkHistoryEntity.ProjectName=WorkHistoryItem[12]
            objWorkHistoryEntity.CompanyEmailId=WorkHistoryItem[13]
            objWorkHistoryEntity.CompanyId=WorkHistoryItem[14]
            arrayItems.append(objWorkHistoryEntity)
        return arrayItems  

    def WorkHistoryDelete(self,WorkHistoryId):
        cursor = connection.cursor()
        args = [WorkHistoryId]
        cursor.callproc('WorkHistory_Delete',args)
        return 1

    def WorkHistoryUpdateVerificationCode(self,WHGuid,VerificationCode):
        cursor = connection.cursor()
        args = [WHGuid,VerificationCode]
        cursor.callproc('WorkHistory_UpdateVerificationCode',args)
        res=cursor.fetchall()
        objWorkHistoryEntity=WorkHistoryEntity()        
        objWorkHistoryEntity.ProfileId=res[0][0]
        return objWorkHistoryEntity

    def WorkHistoryUpdateVerificationCodeById(self,WorkHistoryId,WHGuid,VerificationCode,IsVerified):
        cursor = connection.cursor()
        args = [WorkHistoryId,WHGuid,VerificationCode,IsVerified]
        cursor.callproc('WorkHistory_UpdateVerificationCodeById',args)
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

        

    
        




        
