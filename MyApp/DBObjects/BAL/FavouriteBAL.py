from ..DAL.FavouriteDAL import  FavouriteDAL

class FavouriteBAL:
    def FavouriteInsert(self,ProfileId,FavouriteCategoryId,FavouriteName,FavouriteLink):
        objFavouriteDAL=FavouriteDAL()
        return objFavouriteDAL.FavouriteInsert(ProfileId,FavouriteCategoryId,FavouriteName,FavouriteLink)

    def GetFavouriteByProfileId(self,ProfileId):
        objFavouriteDAL=FavouriteDAL()
        return objFavouriteDAL.GetFavouriteByProfileId(ProfileId)

    def GetFavouriteById(self,FavouriteId):
        objFavouriteDAL=FavouriteDAL()
        return objFavouriteDAL.GetFavouriteById(FavouriteId)

    def FavouriteUpdate(self,FavouriteId,ProfileId,FavouriteCategoryId,FavouriteName,FavouriteLink,):
        objFavouriteDAL=FavouriteDAL()
        return objFavouriteDAL.FavouriteUpdate(FavouriteId,ProfileId,FavouriteCategoryId,FavouriteName,FavouriteLink)

    def FavouriteDelete(self,FavouriteId):
        objFavouriteDAL=FavouriteDAL()
        return objFavouriteDAL.FavouriteDelete(FavouriteId)

        
