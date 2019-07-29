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
        objStoredProcedures.CertificationGetByProfileId('self')
        objStoredProcedures.WorkHistoryInsert('self')
        objStoredProcedures.WorkHistoryGetById('self')
        
        




#objExecOrder=ExecOrder
#objExecOrder.scriptsOrder('self')
