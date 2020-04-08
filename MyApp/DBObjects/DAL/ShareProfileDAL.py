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
        res=cursor.fetchall()
        objShareProfileEntity=ShareProfileEntity()        
        objShareProfileEntity.ProfileId=res[0][0]
        return objShareProfileEntity


