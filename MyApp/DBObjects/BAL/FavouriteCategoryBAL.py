from ..DAL.FavouriteCategoryDAL import  FavouriteCategoryDAL

class FavouriteCategoryBAL:
    def FavouriteCategoryInsert(self,ProfileId,FavouriteCategoryName):
        objFavouriteCategoryDAL=FavouriteCategoryDAL()
        return objFavouriteCategoryDAL.FavouriteCategoryInsert(ProfileId,FavouriteCategoryName)

    def GetFavouriteCategoryByProfileId(self,ProfileId):
        objFavouriteCategoryDAL=FavouriteCategoryDAL()
        return objFavouriteCategoryDAL.GetFavouriteCategoryByProfileId(ProfileId)

    def GetFavouriteCategoryById(self,FavouriteCategoryId):
        objFavouriteCategoryDAL=FavouriteCategoryDAL()
        return objFavouriteCategoryDAL.GetFavouriteCategoryById(FavouriteCategoryId)

    def FavouriteCategoryUpdate(self,FavouriteCategoryId,ProfileId,FavouriteCategoryName):
        objFavouriteCategoryDAL=FavouriteCategoryDAL()
        return objFavouriteCategoryDAL.FavouriteCategoryUpdate(FavouriteCategoryId,ProfileId,FavouriteCategoryName)

    def FavouriteCategoryDelete(self,FavouriteCategoryId):
        objFavouriteCategoryDAL=FavouriteCategoryDAL()
        return objFavouriteCategoryDAL.FavouriteCategoryDelete(FavouriteCategoryId)