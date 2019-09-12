from ..DAL.EducationDAL import EducationDAL

class EducationBAL:
    def EducationInsert(self,ProfileId,NameOfInstitution,Degree,StartYear,EndYear,EducationDescription):
        objEducationDAL=EducationDAL()
        return objEducationDAL.EducationInsert(ProfileId,NameOfInstitution,Degree,StartYear,EndYear,EducationDescription)

    def GetEducationById(self,ProfileId):
        objEducationDAL=EducationDAL()
        return objEducationDAL.GetEducationById(ProfileId)

    def EducationUpdate(self,EducationId,ProfileId,NameOfInstitution,Degree,StartYear,EndYear,EducationDescription):
        objEducationDAL=EducationDAL()
        return objEducationDAL.EducationUpdate(EducationId,ProfileId,NameOfInstitution,Degree,StartYear,EndYear,EducationDescription)

    def EducationDelete(self,EducationId):
        objEducationDAL=EducationDAL()
        return objEducationDAL.EducationDelete(EducationId)

        
