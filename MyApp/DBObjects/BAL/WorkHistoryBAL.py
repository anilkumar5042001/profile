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

    def WorkHistoryUpdate(self,ProfileId,WorkHistoryId,CompanyName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.WorkHistoryUpdate(ProfileId,WorkHistoryId,CompanyName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking)

    def WorkHistoryDelete(self,WorkHistoryId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.WorkHistoryDelete(WorkHistoryId)

    def ProjectHighlightsInsert(self,WorkHistoryId,ProjectHighlightsDescription):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ProjectHighlightsInsert(WorkHistoryId,ProjectHighlightsDescription)
    
    def ProjectHighlightsGetById(self,WorkHistoryId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ProjectHighlightsGetById(WorkHistoryId)

    def ProjectHighlightsUpdate(self,HighlightId,WorkHistoryId,ProjectHighlightsDescription):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ProjectHighlightsUpdate(HighlightId,WorkHistoryId,ProjectHighlightsDescription) 

    def ProjectHighlightsDelete(self,HighlightId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ProjectHighlightsDelete(HighlightId)  

    def ResponsibilitiesInsert(self,ResponsibilitiesId,WorkHistoryId,ResponsibilitiesDescription):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ResponsibilitiesInsert(ResponsibilitiesId,WorkHistoryId,ResponsibilitiesDescription) 

    def ResponsibilitiesGetById(self,WorkHistoryId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ResponsibilitiesGetById(WorkHistoryId)

    def ResponsibilitiesUpdate(self,ResponsibilitiesId,WorkHistoryId,ResponsibilitiesDescription):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ResponsibilitiesUpdate(ResponsibilitiesId,WorkHistoryId,ResponsibilitiesDescription)   

    def ResponsibilitiesDelete(self,ResponsibilitiesId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ResponsibilitiesDelete(ResponsibilitiesId)  