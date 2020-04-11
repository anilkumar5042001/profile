from ..DAL.TaskDAL import TaskDAL


class TaskBAL:
    def TaskInsert(self,TaskCategoryId,ProfileId,TaskTitle,Description,DueDate,AssignTo,CreatedBy,TaskStatus,TaskDuration,TaskOrder):
        objTaskDAL=TaskDAL()
        return objTaskDAL.TaskInsert(TaskCategoryId,ProfileId,TaskTitle,Description,DueDate,AssignTo,CreatedBy,TaskStatus,TaskDuration,TaskOrder)

    def GetTaskByTaskId(self,TaskId):
        objTaskDAL=TaskDAL()
        return objTaskDAL.GetTaskByTaskId(TaskId)

    def GetTaskByProfileId(self,ProfileId):
        objTaskDAL=TaskDAL()
        return objTaskDAL.GetTaskByProfileId(ProfileId)

    def GetTaskByAssignTo(self,AssignTo):
        objTaskDAL=TaskDAL()
        return objTaskDAL.GetTaskByAssignTo(AssignTo)

    def TaskUpdate(self,TaskId,TaskCategoryId,ProfileId,TaskTitle,Description,DueDate,AssignTo,CreatedBy,TaskStatus,TaskDuration,TaskOrder):
        objTaskDAL=TaskDAL()
        return objTaskDAL.TaskUpdate(TaskId,TaskCategoryId,ProfileId,TaskTitle,Description,DueDate,AssignTo,CreatedBy,TaskStatus,TaskDuration,TaskOrder)
    
    def GetUserNameForAssignTo(self):
        objTaskDAL=TaskDAL()
        return objTaskDAL.GetUserNameForAssignTo()
    
    def TaskDelete(self,TaskId):
        objTaskDAL=TaskDAL()
        return objTaskDAL.TaskDelete(TaskId)

    def GetAllTasks(self,FromDueDate,ToDueDate,AssignTo,TaskStatus,ProfileId):
        objTaskDAL=TaskDAL()
        return objTaskDAL.GetAllTasks(FromDueDate,ToDueDate,AssignTo,TaskStatus,ProfileId)