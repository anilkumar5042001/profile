from ..DAL.InterestDAL import InterestDAL

class InterestBAL:
    def InterestInsert(self,ProfileId,InterestName):
        objInterestDAL=InterestDAL()
        return objInterestDAL.InterestInsert(ProfileId,InterestName)

    def GetInterestById(self,InterestId):
        objInterestDAL=InterestDAL()
        return objInterestDAL.GetInterestById(InterestId)
    
    def GetInterestByProfileId(self,ProfileId):
        objInterestDAL=InterestDAL()
        return objInterestDAL.GetInterestByProfileId(ProfileId)

    def InterestUpdate(self,InterestId,ProfileId,InterestName):
        objInterestDAL=InterestDAL()
        return objInterestDAL.InterestUpdate(InterestId,ProfileId,InterestName)

    def InterestDelete(self,InterestId):
        objInterestDAL=InterestDAL()
        return objInterestDAL.InterestDelete(InterestId)
