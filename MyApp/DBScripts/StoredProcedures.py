from django.db import connection

class StoredProcedures:
    def CountryGetAll(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Country_GetAll"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Country_GetAll()
        BEGIN
        SELECT country_id,country_name,country_code  FROM country;
        END """
        cursor.execute(query)
        print('method executed')

    def CountryGetById(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Country_GetById"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Country_GetById(IN countryId INT)
        BEGIN
        SELECT country_id,country_name,country_code  FROM country 
        WHERE country_id = countryId;
        END"""
        cursor.execute(query)
        print('method executed')

    def CountryInsert(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Country_Insert"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Country_Insert(IN countryId INT)
        BEGIN
        SELECT country_id,country_name,country_code  FROM country 
        WHERE country_id = countryId;
        END"""
        cursor.execute(query)
        print('method executed')
    
