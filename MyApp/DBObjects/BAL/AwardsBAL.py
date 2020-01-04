from ..DAL.AwardsDAL import AwardsDAL

class AwardsBAL:
    def AwardsInsert(self,ProfileId,AwardTitle,AwardDescription,AssignTo):
        objAwardsDAL=AwardsDAL()
        return objAwardsDAL.AwardsInsert(ProfileId,AwardTitle,AwardDescription,AssignTo)

    def GetAwardsByProfileId(self,ProfileId):
        objAwardsDAL=AwardsDAL()
        return objAwardsDAL.GetAwardsByProfileId(ProfileId)

    def GetAwardsByAssignTo(self,assignTo):
        objAwardsDAL=AwardsDAL()
        return objAwardsDAL.GetAwardsByAssignTo(assignTo)
    
    def GetAwardsById(self,AwardId):
        objAwardsDAL=AwardsDAL()
        return objAwardsDAL.GetAwardsById(AwardId)

    def AwardsUpdate(self,AwardId,ProfileId,AwardTitle,AwardDescription):
        objAwardsDAL=AwardsDAL()
        return objAwardsDAL.AwardsUpdate(AwardId,ProfileId,AwardTitle,AwardDescription)
    
    def AwardsUpdateShowInProfile(self,AwardId,ShowInProfile):
        objAwardsDAL=AwardsDAL()
        return objAwardsDAL.AwardsUpdateShowInProfile(AwardId,ShowInProfile)

    def AwardsDelete(self,AwardId):
        objAwardsDAL=AwardsDAL()
        return objAwardsDAL.AwardsDelete(AwardId)