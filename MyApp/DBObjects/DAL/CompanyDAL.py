from ..Entity.CompanyEntity import *
from django.db import connection

class CompanyDAL:
    def CompanyGetAll(self):
        cursor = connection.cursor()
        cursor.callproc('Company_GetAll')
        res =  cursor.fetchall()
        arrayItems=[]
        for CompanyItem in res:
            objCompanyEntity=CompanyEntity()
            objCompanyEntity.CompanyId=CompanyItem[0]
            objCompanyEntity.CompanyName=CompanyItem[1]
            objCompanyEntity.DomainName=CompanyItem[2]
            objCompanyEntity.Logo=CompanyItem[3]  
            objCompanyEntity.EmailId=CompanyItem[4]         
            objCompanyEntity.Password=CompanyItem[5]
            arrayItems.append(objCompanyEntity)
        return arrayItems
    
    def CompanyInsert(self,CompanyName,DomainName,Logo,EmailId,Password):
        cursor=connection.cursor()
        args=[CompanyName,DomainName,Logo,EmailId,Password]
        cursor.callproc('Company_Insert',args)
        EventItem=cursor.fetchall()
        objEventId=EventItem[0][0]
        return objEventId
        
