from ..DAL.TaskDAL import TaskDAL

class TaskBAL:
    def TaskInsert(self,ProfileId,TaskTitle,Description,DueDate,AssignTo,CreatedBy,TaskStatus,TaskDuration):
        objTaskDAL=TaskDAL()
        return objTaskDAL.TaskInsert(ProfileId,TaskTitle,Description,DueDate,AssignTo,CreatedBy,TaskStatus,TaskDuration)

    def GetTaskByTaskId(self,TaskId):
        objTaskDAL=TaskDAL()
        return objTaskDAL.GetTaskByTaskId(TaskId)

    def GetTaskByProfileId(self,ProfileId):
        objTaskDAL=TaskDAL()
        return objTaskDAL.GetTaskByProfileId(ProfileId)

    def GetTaskByAssignTo(self,AssignTo):
        objTaskDAL=TaskDAL()
        return objTaskDAL.GetTaskByAssignTo(AssignTo)

    def TaskUpdate(self,TaskId,ProfileId,TaskTitle,Description,DueDate,AssignTo,CreatedBy,TaskStatus,TaskDuration):
        objTaskDAL=TaskDAL()
        return objTaskDAL.TaskUpdate(TaskId,ProfileId,TaskTitle,Description,DueDate,AssignTo,CreatedBy,TaskStatus,TaskDuration)
    
    def GetUserNameForAssignTo(self):
        objTaskDAL=TaskDAL()
        return objTaskDAL.GetUserNameForAssignTo()
    
    def TaskDelete(self,TaskId):
        objTaskDAL=TaskDAL()
        return objTaskDAL.TaskDelete(TaskId)

    def GetAllTasks(self):
        objTaskDAL=TaskDAL()
        return objTaskDAL.GetAllTasks()