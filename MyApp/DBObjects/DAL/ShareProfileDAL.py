from ..Entity.ShareProfileEntity import *
from django.db import connection


class ShareProfileDAL:
    def ShareProfileInsert(self,ProfileId,EmailId,ProfileLink,ExpiryDate,SharedWith,Message):
        cursor = connection.cursor()
        args = [ProfileId,EmailId,ProfileLink,ExpiryDate,SharedWith,Message]
        cursor.callproc('ShareProfile_Insert',args)
        return 1

    def ShareProfileGetProfileIdByProfileLink(self,profileLink):
        db_name = connection.settings_dict['NAME']
        cursor = connection.cursor()
        args = [profileLink]
        cursor.callproc('ShareProfile_GetProfileIdByProfileLink',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for certItem in res:
            objShareProfileEntity=ShareProfileEntity()
            objShareProfileEntity.ProfileId=certItem[0]
            objShareProfileEntity.EmailId=certItem[1]
            objShareProfileEntity.ProfileLink=certItem[2]
            objShareProfileEntity.SharedWith=certItem[3]
            objShareProfileEntity.Message=certItem[4]
            arrayItems.append(objShareProfileEntity)
        return arrayItems  

