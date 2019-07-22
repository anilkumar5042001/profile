
from ..DAL.UserProfileDAL import UserProfileDAL

class UserProfileBAL:
    def GetUserProfileById(self,profileId):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.GetUserProfileById(profileId)

    def GetUserProfile(self):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.GetUserProfile()

    
    def UserProfileInsert(self,firstName,lastName,emailId,phoneNumber,education,designation):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.UserProfileInsert(firstName,lastName,emailId,phoneNumber,education,designation)  

    def UserProfileUpdate(self,profileId,firstName,lastName,emailId,phoneNumber,education,designation):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.UserProfileUpdate(profileId,firstName,lastName,emailId,phoneNumber,education,designation) 