from ..DAL.SkillsDAL import SkillsDAL

class SkillsBAL:
    def SkillsInsert(self,ProfileId,SkillCategoryId,SkillName):
        objSkillsDAL=SkillsDAL()
        return objSkillsDAL.SkillsInsert(ProfileId,SkillCategoryId,SkillName)

    def GetSkillsByProfileId(self,ProfileId):
        objSkillsDAL=SkillsDAL()
        return objSkillsDAL.GetSkillsByProfileId(ProfileId)
    
    def GetSkillsById(self,SkillId):
        objSkillsDAL=SkillsDAL()
        return objSkillsDAL.GetSkillsById(SkillId)

    def SkillsUpdate(self,SkillId,ProfileId,SkillCategoryId,SkillName):
        objSkillsDAL=SkillsDAL()
        return objSkillsDAL.SkillsUpdate(SkillId,ProfileId,SkillCategoryId,SkillName)

    def SkillsDelete(self,SkillId):
        objSkillsDAL=SkillsDAL()
        return objSkillsDAL.SkillsDelete(SkillId)