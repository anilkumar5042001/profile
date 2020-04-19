from ..DAL.WorkHistoryDAL import WorkHistoryDAL
from ..Helper.EmailTemplate import *
from .CommonMethodsBAL import *
import uuid
from ...GlobalConstants import *

class WorkHistoryBAL:
    def WorkHistoryInsert(self,ProfileId,ProjectName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking,CompanyEmailId,CompanyId,CountryId):
        workHistoryId=0
        IsVerified=0
        VerificationCode=""
        WHGuid=""

        if CurrentlyWorking=="1":
            uid = uuid.uuid4()
            WHGuid=uid.hex
            VerificationCode=WHGuid[0:4]

        objWorkHistoryDAL=WorkHistoryDAL()
        workHistoryId=objWorkHistoryDAL.WorkHistoryInsert(ProfileId,ProjectName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking,CompanyEmailId,WHGuid,VerificationCode,IsVerified,CompanyId,CountryId)
        if workHistoryId>0:
            if CurrentlyWorking=="1":
                objWorkHistoryBAL=WorkHistoryBAL()
                objWorkHistoryBAL.SendVerificationEmail(ProjectName,WHGuid,VerificationCode,CompanyEmailId)

        return workHistoryId

    def SendVerificationEmail(self,projectName,WHGuid,VerificationCode,CompanyEmailId):
        
        objCommonMethodsBAL=CommonMethodsBAL()
        objEmailTemplate=EmailTemplate()
        objGlobalConstants=GlobalConstants()
        strLink=objGlobalConstants.SiteUrl+"/"+objGlobalConstants.WHVerificationUrl+"/"+ WHGuid
        verificationEmailTemplate=objEmailTemplate.GetWorkHistoryVerificationEmail(strLink,VerificationCode)
        subject="Company Verification Email for project: "+projectName
        objCommonMethodsBAL.SendMail(CompanyEmailId,subject,verificationEmailTemplate)
    
    def WorkHistoryGetById(self,WorkHistoryId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.WorkHistoryGetById(WorkHistoryId)

    def GetWorkHistoryByProfileId(self,ProfileId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.GetWorkHistoryByProfileId(ProfileId)

    def WorkHistoryGetCurrentlyWorkingItem(self,ProfileId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.WorkHistoryGetCurrentlyWorkingItem(ProfileId)

    def GetWorkHistoryByProfileIdAndCompanyId(self,ProfileId,CompanyId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.GetWorkHistoryByProfileIdAndCompanyId(ProfileId,CompanyId)

    def WorkHistoryUpdate(self,ProfileId,WorkHistoryId,ProjectName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking,CompanyEmailId,CompanyId,CountryId):
        sucess=0
        isEmailIdChanged=False
        objWorkHistoryBAL=WorkHistoryBAL()
        if CurrentlyWorking=="1":
            objWorkHistoryItem=objWorkHistoryBAL.WorkHistoryGetById(WorkHistoryId)
            existingCompanyEmailId=objWorkHistoryItem[0].CompanyEmailId
            if existingCompanyEmailId!=CompanyEmailId:
                isEmailIdChanged=True

        objWorkHistoryDAL=WorkHistoryDAL()
        sucess=objWorkHistoryDAL.WorkHistoryUpdate(ProfileId,WorkHistoryId,ProjectName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking,CompanyEmailId,CompanyId,CountryId)

        if isEmailIdChanged==True:
            sucess=objWorkHistoryBAL.UpdateVerificationAndSendEmal(ProjectName,WorkHistoryId,CompanyEmailId)
        return sucess

    def UpdateVerificationAndSendEmal(self,ProjectName,WorkHistoryId,CompanyEmailId):
        VerificationCode=""
        WHGuid=""
        uid = uuid.uuid4()
        WHGuid=uid.hex
        VerificationCode=WHGuid[0:4]
        objWorkHistoryDAL=WorkHistoryDAL()
        success=objWorkHistoryDAL.WorkHistoryUpdateVerificationCodeById(WorkHistoryId,WHGuid,VerificationCode,"0")

        objWorkHistoryBAL=WorkHistoryBAL()
        objWorkHistoryBAL.SendVerificationEmail(ProjectName,WHGuid,VerificationCode,CompanyEmailId)
        success="2"

        return success
        
    def WorkHistoryDelete(self,WorkHistoryId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.WorkHistoryDelete(WorkHistoryId)

    def WorkHistoryUpdateVerificationCode(self,WHGuid,VerificationCode):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.WorkHistoryUpdateVerificationCode(WHGuid,VerificationCode)

    def ProjectHighlightsInsert(self,WorkHistoryId,Description):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ProjectHighlightsInsert(WorkHistoryId,Description)
    
    def ProjectHighlightsGetById(self,WorkHistoryId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ProjectHighlightsGetById(WorkHistoryId)

    def ProjectHighlightsUpdate(self,HighlightId,WorkHistoryId,Description):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ProjectHighlightsUpdate(HighlightId,WorkHistoryId,Description) 

    def ProjectHighlightsDelete(self,HighlightId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ProjectHighlightsDelete(HighlightId)  
    
    def ProjectHighlightsDeleteByWorkHistoryId(self,WorkHistoryId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ProjectHighlightsDeleteByWorkHistoryId(WorkHistoryId)

    def ResponsibilitiesInsert(self,WorkHistoryId,Description):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ResponsibilitiesInsert(WorkHistoryId,Description) 

    def ResponsibilitiesGetById(self,WorkHistoryId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ResponsibilitiesGetById(WorkHistoryId)

    def ResponsibilitiesUpdate(self,ResponsibilitiesId,WorkHistoryId,Description):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ResponsibilitiesUpdate(ResponsibilitiesId,WorkHistoryId,Description)   

    def ResponsibilitiesDelete(self,ResponsibilitiesId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ResponsibilitiesDelete(ResponsibilitiesId)
    
    def ResponsibilitiesDeleteByWorkHistoryId(self,WorkHistoryId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ResponsibilitiesDeleteByWorkHistoryId(WorkHistoryId) 