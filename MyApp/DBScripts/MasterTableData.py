from django.db import connection

class MasterTableData:
    def CountryMasterData(self):
        cursor = connection.cursor()
        query = """Truncate table CountryMaster"""
        cursor.execute(query)
        query = """
        INSERT INTO CountryMaster(CountryId,CountryName,CountryCode,Flag) 
        VALUES(1,'India','IN','in.jpg');
        INSERT INTO CountryMaster(CountryId,CountryName,CountryCode,Flag) 
        VALUES(2,'United Kingdom','UK','uk.jpg');
        
        END"""
        cursor.execute(query)
        print('Exec MasterTableData CountryMasterData')
