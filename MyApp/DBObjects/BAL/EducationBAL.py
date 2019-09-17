from ..DAL.EducationDAL import EducationDAL

class EducationBAL:
    def EducationInsert(self,ProfileId,NameOfInstitution,Degree,StartYear,EndYear,EducationDescription):
        objEducationDAL=EducationDAL()
        return objEducationDAL.EducationInsert(ProfileId,NameOfInstitution,Degree,StartYear,EndYear,EducationDescription)

    def GetEducationByProfileId(self,ProfileId):
        objEducationDAL=EducationDAL()
        return objEducationDAL.GetEducationByProfileId(ProfileId)

    def GetEducationById(self,EducationId):
        objEducationDAL=EducationDAL()
        return objEducationDAL.GetEducationById(EducationId)

    def EducationUpdate(self,EducationId,ProfileId,NameOfInstitution,Degree,StartYear,EndYear,EducationDescription):
        objEducationDAL=EducationDAL()
        return objEducationDAL.EducationUpdate(EducationId,ProfileId,NameOfInstitution,Degree,StartYear,EndYear,EducationDescription)

    def EducationDelete(self,EducationId):
        objEducationDAL=EducationDAL()
        return objEducationDAL.EducationDelete(EducationId)

        
