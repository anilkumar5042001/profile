from ..DAL.CompanyDAL import CompanyDAL

class CompanyBAL:
    def CompanyGetAll(self):
        objCompanyDAL=CompanyDAL()
        return objCompanyDAL.CompanyGetAll()