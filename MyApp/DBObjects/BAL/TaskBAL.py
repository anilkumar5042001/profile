from ..DAL.TaskDAL import TaskDAL

class TaskBAL:
    def TaskInsert(self,ProfileId,TaskTitle,Description,DueDate,AssignTo,CreatedBy,TaskStatus):
        objTaskDAL=TaskDAL()
        return objTaskDAL.TaskInsert(ProfileId,TaskTitle,Description,DueDate,AssignTo,CreatedBy,TaskStatus)

    def GetTaskByTaskId(self,TaskId):
        objTaskDAL=TaskDAL()
        return objTaskDAL.GetTaskByTaskId(TaskId)

    def GetTaskByAssignTo(self,AssignTo):
        objTaskDAL=TaskDAL()
        return objTaskDAL.GetTaskByAssignTo(AssignTo)

    def TaskUpdate(self,TaskId,ProfileId,TaskTitle,Description,DueDate,AssignTo,CreatedBy,TaskStatus):
        objTaskDAL=TaskDAL()
        return objTaskDAL.TaskUpdate(TaskId,ProfileId,TaskTitle,Description,DueDate,AssignTo,CreatedBy,TaskStatus)