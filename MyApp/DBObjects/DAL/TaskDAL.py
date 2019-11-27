from ..Entity.TaskEntity import *
from django.db import connection
from datetime import datetime
from ..Entity.UserProfileEntity import *

class TaskDAL:
    def TaskInsert(self,ProfileId,TaskTitle,Description,DueDate,AssignTo,CreatedBy,TaskStatus):
        cursor=connection.cursor()
        args=[ProfileId,TaskTitle,Description,DueDate,AssignTo,CreatedBy,TaskStatus]
        cursor.callproc('Task_Insert',args)
        TaskItem=cursor.fetchall()
        objTaskId=TaskItem[0][0]
        return objTaskId

    def GetTaskByTaskId(self,TaskId):
        cursor=connection.cursor()
        args=[TaskId]
        cursor.callproc('GetTask_ByTaskId',args)
        res=cursor.fetchall()
        arrayItems=[]
        for TaskItem in res:
            objTaskEntity=TaskEntity()
            objTaskEntity.TaskId=TaskItem[0]
            objTaskEntity.ProfileId=TaskItem[1]
            objTaskEntity.TaskTitle=TaskItem[2]
            objTaskEntity.Description=TaskItem[3]
            objTaskEntity.DueDate=TaskItem[4].strftime("%m/%d/%Y")
            objTaskEntity.AssignTo=TaskItem[5]
            objTaskEntity.CreatedBy=TaskItem[6]
            objTaskEntity.TaskStatus=TaskItem[7]
            arrayItems.append(objTaskEntity)
        return arrayItems 

    def GetTaskByAssignTo(self,AssignTo):
        cursor=connection.cursor()
        args=[AssignTo]
        cursor.callproc('GetTask_ByAssignTo',args)
        res=cursor.fetchall()
        arrayItems=[]
        for TaskItem in res:
            objTaskEntity=TaskEntity()
            objTaskEntity.TaskId=TaskItem[0]
            objTaskEntity.ProfileId=TaskItem[1]
            objTaskEntity.TaskTitle=TaskItem[2]
            objTaskEntity.Description=TaskItem[3]
            objTaskEntity.DueDate=TaskItem[4].strftime("%m/%d/%Y")
            objTaskEntity.AssignTo=TaskItem[5]
            objTaskEntity.CreatedBy=TaskItem[6]
            objTaskEntity.TaskStatus=TaskItem[7]
            arrayItems.append(objTaskEntity)
        return arrayItems 

    def TaskUpdate(self,TaskId,ProfileId,TaskTitle,Description,DueDate,AssignTo,CreatedBy,TaskStatus):
        cursor=connection.cursor()
        args=[TaskId,ProfileId,TaskTitle,Description,DueDate,AssignTo,CreatedBy,TaskStatus]
        cursor.callproc('Task_Update',args)
        return 1
    
    def GetUserNameForAssignTo(self):
        cursor=connection.cursor()
        cursor.callproc('Get_Users')
        res=cursor.fetchall()
        arrayItems=[]
        for UserItem in res:
            objUserProfileEntity=UserProfileEntity()
            objUserProfileEntity.ProfileId=UserItem[0]
            objUserProfileEntity.FirstName=UserItem[1]
            objUserProfileEntity.LastName=UserItem[2]
            arrayItems.append(objUserProfileEntity)
        return arrayItems 