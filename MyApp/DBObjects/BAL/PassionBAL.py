from ..DAL.PassionDAL import PassionDAL

class PassionBAL:
    def PassionInsert(self,ProfileId,PassionName,Description):
        objPassionDAL=PassionDAL()
        return objPassionDAL.PassionInsert(ProfileId,PassionName,Description)

    def GetPassionByProfileId(self,ProfileId):
        objPassionDAL=PassionDAL()
        return objPassionDAL.GetPassionByProfileId(ProfileId)

    def GetPassionById(self,PassionId):
        objPassionDAL=PassionDAL()
        return objPassionDAL.GetPassionById(PassionId)

    def PassionUpdate(self,PassionId,ProfileId,PassionName,Description):
        objPassionDAL=PassionDAL()
        return objPassionDAL.PassionUpdate(PassionId,ProfileId,PassionName,Description)

    def PassionDelete(self,PassionId):
        objPassionDAL=PassionDAL()
        return objPassionDAL.PassionDelete(PassionId)

        
