from ..DAL.TaskCommentDAL import TaskCommentDAL

class TaskCommentBAL:
    def TaskCommentInsert(self,ProfileId,TaskId,Comment,CommentedBy,CommentedOn):
        objTaskCommentDAL=TaskCommentDAL()
        return objTaskCommentDAL.TaskCommentInsert(ProfileId,TaskId,Comment,CommentedBy,CommentedOn)

    def TaskCommentUpdateIsNew(self,TaskId,ProfileId):
        objTaskCommentDAL=TaskCommentDAL()
        return objTaskCommentDAL.TaskCommentUpdateIsNew(TaskId,ProfileId)

    def GetTaskCommentByProfileId(self,ProfileId,Comment):
        objTaskCommentDAL=TaskCommentDAL()
        return objTaskCommentDAL.GetTaskCommentByProfileId(ProfileId,Comment)

    def GetTaskCommentByTaskId(self,TaskId):
        objTaskCommentDAL=TaskCommentDAL()
        return objTaskCommentDAL.GetTaskCommentByTaskId(TaskId)

    def TaskCommentDelete(self,TaskCommentId):
        objTaskCommentDAL=TaskCommentDAL()
        return objTaskCommentDAL.TaskCommentDelete(TaskCommentId)