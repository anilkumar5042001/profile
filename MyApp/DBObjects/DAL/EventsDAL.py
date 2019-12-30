# from ..Entity.EventyEntity import *
# from django.db import connection
# from datetime import datetime
# from ..Entity.UserProfileEntity import *

# class EventDAL:
#     def EventInsert(self,ProfileId,EventCategoryId,EventName,Description):
#         cursor=connection.cursor()
#         args=[ProfileId,EventCategoryId,EventName,Description,]
#         cursor.callproc('Event_Insert',args)
#         EventItem=cursor.fetchall()
#         objEventId=EventItem[0][0]
#         return objStoryId

#     def GetEventById(self,EventId):
#         cursor=connection.cursor()
#         args=[EventId]
#         cursor.callproc('Event_GetById',args)
#         res=cursor.fetchall()
#         arrayItems=[]
#         for EventItem in res:
#             objEventEntity=EventEntity()
#             objEventEntity.EventId=EventItem[0]
#             objEventEntity.ProfileId=EventItem[1]
#             objEventEntity.EventName=EventItem[2]
#             objEventEntity.Description=EventItem[3]
#             objEventEntity.EventCategoryId=EventItem[6]
#             arrayItems.append(objEventEntity)
#         return arrayItems 

#     def GetEventByProfileId(self,ProfileId):
#         cursor = connection.cursor()
#         args = [ProfileId]
#         cursor.callproc('GetEvent_ByProfileId',args)
#         res =  cursor.fetchall()
#         arrayItems=[]
#         for EventItem in res:
#             objEventEntity=EventEntity()
#             objEventEntity.EventId=EventItem[0]
#             objEventEntity.ProfileId=EventItem[1]
#             objEventEntity.EventName=EventItem[2]
#             objEventEntity.Description=EventItem[3]
#             objEventEntity.EventCategoryId=EventItem[6]

#             arrayItems.append(objEventEntity)
#         return arrayItems 
#     def EventUpdate(self,EventId,EventCategoryId,ProfileId,EventName,Description):
#         cursor=connection.cursor()
#         args=[EventId,ProfileId,EventCategoryId,EventName,Description,]
#         cursor.callproc('Event_Update',args)
#         return 1
    
#     def EventrDelete(self,EventId):
#         cursor = connection.cursor()
#         args = [EventId]
#         cursor.callproc('Event_Delete',args)
#         return 1
