from ..DAL.CertificationDAL import CertificationDAL

class CertificationBAL:
    def CertificationInsert(self,ProfileId,CertificationName,Description):
        objCertificationDAL=CertificationDAL()
        return objCertificationDAL.CertificationInsert(ProfileId,CertificationName,Description)

    def CertificationGetByProfileId(self,ProfileId):
        print('danger')
        objCertificationDAL=CertificationDAL()
        return objCertificationDAL.CertificationGetByProfileId(ProfileId) 