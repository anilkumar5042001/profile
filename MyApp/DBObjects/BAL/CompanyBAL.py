from ..DAL.CompanyDAL import CompanyDAL

class CompanyBAL:
    def CompanyGetAll(self):
        objCompanyDAL=CompanyDAL()
        return objCompanyDAL.CompanyGetAll()
    
    def CompanyInsert(self,CompanyName,DomainName,Logo,EmailId,Password):
        objCompanyDAL=CompanyDAL()
        return objCompanyDAL.CompanyInsert(CompanyName,DomainName,Logo,EmailId,Password)