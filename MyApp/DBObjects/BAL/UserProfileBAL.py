
from ..DAL.UserProfileDAL import UserProfileDAL

class UserProfileBAL:
    def GetUserProfileById(self,profileId):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.GetUserProfileById(profileId)

    def GetUserProfile(self):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.GetUserProfile()

    
    def UserProfileInsert(self,firstName,lastName,emailId,phoneNumber,education,designation,City,Country,aboutMe,Password,CompanyDomain):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.UserProfileInsert(firstName,lastName,emailId,phoneNumber,education,designation,City,Country,aboutMe,Password,CompanyDomain)  

    def UserProfileUpdate(self,profileId,firstName,lastName,emailId,phoneNumber,education,designation,City,Country,AboutMe,profileImageName):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.UserProfileUpdate(profileId,firstName,lastName,emailId,phoneNumber,education,designation,City,Country,AboutMe,profileImageName) 

    def UserProfileUpdateDomainName(self,profileId,companyDomain):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.UserProfileUpdateDomainName(profileId,companyDomain)     

    def UserProfileGetByCompanyDomain(self,companyDomain):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.UserProfileGetByCompanyDomain(companyDomain)  
    
    def UserProfileUpdateAboutMe(self,profileId,aboutMe):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.UserProfileUpdateAboutMe(profileId,aboutMe) 

    def UserLoginCheckCredentials(self,EmailId,Password):
        objUserProfileDAL=UserProfileDAL()
        res = objUserProfileDAL.UserLoginCheckCredentials(EmailId,Password)
        return res