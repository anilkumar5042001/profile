from ..DAL.CountryDAL import CountryDAL

class CountryBAL:
    def GetCountryById(self,countryId):
        objCountryDAL=CountryDAL()
        return objCountryDAL.GetCountryById(countryId)

    def GetCountries(self):
        objCountryDAL=CountryDAL()
        return objCountryDAL.GetCountries() 
    
    