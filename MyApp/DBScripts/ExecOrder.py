from .MySqlTable import MySqlTable
from .StoredProcedures import StoredProcedures
class ExecOrder:
    def scriptsOrder(self):
        #Tables
        objMySqlTable=MySqlTable
        objMySqlTable.CreateTest('self')
        objMySqlTable.CreateUserProfile('self')
        objMySqlTable.CreateCountry('self')
        objMySqlTable.CreateCertificationTable('self')
        objMySqlTable.CreateWorkHistory('self')
        objMySqlTable.CreateProjectHighlights('self')
        objMySqlTable.CreateResponsibilities('self')
        objMySqlTable.CreateEducation('self')
        objMySqlTable.CreateLanguage('self') 
        objMySqlTable.CreateRegistration('self') 
        objMySqlTable.CreateAwards('self')  

        #Stored Procedures
        objStoredProcedures=StoredProcedures
        objStoredProcedures.CountryGetAll('self')        
        objStoredProcedures.CountryGetById('self')        
        objStoredProcedures.CountryInsert('self')  
        objStoredProcedures.UserProfileGetById('self')
        objStoredProcedures.UserProfileInsert('self') 
        objStoredProcedures.UserProfileUpdate('self')    
        objStoredProcedures.UserProfileUpdateAboutMe('self')
        objStoredProcedures.CertificationInsert('self')
        objStoredProcedures.CertificationUpdate('self')
        objStoredProcedures.CertificationDelete('self')
        objStoredProcedures.CertificationGetByProfileId('self')
        objStoredProcedures.CertificationGetByCertificationId('self')
        objStoredProcedures.WorkHistoryInsert('self')
        objStoredProcedures.WorkHistoryGetById('self')
        objStoredProcedures.WorkHistoryUpdate('self')
        objStoredProcedures.ProjectHighlightsInsert('self')
        objStoredProcedures.ProjectHighlightsGetById('self')
        objStoredProcedures.ProjectHighlightsUpdate('self')
        objStoredProcedures.ResponsibilitiesInsert('self')
        objStoredProcedures.ResponsibilitiesGetById('self')
        objStoredProcedures.ResponsibilitiesUpdate('self')
        objStoredProcedures.EducationInsert('self')
        objStoredProcedures.EducationGetById('self')
        objStoredProcedures.EducationUpdate('self')
        objStoredProcedures.EducationDelete('self')
        objStoredProcedures.LanguageInsert('self')
        objStoredProcedures.LanguageGetById('self')
        objStoredProcedures.LanguageUpdate('self')
        objStoredProcedures.LanguageDelete('self')
        objStoredProcedures.RegistrationInsert('self')
        objStoredProcedures.RegistrationGetById('self')
        objStoredProcedures.RegistrationUpdate('self')
        objStoredProcedures.AwardsInsert('self')
        objStoredProcedures.GetAwardsById('self')
        objStoredProcedures.GetAwardsByProfileId('self')
        objStoredProcedures.AwardsUpdate('self')
        objStoredProcedures.AwardsDelete('self')
        
        




#objExecOrder=ExecOrder
#objExecOrder.scriptsOrder('self')
