from ..Entity.ShareProfileEntity import *
from django.db import connection

class ShareProfileDAL:
    def ShareProfileInsert(self,ProfileId,EmailId,ProfileLink,ExpiryDate,SharedWith,Message):
        cursor = connection.cursor()
        args = [ProfileId,EmailId,ProfileLink,ExpiryDate,SharedWith,Message]
        cursor.callproc('ShareProfile_Insert',args)
        return 1

