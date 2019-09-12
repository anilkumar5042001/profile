from ..DAL.RegistrationDAL import RegistrationDAL

class RegistrationBAL:
    def RegistrationInsert(self,RegistrationId,EmailId,Password):
        objRegistrationDAL=RegistrationDAL()
        return objRegistrationDAL.RegistrationInsert(RegistrationId,EmailId,Password)

    def GetRegistrationById(self,RegistrationId):
        objRegistrationDAL=RegistrationDAL()
        return objRegistrationDAL.GetRegistrationById(RegistrationId)

    def RegistrationUpdate(self,RegistrationId,EmailId,Password):
        objRegistrationDAL=RegistrationDAL()
        return objRegistrationDAL.RegistrationUpdate(RegistrationId,EmailId,Password)


    