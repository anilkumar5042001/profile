from ..DAL.RegistrationDAL import RegistrationDAL

class RegistrationBAL:
    def RegistrationInsert(self,EmailId,Password):
        objRegistrationDAL=RegistrationDAL()
        return objRegistrationDAL.RegistrationInsert(EmailId,Password)

    def GetRegistrationById(self,RegistrationId):
        objRegistrationDAL=RegistrationDAL()
        return objRegistrationDAL.GetRegistrationeById(RegistrationId)

    def RegistrationUpdate(self,RegistrationId,EmailId,Password):
        objRegistrationDAL=RegistrationDAL()
        return objRegistrationDAL.RegistrationUpdate(RegistrationId,EmailId,Password)


    