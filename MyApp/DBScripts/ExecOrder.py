from .MySqlTable import MySqlTable
from .StoredProcedures import StoredProcedures
class ExecOrder:
    def scriptsOrder(self):
        #Tables
        objMySqlTable=MySqlTable
        objMySqlTable.CreateTest('self')
        objMySqlTable.CreateUserProfile('self')

        #Stored Procedures
        objStoredProcedures=StoredProcedures
        objStoredProcedures.CountryGetAll('self')        
        objStoredProcedures.CountryGetById('self')        




objExecOrder=ExecOrder
objExecOrder.scriptsOrder('self')
