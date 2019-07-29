from ..DAL.WorkHistoryDAL import WorkHistoryDAL

class WorkHistoryBAL:
    def WorkHistoryInsert(self,ProfileId,CompanyName,Role,Description,City,Country,StartDate,EndDate):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.WorkHistoryInsert(ProfileId,CompanyName,Role,Description,City,Country,StartDate,EndDate)
    
    def WorkHistoryGetById(self,WorkHistoryId):
        objWorkHistoryDAL=WorkHistoryDAL()
        return objWorkHistoryDAL.WorkHistoryGetById(WorkHistoryId)