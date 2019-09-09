from ..DAL.CertificationDAL import CertificationDAL

class CertificationBAL:
    def CertificationInsert(self,ProfileId,CertificationName,Description):
        objCertificationDAL=CertificationDAL()
        return objCertificationDAL.CertificationInsert(ProfileId,CertificationName,Description)

    def CertificationUpdate(self,CertificationId,CertificationName,Description):
        objCertificationDAL=CertificationDAL()
        return objCertificationDAL.CertificationUpdate(CertificationId,CertificationName,Description)

    def CertificationDelete(self,CertificationId):
        objCertificationDAL=CertificationDAL()
        return objCertificationDAL.CertificationDelete(CertificationId)

    def CertificationGetByProfileId(self,ProfileId):
        objCertificationDAL=CertificationDAL()
        return objCertificationDAL.CertificationGetByProfileId(ProfileId) 

    def CertificationGetByCertificationId(self,certificationId):
        objCertificationDAL=CertificationDAL()
        return objCertificationDAL.CertificationGetByCertificationId(certificationId) 