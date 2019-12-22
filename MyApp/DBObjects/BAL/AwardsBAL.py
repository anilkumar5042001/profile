from ..DAL.AwardsDAL import AwardsDAL

class AwardsBAL:
    def AwardsInsert(self,ProfileId,AwardTitle,AwardDescription,AssignTo):
        objAwardsDAL=AwardsDAL()
        return objAwardsDAL.AwardsInsert(ProfileId,AwardTitle,AwardDescription,AssignTo)

    def GetAwardsByProfileId(self,ProfileId):
        objAwardsDAL=AwardsDAL()
        return objAwardsDAL.GetAwardsByProfileId(ProfileId)
    
    def GetAwardsById(self,AwardId):
        objAwardsDAL=AwardsDAL()
        return objAwardsDAL.GetAwardsById(AwardId)

    def AwardsUpdate(self,AwardId,ProfileId,AwardTitle,AwardDescription):
        objAwardsDAL=AwardsDAL()
        return objAwardsDAL.AwardsUpdate(AwardId,ProfileId,AwardTitle,AwardDescription)

    def AwardsDelete(self,AwardId):
        objAwardsDAL=AwardsDAL()
        return objAwardsDAL.AwardsDelete(AwardId)