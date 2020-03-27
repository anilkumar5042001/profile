
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

    
    def UserProfileInsert(self,firstName,lastName,emailId,phoneNumber,education,designation,City,Country,aboutMe,Password,CompanyDomain,RegGuid,ActivationCode,IsActivated):
        objCommonMethodsBAL=CommonMethodsBAL()
        uid = uuid.uuid4()
        strRegGuid=uid.hex
        actCode=strRegGuid[0:4]
        objCommonMethodsBAL.SendHTMLMail(emailId,"https://boring-rosalind-5ae0ce.netlify.com/Activation/"+strRegGuid,"Please enter activation code: "+actCode)
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.UserProfileInsert(firstName,lastName,emailId,phoneNumber,education,designation,City,Country,aboutMe,Password,CompanyDomain,strRegGuid,actCode,IsActivated)

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
    
    def UserProfileUpdateRegCode(self,RegGuid,ActivationCode):
        objUserProfileDAL=UserProfileDAL()
        return objUserProfileDAL.UserProfileUpdateRegCode(RegGuid,ActivationCode)