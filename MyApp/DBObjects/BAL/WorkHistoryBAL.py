from ..DAL.WorkHistoryDAL import WorkHistoryDAL

class WorkHistoryBAL:
    def WorkHistoryInsert(self,ProfileId,CompanyName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.WorkHistoryInsert(ProfileId,CompanyName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking)
    
    def WorkHistoryGetById(self,WorkHistoryId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.WorkHistoryGetById(WorkHistoryId)

    def GetWorkHistoryByProfileId(self,ProfileId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.GetWorkHistoryByProfileId(ProfileId)

    def GetWorkHistoryByProfileIdAndCompanyName(self,ProfileId,CompanyName):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.GetWorkHistoryByProfileIdAndCompanyName(ProfileId,CompanyName)

    def WorkHistoryUpdate(self,ProfileId,WorkHistoryId,CompanyName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.WorkHistoryUpdate(ProfileId,WorkHistoryId,CompanyName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking)

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