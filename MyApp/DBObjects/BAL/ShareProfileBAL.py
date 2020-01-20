from ..DAL.ShareProfileDAL import ShareProfileDAL

class ShareProfileBAL:
    def ShareProfileInsert(self,ProfileId,EmailId,ProfileLink,ExpiryDate,SharedWith,Message):
        objShareProfileDAL=ShareProfileDAL()
        return objShareProfileDAL.ShareProfileInsert(ProfileId,EmailId,ProfileLink,ExpiryDate,SharedWith,Message)
