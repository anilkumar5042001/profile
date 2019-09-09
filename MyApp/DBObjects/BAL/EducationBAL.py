from ..DAL.EducationDAL import EducationDAL

class EducationBAL:
    def EducationInsert(self,EducationId,ProfileId,NameOfInstitution,CourseName,StartYear,EndYear):
        objEducationDAL=EducationDAL()
        return objEducationDAL.EducationInsert(EducationId,ProfileId,NameOfInstitution,CourseName,StartYear,EndYear)

    def GetEducationById(self,ProfileId):
        objEducationDAL=EducationDAL()
        return objEducationDAL.GetEducationById(ProfileId)

    def EducationUpdate(self,EducationId,ProfileId,NameOfInstitution,CourseName,StartYear,EndYear):
        objEducationDAL=EducationDAL()
        return objEducationDAL.EducationUpdate(EducationId,ProfileId,NameOfInstitution,CourseName,StartYear,EndYear)

    def EducationDelete(self,EducationId):
        objEducationDAL=EducationDAL()
        return objEducationDAL.EducationDelete(EducationId)

        
