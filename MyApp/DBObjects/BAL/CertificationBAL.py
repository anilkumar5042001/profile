from ..DAL.CertificationDAL import CertificationDAL

class CertificationBAL:
    def CertificationInsert(self,ProfileId,CertificationName,Description):
        objCertificationDAL=CertificationDAL()
        return objCertificationDAL.CertificationInsert(ProfileId,CertificationName,Description)