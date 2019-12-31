
from ..DAL.EventsDAL import EventDAL

class EventBAL:
    def EventInsert(self,ProfileId,EventCategoryId,EventName,Description):
        objEventDAL=EventDAL()
        return objEventDAL.EventInsert(ProfileId,EventCategoryId,EventName,Description)

    def GetEventByProfileId(self,ProfileId):
        objEventDAL=EventDAL()
        return objEventDAL.GetEventByProfileId(ProfileId)

    def GetEventById(self,EventId):
        objEventDAL=EventDAL()
        return objEventDAL.GetEventById(EventId)

    def EventUpdate(self,EventId,ProfileId,EventCategoryId,EventName,Description):
        objEventDAL=EventDAL()
        return objEventDAL.EventUpdate(EventId,ProfileId,EventCategoryId,EventName,Description)

    def EventDelete(self,EventId):
        objEventDAL=EventDAL()
        return objEventDAL.EventDelete(EventId)

        
