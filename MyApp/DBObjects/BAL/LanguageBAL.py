from ..DAL.LanguageDAL import LanguageDAL

class LanguageBAL:
    def LanguageInsert(self,ProfileId,LanguageName,LanguageLevel):
        objLanguageDAL=LanguageDAL()
        return objLanguageDAL.LanguageInsert(ProfileId,LanguageName,LanguageLevel)

    def GetLanguageById(self,ProfileId):
        objLanguageDAL=LanguageDAL()
        return objLanguageDAL.GetLanguageById(ProfileId)

    def LanguageUpdate(self,LanguageId,ProfileId,LanguageName,LanguageLevel):
        objLanguageDAL=LanguageDAL()
        return objLanguageDAL.LanguageUpdate(LanguageId,ProfileId,LanguageName,LanguageLevel)

    def LanguageDelete(self,LanguageId):
        objLanguageDAL=LanguageDAL()
        return objLanguageDAL.LanguageDelete(LanguageId)

    