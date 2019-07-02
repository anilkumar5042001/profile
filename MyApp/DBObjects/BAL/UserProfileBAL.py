
from ..DAL.UserProfileDAL import UserProfileDAL

class UserProfileBAL:
    def GetUserProfileById(self,profileId):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.GetUserProfileById(profileId)

    def GetUserProfile(self):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.GetUserProfile() 