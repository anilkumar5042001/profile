from ..DAL.CertificationDAL import CertificationDAL

class CertificationBAL:
    def CertificationInsert(self,ProfileId,CertificationName,Description):
        objCertificationDAL=CertificationDAL()
        return objCertificationDAL.CertificationInsert(ProfileId,CertificationName,Description)

    def CertificationGetByProfileId(self,ProfileId):
        objCertificationDAL=CertificationDAL()
        return objCertificationDAL.CertificationGetByProfileId(ProfileId) 

    def CertificationGetByCertificationId(self,certificationId):
        objCertificationDAL=CertificationDAL()
        return objCertificationDAL.CertificationGetByCertificationId(certificationId) 