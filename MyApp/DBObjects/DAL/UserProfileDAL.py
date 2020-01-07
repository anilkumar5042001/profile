from ..Entity.UserProfileEntity import *
from django.db import connection

class UserProfileDAL:
    # def GetUserProfile(self):
    #     cursor = connection.cursor()
    #     query = """select * from UserProfile;"""
    #     cursor.execute(query)
    #     res =  cursor.fetchall()
    #     UserProfile=[]

    #     for r in res:
    #         objUserProfileEntity=UserProfileEntity()
    #         objUserProfileEntity.FirstName=r[0]
    #         objUserProfileEntity.LastName=r[1]
    #         objUserProfileEntity.EmailId=r[2]
    #         objUserProfileEntity.PhoneNumber=r[3]
            
    #         UserProfile.append(objUserProfileEntity)

    #     return UserProfile

    def GetUserProfileById(self,profileId):
        db_name = connection.settings_dict['NAME']
        print(db_name)
        cursor = connection.cursor()
        args = [profileId]
        cursor.callproc('UserProfile_GetById',args)
        res =  cursor.fetchall()
        objUserProfileEntity=UserProfileEntity()
        objUserProfileEntity.ProfileId=res[0][0]
        objUserProfileEntity.FirstName=res[0][1]
        objUserProfileEntity.LastName=res[0][2]
        objUserProfileEntity.EmailId=res[0][3]
        objUserProfileEntity.PhoneNumber=res[0][4]
        objUserProfileEntity.Education=res[0][5]
        objUserProfileEntity.Designation=res[0][6]
        objUserProfileEntity.City=res[0][7]
        objUserProfileEntity.Country=res[0][8]
        objUserProfileEntity.AboutMe=res[0][9]
        objUserProfileEntity.CompanyDomain=res[0][10]
        objUserProfileEntity.ProfileImageName=res[0][11]
        return objUserProfileEntity  

    def UserProfileGetByCompanyDomain(self,companyDomain):
        db_name = connection.settings_dict['NAME']
        cursor = connection.cursor()
        args = [companyDomain]
        cursor.callproc('UserProfile_GetByCompanyDomain',args)
        results =  cursor.fetchall()
        arrayItems=[]
        for res in results:
            objUserProfileEntity=UserProfileEntity()
            objUserProfileEntity.ProfileId=res[0]
            objUserProfileEntity.FirstName=res[1]
            objUserProfileEntity.LastName=res[2]
            objUserProfileEntity.EmailId=res[3]
            objUserProfileEntity.PhoneNumber=res[4]
            objUserProfileEntity.Education=res[5]
            objUserProfileEntity.Designation=res[6]
            objUserProfileEntity.City=res[7]
            objUserProfileEntity.Country=res[8]
            objUserProfileEntity.AboutMe=res[9]
            objUserProfileEntity.CompanyDomain=res[10]
            arrayItems.append(objUserProfileEntity)
        return arrayItems  

    def UserProfileInsert(self,firstName,lastName,emailId,phoneNumber,education,designation,City,Country,aboutMe,Password,CompanyDomain):
        cursor = connection.cursor()
        args = [firstName,lastName,emailId,phoneNumber,education,designation,City,Country,aboutMe,Password,CompanyDomain]
        cursor.callproc('UserProfile_Insert',args)
        return 1

    def UserProfileUpdateDomainName(self,profileId,companyDomain):
        cursor = connection.cursor()
        args = [profileId,companyDomain]
        cursor.callproc('UserProfile_UpdateDomainName',args)
        return 1

    def UserProfileUpdate(self,ProfileId,firstName,lastName,emailId,phoneNumber,education,designation,City,Country,AboutMe,profileImageName):
        cursor = connection.cursor()
        args = [ProfileId,firstName,lastName,emailId,phoneNumber,education,designation,City,Country,AboutMe,profileImageName]
        cursor.callproc('UserProfile_Update',args)
        return 1
    def UserProfileUpdateAboutMe(self,ProfileId,aboutMe):
        cursor = connection.cursor()
        args = [ProfileId,aboutMe]
        cursor.callproc('UserProfile_UpdateAboutMe',args)
        return 1

    def UserLoginCheckCredentials(self,EmailId,Password):
        cursor = connection.cursor()
        args = [EmailId,Password]
        cursor.callproc('CheckLoginCredentials',args)
        res=cursor.fetchall()
        objUserProfileEntity=UserProfileEntity()        
        objUserProfileEntity.ProfileId=res[0][0]
        return objUserProfileEntity
        
