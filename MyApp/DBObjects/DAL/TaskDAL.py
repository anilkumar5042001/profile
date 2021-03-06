from ..Entity.TaskEntity import *
from django.db import connection
from datetime import datetime
from ..Entity.UserProfileEntity import *
import decimal

class TaskDAL:
    def TaskInsert(self,TaskCategoryId,ProfileId,TaskTitle,Description,DueDate,AssignTo,CreatedBy,TaskStatus,TaskDuration,TaskOrder):
        cursor=connection.cursor()
        args=[TaskCategoryId,ProfileId,TaskTitle,Description,DueDate,AssignTo,CreatedBy,TaskStatus,TaskDuration,TaskOrder]
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
            objTaskEntity.TaskCategoryId=TaskItem[1]
            objTaskEntity.ProfileId=TaskItem[2]
            objTaskEntity.TaskTitle=TaskItem[3]
            objTaskEntity.Description=TaskItem[4]
            objTaskEntity.DueDate=TaskItem[5].strftime("%m/%d/%Y %H:%M:%S")
            # objTaskEntity.DueDate=TaskItem[4].strftime("%m/%d/%Y")
            objTaskEntity.AssignTo=TaskItem[6]
            objTaskEntity.CreatedBy=TaskItem[7]
            objTaskEntity.TaskStatus=TaskItem[8]
            objTaskEntity.TaskDuration=str(decimal.Decimal(TaskItem[9]))
            objTaskEntity.TaskOrder=TaskItem[10]
            arrayItems.append(objTaskEntity)
        return arrayItems 
    
    def GetTaskByProfileId(self,ProfileId):
        cursor=connection.cursor()
        args=[ProfileId]
        cursor.callproc('GetTask_ByProfileId',args)
        res=cursor.fetchall()
        arrayItems=[]
        for TaskItem in res:
            objTaskEntity=TaskEntity()
            objTaskEntity.TaskId=TaskItem[0]
            objTaskEntity.TaskCategoryId=TaskItem[1]
            objTaskEntity.ProfileId=TaskItem[2]
            objTaskEntity.TaskTitle=TaskItem[3]
            objTaskEntity.Description=TaskItem[4]
            objTaskEntity.DueDate=TaskItem[5].strftime("%d/%m/%Y %H:%M:%S")           
            objTaskEntity.AssignTo=TaskItem[6]
            objTaskEntity.CreatedBy=TaskItem[7]
            objTaskEntity.TaskStatus=TaskItem[8]
            objTaskEntity.TaskDuration=str(decimal.Decimal(TaskItem[9]))
            objTaskEntity.TaskOrder=TaskItem[10]
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
            objTaskEntity.DueDate=TaskItem[4].strftime("%d/%m/%Y %H:%M:%S")
            objTaskEntity.AssignTo=TaskItem[5]
            objTaskEntity.CreatedBy=TaskItem[6]
            objTaskEntity.TaskStatus=TaskItem[7]
            objTaskEntity.TaskDuration=str(decimal.Decimal(TaskItem[8]))
            objTaskEntity.NewCommentCount=TaskItem[9]
            objTaskEntity.TaskOrder=TaskItem[10]
            objTaskEntity.TaskCategoryId=TaskItem[11]
            arrayItems.append(objTaskEntity)
        return arrayItems 

    def TaskUpdate(self,TaskId,TaskCategoryId,ProfileId,TaskTitle,Description,DueDate,AssignTo,CreatedBy,TaskStatus,TaskDuration,TaskOrder):
        cursor=connection.cursor()
        args=[TaskId,TaskCategoryId,ProfileId,TaskTitle,Description,DueDate,AssignTo,CreatedBy,TaskStatus,TaskDuration,TaskOrder]
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
            objUserProfileEntity.ProfileImageName=UserItem[3]
            objUserProfileEntity.EmailId=UserItem[4]
            objUserProfileEntity.Designation=UserItem[5]
            arrayItems.append(objUserProfileEntity)
        return arrayItems 
    
    def TaskDelete(self,TaskId):
        cursor = connection.cursor()
        args = [TaskId]
        cursor.callproc('Task_Delete',args)
        return 1

    def GetAllTasks(self,FromDueDate,ToDueDate,AssignTo,TaskStatus,ProfileId):
        cursor=connection.cursor()
        args = [FromDueDate,ToDueDate,AssignTo,TaskStatus,ProfileId]
        cursor.callproc('Task_All',args)
        res=cursor.fetchall()
        arrayItems=[]
        for TaskItem in res:
            objTaskEntity=TaskEntity()
            objTaskEntity.TaskId=TaskItem[0]
            objTaskEntity.TaskCategoryId=TaskItem[1]
            objTaskEntity.ProfileId=TaskItem[2]
            objTaskEntity.TaskTitle=TaskItem[3]
            objTaskEntity.Description=TaskItem[4]
            objTaskEntity.DueDate=TaskItem[5].strftime("%d/%m/%Y %H:%M:%S")           
            objTaskEntity.AssignTo=TaskItem[6]
            objTaskEntity.CreatedBy=TaskItem[7]
            objTaskEntity.TaskStatus=TaskItem[8]
            objTaskEntity.TaskDuration=str(decimal.Decimal(TaskItem[9]))
            objTaskEntity.AssignToFullName=TaskItem[10]
            objTaskEntity.CreatedByFullName=TaskItem[11]
            objTaskEntity.AssignToProfileImageName=TaskItem[12]
            objTaskEntity.CreatedByProfileImageName=TaskItem[13]
            objTaskEntity.TaskOrder=TaskItem[14]
            arrayItems.append(objTaskEntity)
        return arrayItems