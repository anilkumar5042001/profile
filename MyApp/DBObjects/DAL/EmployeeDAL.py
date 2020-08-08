from ..Entity.EmployeeEntity import *
from django.db import connection

class EmployeeDAL:
    def EmployeeInsert(self,ProfileId,ManagerId,RoleId,HrId,EUID):
        cursor = connection.cursor()
        args = [ProfileId,ManagerId,RoleId,HrId,EUID]
        cursor.callproc('Employee_Insert',args)
        EmployeeItem=cursor.fetchall()
        objEmployeeId=EmployeeItem[0][0]
        return objEmployeeId
        

    def GetEmployeeByProfileId(self,ProfileId):
        cursor = connection.cursor()
        args = [ProfileId]
        cursor.callproc('GetEmployee_ByProfileId',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for EmployeeItem in res:
            objEmployeeEntity=EmployeeEntity()
            objEmployeeEntity.EmployeeId=EmployeeItem[0]
            objEmployeeEntity.ProfileId=EmployeeItem[1]
            objEmployeeEntity.ManagerId=EmployeeItem[2]
            objEmployeeEntity.RoleId=EmployeeItem[3]
            objEmployeeEntity.HrId=EmployeeItem[4]
            objEmployeeEntity.EUID=EmployeeItem[5]
            arrayItems.append(objEmployeeEntity)
        return arrayItems

    def GetEmployeeByEmployeeId(self,EmployeeId):
        cursor = connection.cursor()
        args = [EmployeeId]
        cursor.callproc('GetEmployee_ByEmployeeId',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for EmployeeItem in res:
            objEmployeeEntity=EmployeeEntity()
            objEmployeeEntity.EmployeeId=EmployeeItem[0]
            objEmployeeEntity.ProfileId=EmployeeItem[1]
            objEmployeeEntity.ManagerId=EmployeeItem[2]
            objEmployeeEntity.RoleId=EmployeeItem[3]
            objEmployeeEntity.HrId=EmployeeItem[4]
            objEmployeeEntity.EUID=EmployeeItem[5]
            arrayItems.append(objEmployeeEntity)
        return arrayItems
    
    def GetEmployeeByManagerId(self,ManagerId):
        cursor = connection.cursor()
        args = [ManagerId]
        cursor.callproc('GetEmployee_ByManagerId',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for EmployeeItem in res:
            objEmployeeEntity=EmployeeEntity()
            objEmployeeEntity.EmployeeId=EmployeeItem[0]
            objEmployeeEntity.ProfileId=EmployeeItem[1]
            objEmployeeEntity.ManagerId=EmployeeItem[2]
            objEmployeeEntity.RoleId=EmployeeItem[3]
            objEmployeeEntity.HrId=EmployeeItem[4]
            objEmployeeEntity.EUID=EmployeeItem[5]
            arrayItems.append(objEmployeeEntity)
        return arrayItems

    def GetEmployeeByRoleId(self,RoleId):
        cursor = connection.cursor()
        args = [RoleId]
        cursor.callproc('GetEmployee_ByRoleId',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for EmployeeItem in res:
            objEmployeeEntity=EmployeeEntity()
            objEmployeeEntity.EmployeeId=EmployeeItem[0]
            objEmployeeEntity.ProfileId=EmployeeItem[1]
            objEmployeeEntity.ManagerId=EmployeeItem[2]
            objEmployeeEntity.RoleId=EmployeeItem[3]
            objEmployeeEntity.HrId=EmployeeItem[4]
            objEmployeeEntity.EUID=EmployeeItem[5]
            arrayItems.append(objEmployeeEntity)
        return arrayItems
    
    def GetEmployeeByHrId(self,HrId):
        cursor = connection.cursor()
        args = [HrId]
        cursor.callproc('GetEmployee_ByHrId',args)
        res =  cursor.fetchall()
        arrayItems=[]
        for EmployeeItem in res:
            objEmployeeEntity=EmployeeEntity()
            objEmployeeEntity.EmployeeId=EmployeeItem[0]
            objEmployeeEntity.ProfileId=EmployeeItem[1]
            objEmployeeEntity.ManagerId=EmployeeItem[2]
            objEmployeeEntity.RoleId=EmployeeItem[3]
            objEmployeeEntity.HrId=EmployeeItem[4]
            objEmployeeEntity.EUID=EmployeeItem[5]
            arrayItems.append(objEmployeeEntity)
        return arrayItems
    
    def EmployeeGetAll(self):
        cursor = connection.cursor()
        cursor.callproc('Employee_GetAll')
        res =  cursor.fetchall()
        arrayItems=[]
        for EmployeeItem in res:
            objEmployeeEntity=EmployeeEntity()
            objEmployeeEntity.EmployeeId=EmployeeItem[0]
            objEmployeeEntity.ProfileId=EmployeeItem[1]
            objEmployeeEntity.ManagerId=EmployeeItem[2]
            objEmployeeEntity.RoleId=EmployeeItem[3]
            objEmployeeEntity.HrId=EmployeeItem[4]
            objEmployeeEntity.EUID=EmployeeItem[5]
            arrayItems.append(objEmployeeEntity)
        return arrayItems

    def EmployeeUpdate(self,EmployeeId,ProfileId,ManagerId,RoleId,HrId,EUID):
        cursor = connection.cursor()
        args = [EmployeeId,ProfileId,ManagerId,RoleId,HrId,EUID]
        cursor.callproc('Employee_Update',args)
        return 1

    def EmployeeDelete(self,EmployeeId):
        cursor = connection.cursor()
        args = [EmployeeId]
        cursor.callproc('Employee_Delete',args)
        return 1
