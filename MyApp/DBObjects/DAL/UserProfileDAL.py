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
        objUserProfileEntity.AboutMe=res[0][7]
        return objUserProfileEntity  

    def UserProfileInsert(self,firstName,lastName,emailId,phoneNumber,education,designation,aboutMe):
        cursor = connection.cursor()
        args = [firstName,lastName,emailId,phoneNumber,education,designation,aboutMe]
        cursor.callproc('UserProfile_Insert',args)
        return 1

    def UserProfileUpdate(self,ProfileId,firstName,lastName,emailId,phoneNumber,education,designation):
        cursor = connection.cursor()
        args = [ProfileId,firstName,lastName,emailId,phoneNumber,education,designation]
        cursor.callproc('UserProfile_Update',args)
        return 1
    def UserProfileUpdateAboutMe(self,ProfileId,aboutMe):
        cursor = connection.cursor()
        args = [ProfileId,aboutMe]
        cursor.callproc('UserProfile_UpdateAboutMe',args)
        return 1
