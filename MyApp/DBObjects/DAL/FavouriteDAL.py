from ..Entity.FavouriteEntity import *
from django.db import connection

class FavouriteDAL:
    def FavouriteInsert(self,ProfileId,FavouriteCategoryId,FavouriteName,FavouriteLink):
        cursor=connection.cursor()
        args=[ProfileId,FavouriteCategoryId,FavouriteName,FavouriteLink]
        cursor.callproc('Favourite_Insert',args)
        FavouriteItem=cursor.fetchall()
        objFavouriteId=FavouriteItem[0][0]
        return objFavouriteId

    def GetFavouriteById(self,FavouriteId):
        cursor = connection.cursor()
        args = [FavouriteId]
        cursor.callproc('GetFavourite_ById',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for FavouriteItem in res:
            objFavouriteEntity=FavouriteEntity()
            objFavouriteEntity.FavouriteId=FavouriteItem[0]
            objFavouriteEntity.ProfileId=FavouriteItem[1]
            objFavouriteEntity.FavouriteName=FavouriteItem[2]
            objFavouriteEntity.FavouriteLink=FavouriteItem[3]
            objFavouriteEntity.FavouriteCategoryId=FavouriteItem[4]
            arrayItems.append(objFavouriteEntity)
        return arrayItems

    def GetFavouriteByProfileId(self,ProfileId):
        cursor = connection.cursor()
        args = [ProfileId]
        cursor.callproc('GetFavourite_ByProfileId',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for FavouriteItem in res:
            objFavouriteEntity=FavouriteEntity()
            objFavouriteEntity.FavouriteId=FavouriteItem[0]
            objFavouriteEntity.ProfileId=FavouriteItem[1]
            objFavouriteEntity.FavouriteCategoryId=FavouriteItem[2]
            objFavouriteEntity.FavouriteName=FavouriteItem[3]
            objFavouriteEntity.FavouriteLink=FavouriteItem[4]
            arrayItems.append(objFavouriteEntity)
        return arrayItems

    def FavouriteUpdate(self,FavouriteId,ProfileId,FavouriteCategoryId,FavouriteName,FavouriteLink):
        cursor = connection.cursor()
        args = [FavouriteId,ProfileId,FavouriteCategoryId,FavouriteName,FavouriteLink]
        cursor.callproc('Favourite_Update',args)
        return 1

    def FavouriteDelete(self,FavouriteId):
        cursor = connection.cursor()
        args = [FavouriteId]
        cursor.callproc('Favourite_Delete',args)
        return 1
