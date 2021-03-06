from ..Entity.TaskCommentEntity import *
from django.db import connection

class TaskCommentDAL:
    def TaskCommentInsert(self,ProfileId,TaskId,Comment,CommentedBy,CommentedOn):
        cursor = connection.cursor()
        args = [ProfileId,TaskId,Comment,CommentedBy,CommentedOn]
        cursor.callproc('TaskComment_Insert',args)
        TaskCommentItem=cursor.fetchall()
        objTaskCommentId=TaskCommentItem[0][0]
        return objTaskCommentId

    def TaskCommentUpdateIsNew(self,TaskId,ProfileId):
        cursor = connection.cursor()
        args = [TaskId,ProfileId]
        cursor.callproc('TaskComment_UpdateIsNew',args)
        TaskCommentItem=cursor.fetchall()
        return 1

    def GetTaskCommentByProfileId(self,ProfileId,Comment):
        cursor = connection.cursor()
        args = [ProfileId,Comment]
        cursor.callproc('GetTaskComment_ByProfileId',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for TaskCommentItem in res:
            objTaskCommentEntity=TaskCommentEntity()
            objTaskCommentEntity.TaskCommentId=TaskCommentItem[0]
            objTaskCommentEntity.ProfileId=TaskCommentItem[1]
            objTaskCommentEntity.TaskId=TaskCommentItem[2]
            objTaskCommentEntity.Comment=TaskCommentItem[3]
            objTaskCommentEntity.CommentedBy=TaskCommentItem[4]
            objTaskCommentEntity.CommentedOn=TaskCommentItem[5].strftime("%d/%m/%Y %H:%M:%S")
            arrayItems.append(objTaskCommentEntity)
        return arrayItems
    
    def GetTaskCommentByTaskId(self,TaskId):
        cursor = connection.cursor()
        args = [TaskId]
        cursor.callproc('GetTaskComment_ByTaskId',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for TaskCommentItem in res:
            objTaskCommentEntity=TaskCommentEntity()
            objTaskCommentEntity.TaskCommentId=TaskCommentItem[0]
            objTaskCommentEntity.ProfileId=TaskCommentItem[1]
            objTaskCommentEntity.TaskId=TaskCommentItem[2]
            objTaskCommentEntity.Comment=TaskCommentItem[3]
            objTaskCommentEntity.CommentedBy=TaskCommentItem[4]
            objTaskCommentEntity.CommentedOn=TaskCommentItem[5].strftime("%d/%m/%Y %H:%M:%S")
            objTaskCommentEntity.CommentedToFullName=TaskCommentItem[6]
            objTaskCommentEntity.CommentedByFullName=TaskCommentItem[7]
            objTaskCommentEntity.IsNew=TaskCommentItem[8]
            arrayItems.append(objTaskCommentEntity)
        return arrayItems

    def TaskCommentDelete(self,TaskCommentId):
        cursor = connection.cursor()
        args = [TaskCommentId]
        cursor.callproc('TaskComment_Delete',args)
        return 1
