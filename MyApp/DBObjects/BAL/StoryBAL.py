from ..DAL.StoryDAL import StoryDAL

class StoryBAL:
    def StoryInsert(self,ProfileId,StoryCategoryId,StoryTitle,Description,Thumbnail,IsPublished,StoryDate):
        objStoryDAL=StoryDAL()
        return objStoryDAL.StoryInsert(ProfileId,StoryCategoryId,StoryTitle,Description,Thumbnail,IsPublished,StoryDate)

    def GetStoryByProfileId(self,ProfileId):
        objStoryDAL=StoryDAL()
        return objStoryDAL.GetStoryByProfileId(ProfileId)

    def GetStoryById(self,StoryId):
        objStoryDAL=StoryDAL()
        return objStoryDAL.GetStoryById(StoryId)

    def StoryUpdate(self,StoryId,StoryCategoryId,ProfileId,StoryTitle,Description,Thumbnail,IsPublished,StoryDate):
        objStoryDAL=StoryDAL()
        return objStoryDAL.StoryUpdate(StoryId,StoryCategoryId,ProfileId,StoryTitle,Description,Thumbnail,IsPublished,StoryDate)

    def StoryDelete(self,StoryId):
        objStoryDAL=StoryDAL()
        return objStoryDAL.StoryDelete(StoryId)

        
