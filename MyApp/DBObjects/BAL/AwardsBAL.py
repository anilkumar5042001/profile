from ..DAL.AwardsDAL import AwardsDAL

class AwardsBAL:
    def AwardsInsert(self,ProfileId,AwardTitle,AwardDescription):
        objAwardsDAL=AwardsDAL()
        return objAwardsDAL.AwardsInsert(ProfileId,AwardTitle,AwardDescription)

    def GetAwardsById(self,ProfileId):
        objAwardsDAL=AwardsDAL()
        return objAwardsDAL.GetAwardsById(ProfileId)

    def AwardsUpdate(self,AwardId,ProfileId,AwardTitle,AwardDescription):
        objAwardsDAL=AwardsDAL()
        return objAwardsDAL.AwardsUpdate(AwardId,ProfileId,AwardTitle,AwardDescription)

    def AwardsDelete(self,AwardId):
        objAwardsDAL=AwardsDAL()
        return objAwardsDAL.AwardsDelete(AwardId)