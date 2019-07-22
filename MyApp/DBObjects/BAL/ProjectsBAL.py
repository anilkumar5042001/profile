from ..DAL.ProjectsDAL import ProjectsDAL

class ProjectsBAL:
    def ProjectInsert(self,ProfileId,ProjectName,ProjectDescription,Role,StartYear,EndYear,Responsibilities,Awards):
        objUserProfileDAL=UserProfileDAL()
        objProjectsDAL=ProjectsDAL
        return objProjectsDAL.ProjectInsert(ProfileId,ProjectName,ProjectDescription,Role,StartYear,EndYear,Responsibilities,Awards) 