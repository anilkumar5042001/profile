from ..Entity.ProjectEntity import *
from django.db import connection
  
class ProjectsDAL:  
    def ProjectInsert(self,ProfileId,ProjectName,ProjectDescription,Role,StartYear,EndYear,Responsibilities,Awards):
      cursor = connection.cursor()
      args = [ProfileId,ProjectName,ProjectDescription,Role,StartYear,EndYear,Responsibilities,Awards]
      cursor.callproc('Project_Insert',args)
      return 1