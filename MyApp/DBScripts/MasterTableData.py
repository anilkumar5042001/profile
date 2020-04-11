from django.db import connection

class MasterTableData:
    def CountryMasterData(self):
        cursor = connection.cursor()
        query = """
        Truncate table CountryMaster;
        INSERT INTO CountryMaster(CountryId,CountryName,CountryCode,Flag) 
        VALUES(1,'India','IN','in.png');
        INSERT INTO CountryMaster(CountryId,CountryName,CountryCode,Flag) 
        VALUES(2,'United Kingdom','GB','gb.png');
        INSERT INTO CountryMaster(CountryId,CountryName,CountryCode,Flag) 
        VALUES(3,'United States','US','us.png');
        END"""
        cursor.execute(query)
        print('Exec MasterTableData CountryMasterData')
