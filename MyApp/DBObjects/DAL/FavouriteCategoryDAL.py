from ..Entity.FavouriteCategoryEntity import *
from django.db import connection

class FavouriteCategoryDAL:
    def FavouriteCategoryInsert(self,ProfileId,FavouriteCategoryName):
        cursor = connection.cursor()
        args = [ProfileId,FavouriteCategoryName]
        cursor.callproc('FavouriteCategory_Insert',args)
        FavCategoryItem = cursor.fetchall()
        objFavCategoryId=FavCategoryItem[0][0]
        return objFavCategoryId

    def GetFavouriteCategoryById(self,FavouriteCategoryId):
        cursor = connection.cursor()
        args = [FavouriteCategoryId]
        cursor.callproc('GetFavouriteCategory_ById',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for FavouriteCategoryItem in res:
            objFavouriteCategoryEntity=FavouriteCategoryEntity()
            objFavouriteCategoryEntity.FavouriteCategoryId=FavouriteCategoryItem[0]
            objFavouriteCategoryEntity.ProfileId=FavouriteCategoryItem[1]
            objFavouriteCategoryEntity.FavouriteCategoryName=FavouriteCategoryItem[2]
            arrayItems.append(objFavouriteCategoryEntity)
        return arrayItems

    def GetFavouriteCategoryByProfileId(self,ProfileId):
        cursor = connection.cursor()
        args = [ProfileId]
        cursor.callproc('GetFavouriteCategory_ByProfileId',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for FavouriteCategoryItem in res:
            objFavouriteCategoryEntity=FavouriteCategoryEntity()
            objFavouriteCategoryEntity.FavouriteCategoryId=FavouriteCategoryItem[0]
            objFavouriteCategoryEntity.ProfileId=FavouriteCategoryItem[1]
            objFavouriteCategoryEntity.FavouriteCategoryName=FavouriteCategoryItem[2]
            arrayItems.append(objFavouriteCategoryEntity)
        return arrayItems

    def FavouriteCategoryUpdate(self,FavouriteCategoryId,ProfileId,FavouriteCategoryName):
        cursor = connection.cursor()
        args = [FavouriteCategoryId,ProfileId,FavouriteCategoryName]
        cursor.callproc('FavouriteCategory_Update',args)
        return 1

    def FavouriteCategoryDelete(self,FavouriteCategoryId):
        cursor = connection.cursor()
        args = [FavouriteCategoryId]
        cursor.callproc('FavouriteCategory_Delete',args)
        return 1
