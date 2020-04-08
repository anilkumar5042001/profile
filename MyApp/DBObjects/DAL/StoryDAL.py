from ..Entity.StoryEntity import *
from django.db import connection
from datetime import datetime


class StoryDAL:
    def StoryInsert(self,ProfileId,StoryCategoryId,StoryTitle,Description,Thumbnail,IsPublished,StoryDate):
        cursor=connection.cursor()
        args=[ProfileId,StoryCategoryId,StoryTitle,Description,Thumbnail,IsPublished,StoryDate]
        cursor.callproc('Story_Insert',args)
        StoryItem=cursor.fetchall()
        objStoryId=StoryItem[0][0]
        return objStoryId

    def StoryDelete(self,StoryId):
        cursor=connection.cursor()
        args=[StoryId]
        cursor.callproc('Story_Delete',args)
        return 1

    def GetStoryById(self,StoryId):
        cursor=connection.cursor()
        args=[StoryId]
        cursor.callproc('Story_GetById',args)
        res=cursor.fetchall()
        arrayItems=[]
        for StoryItem in res:
            objStoryEntity=StoryEntity()
            objStoryEntity.StoryId=StoryItem[0]
            objStoryEntity.ProfileId=StoryItem[1]
            objStoryEntity.StoryCategoryId=StoryItem[2]
            objStoryEntity.StoryTitle=StoryItem[3]
            objStoryEntity.Description=StoryItem[4]
            objStoryEntity.Thumbnail=StoryItem[5]
            objStoryEntity.IsPublished=StoryItem[6]
            # objStoryEntity.StoryDate=StoryItem[7]
            objStoryEntity.StoryDate=StoryItem[7].strftime("%m/%d/%Y %H:%M:%S")
            arrayItems.append(objStoryEntity)
        return arrayItems 

    def GetStoryByProfileId(self,ProfileId):
        cursor = connection.cursor()
        args = [ProfileId]
        cursor.callproc('GetStory_ByProfileId',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for StoryItem in res:
            objStoryEntity=StoryEntity()
            objStoryEntity.StoryId=StoryItem[0]
            objStoryEntity.ProfileId=StoryItem[1]
            objStoryEntity.StoryCategoryId=StoryItem[2]
            objStoryEntity.StoryTitle=StoryItem[3]
            objStoryEntity.Description=StoryItem[4]
            objStoryEntity.Thumbnail=StoryItem[5]
            objStoryEntity.IsPublished=StoryItem[6]
            # objStoryEntity.StoryDate=StoryItem[7]
            objStoryEntity.StoryDate=StoryItem[7].strftime("%m/%d/%Y %H:%M:%S")            
            arrayItems.append(objStoryEntity)
        return arrayItems 

    def StoryUpdate(self,StoryId,ProfileId,StoryCategoryId,StoryTitle,Description,Thumbnail,IsPublished,StoryDate):
        cursor=connection.cursor()
        args=[StoryId,ProfileId,StoryCategoryId,StoryTitle,Description,Thumbnail,IsPublished,StoryDate]
        cursor.callproc('Story_Update',args)
        return 1
    
    