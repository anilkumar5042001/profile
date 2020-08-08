
from ..DAL.UserProfileDAL import UserProfileDAL
from ..BAL.CommonMethodsBAL import CommonMethodsBAL
import uuid

class UserProfileBAL:
    def GetUserProfileById(self,profileId):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.GetUserProfileById(profileId)

    def GetUserProfile(self):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.GetUserProfile()

    
    def UserProfileInsert(self,firstName,lastName,emailId,phoneNumber,education,designation,City,Country,aboutMe,Password,CompanyDomain,RegGuid,ActivationCode,IsActivated,CountryId):
        objCommonMethodsBAL=CommonMethodsBAL()
        uid = uuid.uuid4()
        strRegGuid=uid.hex
        actCode=strRegGuid[0:4]
        objCommonMethodsBAL.SendActivationEmail(emailId,"https://boring-rosalind-5ae0ce.netlify.com/Activation/"+strRegGuid,actCode)
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.UserProfileInsert(firstName,lastName,emailId,phoneNumber,education,designation,City,Country,aboutMe,Password,CompanyDomain,strRegGuid,actCode,IsActivated,CountryId)

    def UserProfileUpdate(self,profileId,firstName,lastName,emailId,phoneNumber,education,designation,City,Country,AboutMe,profileImageName,CountryId):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.UserProfileUpdate(profileId,firstName,lastName,emailId,phoneNumber,education,designation,City,Country,AboutMe,profileImageName,CountryId) 

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

    def UserProfileGetProfileIdByEmailId(self,EmailId):
        objUserProfileDAL=UserProfileDAL()
        res = objUserProfileDAL.UserProfileGetProfileIdByEmailId(EmailId)
        return res
    
    def UserProfileUpdateRegCode(self,RegGuid,ActivationCode):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.UserProfileUpdateRegCode(RegGuid,ActivationCode)
    
    def UserProfileGetAll(self):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.UserProfileGetAll()