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

    def GetUserProfileById(self,ProfileId):

        cursor = connection.cursor()
        query = """select * from UserProfile;"""
        cursor.execute(query)

        objUserProfileEntity=UserProfileEntity()
        objUserProfileEntity.FirstName="test"
        objUserProfileEntity.LastName="one"
        objUserProfileEntity.EmailId="testone@gmail.com"
        objUserProfileEntity.PhoneNumber="12345"

        return objUserProfileEntity  

