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
        query = """CREATE PROCEDURE Country_Insert(IN p_country_code VARCHAR(250),IN p_country_name VARCHAR(250))
        BEGIN
        INSERT INTO country (country_name,country_code) 
        VALUES (p_country_name,p_country_code);
        END"""
        cursor.execute(query)
        print('Exec SP CountryInsert')
    
    def UserProfileGetById(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS UserProfile_GetById"""
        cursor.execute(query)
        query = """CREATE PROCEDURE UserProfile_GetById(IN p_ProfileId INT)
        BEGIN
        SELECT ProfileId,FirstName,LastName,EmailId,
        PhoneNumber,
        Education,
        Designation,
        AboutMe
        FROM UserProfile 
        WHERE ProfileId = p_ProfileId;
        END"""
        cursor.execute(query)
        print('SP UserProfileGetById executed')

    def CertificationGetByProfileId(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Certification_GetByProfileId"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Certification_GetByProfileId(IN p_ProfileId INT)
        BEGIN
        SELECT 
        CertificationId,
        ProfileId,
        CertificationName,
        Description
        FROM Certification 
        WHERE ProfileId = p_ProfileId;
        END"""
        cursor.execute(query)
        print('SP CertificationGetByProfileId executed')
    
    def UserProfileInsert(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS UserProfile_Insert"""
        cursor.execute(query)
        query = """CREATE PROCEDURE UserProfile_Insert
        (
        IN p_FirstName VARCHAR(250),
        IN p_LastName VARCHAR(250),
        IN p_EmailId NVARCHAR(500),
        IN p_PhoneNumber NVARCHAR(250),
        IN p_Education NVARCHAR(250),
        IN p_Designation NVARCHAR(250),
        IN p_AboutMe NVARCHAR(500)
        )
        BEGIN
        INSERT INTO UserProfile (
        FirstName,
        LastName,
        EmailId,
        PhoneNumber,
        Education,
        Designation,
        AboutMe) 
        VALUES (
        p_FirstName,
        p_LastName,
        p_EmailId,
        p_PhoneNumber,
        p_Education,
        p_Designation,
        p_AboutMe);
        END"""
        cursor.execute(query)
        print('Exec SP UserProfileInsert')

    def CertificationInsert(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Certification_Insert"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Certification_Insert
        (
        IN p_ProfileId INT,
        IN p_CertificationName VARCHAR(250),
        IN p_Description VARCHAR(500)
        )
        BEGIN
        INSERT INTO Certification (
        ProfileId,    
        CertificationName,
        Description
        ) 
        VALUES (
        p_ProfileId,
        p_CertificationName,
        p_Description
        );
        END"""
        cursor.execute(query)
        print('Exec SP CertificationInsert')

    def CertificationUpdate(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Certification_Update"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Certification_Update
        (
        IN p_CertificationId VARCHAR(250),
        IN p_CertificationName VARCHAR(250),
        IN p_Description VARCHAR(500)
        )
        BEGIN
        Update Certification 
        SET CertificationName=p_CertificationName,
        Description=p_Description
        WHERE CertificationId=p_CertificationId;
        END"""
        cursor.execute(query)
        print('Exec SP CertificationUpdate')
  
    def UserProfileUpdate(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS UserProfile_Update"""
        cursor.execute(query)
        query = """CREATE PROCEDURE UserProfile_Update
        (IN p_ProfileId INT,
        IN p_FirstName VARCHAR(250),
        IN p_LastName VARCHAR(250),
        IN p_EmailId NVARCHAR(500),
        IN p_PhoneNumber NVARCHAR(250),
        IN p_Education NVARCHAR(250),
        IN p_Designation NVARCHAR(250)
        )
        BEGIN
        UPDATE UserProfile SET 
        FirstName=p_FirstName,
        LastName=p_LastName,
        EmailId=p_EmailId,
        PhoneNumber=p_PhoneNumber,
        Education=p_Education,
        Designation=p_Designation
        WHERE ProfileId=p_ProfileId;
        END"""
        cursor.execute(query)
        print('Exec SP UserProfileUpdate')

    def UserProfileUpdateAboutMe(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS UserProfile_UpdateAboutMe"""
        cursor.execute(query)
        query = """CREATE PROCEDURE UserProfile_UpdateAboutMe
        (IN p_ProfileId INT,
        IN p_AboutMe VARCHAR(500)
        )
        BEGIN
        UPDATE UserProfile SET 
        AboutMe=p_AboutMe
        WHERE ProfileId=p_ProfileId;
        END"""
        cursor.execute(query)
        print('Exec SP UserProfileUpdateAboutMe')
    
    def ProjectInsert(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Project_Insert"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Project_Insert
        (IN p_ProfileId INT,IN p_ProjectId INT,IN p_ProjectName NVARCHAR(250),
        IN p_ProjectDescription NVARCHAR(500),IN p_Role NVARCHAR(250),IN p_StartYear DATETIME(),IN p_EndYear DATETIME(),IN p_Responsibilities NVARCHAR(250),IN p_Awards NVARCHAR(250))
        BEGIN
        INSERT INTO Projects (ProfileId,ProjectName,ProjectDescription,Role,StartYear,EndYear,Responsibilities,Awards) 
        VALUES (p_ProfileId,p_ProjectName,p_ProjectDescription,p_Role,p_StartYear,p_EndYear,p_Responsibilities,p_Awards)
        );
        END"""
        cursor.execute(query)
        print('Exec SP ProjectInsert')

    def WorkHistoryInsert(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS WorkHistory_Insert"""
        cursor.execute(query)
        query = """CREATE PROCEDURE WorkHistory_Insert
        (
        IN p_ProfileId INT,
        IN p_CompanyName NVARCHAR(250),
        IN p_Role NVARCHAR(250),
        IN p_Description NVARCHAR(500),
        IN p_City VARCHAR(250),
        IN p_Country VARCHAR(250),
        IN p_StartDate DATETIME,
        IN p_EndDate DATETIME
        )
        BEGIN
        INSERT INTO WorkHistory (
        ProfileId,
        CompanyName,
        Role,
        Description,
        City,
        Country,
        StartDate,
        EndDate) 
        VALUES (
        p_ProfileId,
        p_CompanyName,
        p_Role,
        p_Description,
        p_City,
        p_Country,
        p_StartDate,
        p_EndDate);
        END"""
        cursor.execute(query)
        print('Exec SP WorkHistoryInsert')

    def GetAllWorkHistory(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS WorkHistory_GetById"""
        cursor.execute(query)
        query = """CREATE PROCEDURE WorkHistory_GetById(IN p_ProfileId INT)
        BEGIN
        SELECT ProfileId,
        WorkHistoryId,
        CompanyName,
        Role,
        Description,
        City,
        Country,
        StartDate,
        EndDate
        FROM WorkHistory 
        WHERE ProfileId = p_ProfileId;
        END"""
        cursor.execute(query)
        print('SP WorkHistoryGetById executed')

    