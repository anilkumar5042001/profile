from ..DAL.WorkHistoryDAL import WorkHistoryDAL
from ..Helper.EmailTemplate import *
from .CommonMethodsBAL import *
import uuid

class WorkHistoryBAL:
    def WorkHistoryInsert(self,ProfileId,CompanyName,ProjectName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking,CompanyEmailId):
        VerificationCode=""
        WHGuid=""
        IsVerified=0
        
        if CurrentlyWorking=="1":
            uid = uuid.uuid4()
            WHGuid=uid.hex
            VerificationCode=WHGuid[0:4]
            objCommonMethodsBAL=CommonMethodsBAL()
            objEmailTemplate=EmailTemplate()
            strLink="https://boring-rosalind-5ae0ce.netlify.com/whverification/"+WHGuid
            verificationEmailTemplate=objEmailTemplate.GetWorkHistoryVerificationEmail(WHGuid,VerificationCode)
            objCommonMethodsBAL.SendMail(CompanyEmailId,"Company Verification Email",verificationEmailTemplate)

        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.WorkHistoryInsert(ProfileId,CompanyName,ProjectName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking,CompanyEmailId,WHGuid,VerificationCode,IsVerified)
    
    def WorkHistoryGetById(self,WorkHistoryId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.WorkHistoryGetById(WorkHistoryId)

    def GetWorkHistoryByProfileId(self,ProfileId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.GetWorkHistoryByProfileId(ProfileId)

    def GetWorkHistoryByProfileIdAndCompanyName(self,ProfileId,CompanyName):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.GetWorkHistoryByProfileIdAndCompanyName(ProfileId,CompanyName)

    def WorkHistoryUpdate(self,ProfileId,WorkHistoryId,CompanyName,ProjectName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking,CompanyEmailId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.WorkHistoryUpdate(ProfileId,WorkHistoryId,CompanyName,ProjectName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking,CompanyEmailId)

    def WorkHistoryDelete(self,WorkHistoryId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.WorkHistoryDelete(WorkHistoryId)

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