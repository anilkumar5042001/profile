from ..DAL.EducationDAL import EducationDAL

class EducationBAL:
    def EducationInsert(self,EducationId,ProfileId,NameOfInstitution,CourseName,StartYear,EndYear):
        objEducationDAL=EducationDAL()
        return objEducationDAL.EducationInsert(EducationId,ProfileId,NameOfInstitution,CourseName,StartYear,EndYear)
