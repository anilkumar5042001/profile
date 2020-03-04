from ..DAL.TaskCommentDAL import TaskCommentDAL

class TaskCommentBAL:
    def TaskCommentInsert(self,ProfileId,TaskId,Comment,CommentedBy,CommentedOn):
        objTaskCommentDAL=TaskCommentDAL()
        return objTaskCommentDAL.TaskCommentInsert(ProfileId,TaskId,Comment,CommentedBy,CommentedOn)

    def GetTaskCommentByProfileId(self,ProfileId):
        objTaskCommentDAL=TaskCommentDAL()
        return objTaskCommentDAL.GetTaskCommentByProfileId(ProfileId)

    def TaskCommentDelete(self,TaskCommentId):
        objTaskCommentDAL=TaskCommentDAL()
        return objTaskCommentDAL.TaskCommentDelete(TaskCommentId)