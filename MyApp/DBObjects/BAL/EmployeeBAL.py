from ..DAL.EmployeeDAL import EmployeeDAL
import csv
from django.db import connection

class EmployeeBAL:
    def InsertEmployee(self,fileName):
        #result="a"
        #result = open(os.path.expanduser('media/Emp/cbc.csv')).read()
        fileName='/home/anil5042001/profile/media/'+fileName
        with open(fileName) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                print(row[0],row[1])
                cursor = connection.cursor()
                args = [row[0],row[1]]
                cursor.callproc('Interest_Insert',args)


    def EmployeeInsert(self,ProfileId,ManagerId,RoleId,HrId,EUID):
        objEmployeeDAL=EmployeeDAL()
        return objEmployeeDAL.EmployeeInsert(ProfileId,ManagerId,RoleId,HrId,EUID)

    def GetEmployeeByProfileId(self,ProfileId):
        objEmployeeDAL=EmployeeDAL()
        return objEmployeeDAL.GetEmployeeByProfileId(ProfileId)

    def GetEmployeeByEmployeeId(self,EmployeeId):
        objEmployeeDAL=EmployeeDAL()
        return objEmployeeDAL.GetEmployeeByEmployeeId(EmployeeId)
    
    def GetEmployeeByManagerId(self,ManagerId):
        objEmployeeDAL=EmployeeDAL()
        return objEmployeeDAL.GetEmployeeByManagerId(ManagerId)

    def GetEmployeeByRoleId(self,RoleId):
        objEmployeeDAL=EmployeeDAL()
        return objEmployeeDAL.GetEmployeeByRoleId(RoleId)
    
    def GetEmployeeByHrId(self,HrId):
        objEmployeeDAL=EmployeeDAL()
        return objEmployeeDAL.GetEmployeeByHrId(HrId)
    
    def EmployeeGetAll(self):
        objEmployeeDAL=EmployeeDAL()
        return objEmployeeDAL.EmployeeGetAll()

    def EmployeeUpdate(self,EmployeeId,ProfileId,ManagerId,RoleId,HrId,EUID):
        objEmployeeDAL=EmployeeDAL()
        return objEmployeeDAL.EmployeeUpdate(EmployeeId,ProfileId,ManagerId,RoleId,HrId,EUID)

    def EmployeeDelete(self,EmployeeId):
        objEmployeeDAL=EmployeeDAL()
        return objEmployeeDAL.EmployeeDelete(EmployeeId)



