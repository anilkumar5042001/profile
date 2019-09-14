from ..DAL.WorkHistoryDAL import WorkHistoryDAL

class WorkHistoryBAL:
    def WorkHistoryInsert(self,ProfileId,CompanyName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.WorkHistoryInsert(ProfileId,CompanyName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking)
    
    def WorkHistoryGetById(self,WorkHistoryId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.WorkHistoryGetById(WorkHistoryId)

    def WorkHistoryUpdate(self,ProfileId,WorkHistoryId,CompanyName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.WorkHistoryUpdate(ProfileId,WorkHistoryId,CompanyName,Role,Description,City,Country,StartMonth,StartYear,EndMonth,EndYear,CurrentlyWorking)

    def ProjectHighlightsInsert(self,WorkHistoryId,ProjectHighlightsDescription):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ProjectHighlightsInsert(WorkHistoryId,ProjectHighlightsDescription)
    
    def ProjectHighlightsGetById(self,WorkHistoryId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ProjectHighlightsGetById(WorkHistoryId)

    def ProjectHighlightsUpdate(self,ProjectHighlightsId,WorkHistoryId,ProjectHighlightsDescription):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ProjectHighlightsUpdate(ProjectHighlightsId,WorkHistoryId,ProjectHighlightsDescription)   

    def ResponsibilitiesInsert(self,ResponsibilitiesId,WorkHistoryId,ResponsibilitiesDescription):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ResponsibilitiesInsert(ResponsibilitiesId,WorkHistoryId,ResponsibilitiesDescription) 

    def ResponsibilitiesGetById(self,WorkHistoryId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ResponsibilitiesGetById(WorkHistoryId)

    def ResponsibilitiesUpdate(self,ResponsibilitiesId,WorkHistoryId,ResponsibilitiesDescription):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.ResponsibilitiesUpdate(ResponsibilitiesId,WorkHistoryId,ResponsibilitiesDescription)     