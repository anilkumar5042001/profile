from ..DAL.SkillCategoryDAL import SkillCategoryDAL

class SkillCategoryBAL:
    def SkillsCategoryInsert(self,ProfileId,SkillCategoryName):
        objSkillCategoryDAL=SkillCategoryDAL()
        return objSkillCategoryDAL.SkillsCategoryInsert(ProfileId,SkillCategoryName)

    def GetSkillsCategoryByProfileId(self,ProfileId):
        objSkillCategoryDAL=SkillCategoryDAL()
        return objSkillCategoryDAL.GetSkillsCategoryByProfileId(ProfileId)
    
    def GetSkillsCategoryById(self,SkillCategoryId):
        objSkillCategoryDAL=SkillCategoryDAL()
        return objSkillCategoryDAL.GetSkillsCategoryById(SkillCategoryId)

    def SkillsCategoryUpdate(self,SkillCategoryId,ProfileId,SkillCategoryName):
        objSkillCategoryDAL=SkillCategoryDAL()
        return objSkillCategoryDAL.SkillsCategoryUpdate(SkillCategoryId,ProfileId,SkillCategoryName)

    def SkillsCategoryDelete(self,SkillCategoryId):
        objSkillCategoryDAL=SkillCategoryDAL()
        return objSkillCategoryDAL.SkillsCategoryDelete(SkillCategoryId)