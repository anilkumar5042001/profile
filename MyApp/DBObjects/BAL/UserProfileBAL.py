
from ..DAL.UserProfileDAL import UserProfileDAL

class UserProfileBAL:
    def GetUserProfileById(self,ProfileId):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.GetUserProfileById(ProfileId)

    def GetUserProfile(self):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.GetUserProfile() 