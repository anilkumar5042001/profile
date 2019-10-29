
from ..DAL.UserProfileDAL import UserProfileDAL

class UserProfileBAL:
    def GetUserProfileById(self,profileId):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.GetUserProfileById(profileId)

    def GetUserProfile(self):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.GetUserProfile()

    
    def UserProfileInsert(self,firstName,lastName,emailId,phoneNumber,education,designation,aboutMe):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.UserProfileInsert(firstName,lastName,emailId,phoneNumber,education,designation,aboutMe)  

    def UserProfileUpdate(self,profileId,firstName,lastName,emailId,phoneNumber,education,designation,AboutMe):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.UserProfileUpdate(profileId,firstName,lastName,emailId,phoneNumber,education,designation,AboutMe) 
    
    def UserProfileUpdateAboutMe(self,profileId,aboutMe):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.UserProfileUpdateAboutMe(profileId,aboutMe) 