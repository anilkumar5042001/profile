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

    def CertificationGetByCertificationId(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Certification_GetByCertificationId"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Certification_GetByCertificationId(IN p_CertificationId INT)
        BEGIN
        SELECT 
        CertificationId,
        ProfileId,
        CertificationName,
        Description
        FROM Certification 
        WHERE CertificationId = p_CertificationId;
        END"""
        cursor.execute(query)
        print('SP CertificationGetByCertificationId executed')    
    
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

    def CertificationDelete(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Certification_Delete"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Certification_Delete
        (
        IN p_CertificationId INT
        )
        BEGIN
        DELETE FROM Certification 
        WHERE CertificationId=p_CertificationId;
        END"""
        cursor.execute(query)
        print('Exec SP CertificationDelete')
  
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
        IN p_StartMonth INT,
        IN p_StartYear INT,
        IN p_EndMonth INT,
        IN p_EndYear INT,
        IN p_CurrentlyWorking BOOLEAN
        )
        BEGIN
        INSERT INTO WorkHistory (
        ProfileId,
        CompanyName,
        Role,
        Description,
        City,
        Country,
        StartMonth,
        StartYear,
        EndMonth,
        EndYear,
        CurrentlyWorking) 
        VALUES (
        p_ProfileId,
        p_CompanyName,
        p_Role,
        p_Description,
        p_City,
        p_Country,
        p_StartMonth,
        p_StartYear,
        p_EndMonth,
        p_EndYear,
        p_CurrentlyWorking);
        END"""
        cursor.execute(query)
        print('Exec SP WorkHistoryInsert')

    def WorkHistoryGetById(self):
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
    
    def WorkHistoryUpdate(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS WorkHistory_Update"""
        cursor.execute(query)
        query = """CREATE PROCEDURE WorkHistory_Update
        (
        IN p_ProfileId INT,
        IN p_WorkHistoryId INT,
        IN p_CompanyName NVARCHAR(250),
        IN p_Role NVARCHAR(250),
        IN p_Description NVARCHAR(500),
        IN p_City VARCHAR(250),
        IN p_Country VARCHAR(250),
        IN p_StartMonth INT,
        IN p_StartYear INT,
        IN p_EndMonth INT,
        IN p_EndYear INT,
        IN p_CurrentlyWorking BOOLEAN
        )
        BEGIN
        Update WorkHistory 
        SET ProfileId=p_ProfileId,
        CompanyName=p_CompanyName,
        Role=p_Role,
        Description=p_Description,
        City=p_City,
        Country=p_Country,
        StartMonth=p_StartMonth,
        StartYear=p_StartYear,
        EndMonth=p_EndMonth,
        EndYear=p_EndYear,
        CurrentlyWorking=p_CurrentlyWorking
        WHERE WorkHistoryId=p_WorkHistoryId;
        END"""
        cursor.execute(query)
        print('Exec SP WorkHistoryUpdate')

    def ProjectHighlightsInsert(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS ProjectHighlights_Insert"""
        cursor.execute(query)
        query = """CREATE PROCEDURE ProjectHighlights_Insert
        (
        IN p_ProjectHighlightsId INT,
        IN p_WorkHistoryId INT,
        IN p_ProjectHighlightsDescription NVARCHAR(500)
        )
        BEGIN
        INSERT INTO ProjectHighlights (
        ProjectHighlightsId,
        WorkHistoryId,
        ProjectHighlightsDescription
        ) 
        VALUES (
        p_ProjectHighlightsId,
        p_WorkHistoryId,
        p_ProjectHighlightsDescription
        );
        END"""
        cursor.execute(query)
        print('Exec SP ProjectHighlightsInsert')

    def ProjectHighlightsGetById(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS ProjectHighlights_GetById"""
        cursor.execute(query)
        query = """CREATE PROCEDURE ProjectHighlights_GetById(IN p_WorkHistoryId INT)
        BEGIN
        SELECT ProjectHighlightsId,
        WorkHistoryId,
        ProjectHighlightsDescription
        FROM ProjectHighlights 
        WHERE WorkHistoryId = p_WorkHistoryId;
        END"""
        cursor.execute(query)
        print('SP ProjectHighlightsGetById executed')

    def ProjectHighlightsUpdate(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS ProjectHighlights_Update"""
        cursor.execute(query)
        query = """CREATE PROCEDURE ProjectHighlights_Update
        (
        IN p_ProjectHighlightsId INT,
        IN p_WorkHistoryId INT,
        IN p_ProjectHighlightsDescription NVARCHAR(500)
        )
        BEGIN
        Update ProjectHighlights 
        SET WorkHistoryId=p_WorkHistoryId,
        ProjectHighlightsDescription=p_ProjectHighlightsDescription
        WHERE ProjectHighlightsId=p_ProjectHighlightsId;
        END"""
        cursor.execute(query)
        print('Exec SP ProjectHighlightsUpdate')

    def ResponsibilitiesInsert(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Responsibilities_Insert"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Responsibilities_Insert
        (
        IN p_ResponsibilitiesId INT,
        IN p_WorkHistoryId INT,
        IN p_ResponsibilitiesDescription NVARCHAR(500)
        )
        BEGIN
        INSERT INTO Responsibilities (
        ResponsibilitiesId,
        WorkHistoryId,
        ResponsibilitiesDescription
        ) 
        VALUES (
        p_ResponsibilitiesId,
        p_WorkHistoryId,
        p_ResponsibilitiesDescription
        );
        END"""
        cursor.execute(query)
        print('Exec SP ResponsibilitiesInsert')

    def ResponsibilitiesGetById(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Responsibilities_GetById"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Responsibilities_GetById(IN p_WorkHistoryId INT)
        BEGIN
        SELECT ResponsibilitiesId,
        WorkHistoryId,
        ResponsibilitiesDescription
        FROM Responsibilities 
        WHERE WorkHistoryId = p_WorkHistoryId;
        END"""
        cursor.execute(query)
        print('SP ResponsibilitiesGetById executed')

    def ResponsibilitiesUpdate(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Responsibilities_Update"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Responsibilities_Update
        (
        IN p_ResponsibilitiesId INT,
        IN p_WorkHistoryId INT,
        IN p_ResponsibilitiesDescription NVARCHAR(500)
        )
        BEGIN
        Update Responsibilities 
        SET WorkHistoryId=p_WorkHistoryId,
        ResponsibilitiesDescription=p_ResponsibilitiesDescription
        WHERE ResponsibilitiesId=p_ResponsibilitiesId;
        END"""
        cursor.execute(query)
        print('Exec SP ResponsibilitiesUpdate')

    def EducationInsert(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Education_Insert"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Education_Insert
        (
        IN p_ProfileId INT,
        IN p_NameOfInstitution NVARCHAR(500),
        IN p_Degree NVARCHAR(250),
        IN p_StartYear INT,
        IN p_EndYear INT,
        IN p_EducationDescription NVARCHAR(500)
        )
        BEGIN
        INSERT INTO Education (
        ProfileId,
        NameOfInstitution,
        Degree,
        StartYear,
        EndYear,
        EducationDescription
        ) 
        VALUES (
        p_ProfileId,
        p_NameOfInstitution,
        p_Degree,
        p_StartYear,
        p_EndYear,
        p_EducationDescription
        );
        END"""
        cursor.execute(query)
        print('Exec SP EducationInsert')

    def EducationGetById(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Education_GetById"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Education_GetById(IN p_ProfileId INT)
        BEGIN
        SELECT EducationId,
        ProfileId,
        NameOfInstitution,
        Degree,
        StartYear,
        EndYear,
        EducationDescription
        FROM Education 
        WHERE ProfileId = p_ProfileId;
        END"""
        cursor.execute(query)
        print('SP EducationGetById executed')

    def EducationUpdate(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Education_Update"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Education_Update
        (
        IN p_EducationId INT,
        IN p_ProfileId INT,
        IN p_NameOfInstitution NVARCHAR(500),
        IN p_Degree NVARCHAR(250),
        IN p_StartYear INT,
        IN p_EndYear INT,
        IN p_EducationDescription NVARCHAR(500)
        )
        BEGIN
        Update Education 
        SET ProfileId=p_ProfileId,
        NameOfInstitution=p_NameOfInstitution,
        Degree=p_Degree,
        StartYear=p_StartYear,
        EndYear=p_EndYear,
        EducationDescription=p_EducationDescription
        WHERE EducationId=p_EducationId;
        END"""
        cursor.execute(query)
        print('Exec SP EducationUpdate')

    def EducationDelete(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Education_Delete"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Education_Delete(IN p_EducationId INT)
        BEGIN
        Delete
        FROM Education 
        WHERE EducationId = p_EducationId;
        END"""
        cursor.execute(query)
        print('SP EducationDelete executed')

    def LanguageInsert(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Language_Insert"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Language_Insert
        (
        IN p_ProfileId INT,
        IN p_LanguageName NVARCHAR(250),
        IN p_LanguageLevel NVARCHAR(250)
        )
        BEGIN
        INSERT INTO Language (
        ProfileId,
        LanguageName,
        LanguageLevel
        ) 
        VALUES (
        p_ProfileId,
        p_LanguageName,
        p_LanguageLevel
        );
        END"""
        cursor.execute(query)
        print('Exec SP LanguageInsert')

    def LanguageGetById(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Language_GetById"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Language_GetById(IN p_ProfileId INT)
        BEGIN
        SELECT LanguageId,
        ProfileId,
        LanguageName,
        LanguageLevel
        FROM Language 
        WHERE ProfileId = p_ProfileId;
        END"""
        cursor.execute(query)
        print('SP LanguageGetById executed')

    def LanguageUpdate(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Language_Update"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Language_Update
        (
        IN p_LanguageId INT,
        IN p_ProfileId INT,
        IN p_LanguageName NVARCHAR(250),
        IN p_LanguageLevel NVARCHAR(250)
        )
        BEGIN
        Update Language 
        SET ProfileId=p_ProfileId,
        LanguageName=p_LanguageName,
        LanguageLevel=p_LanguageLevel
        WHERE LanguageId=p_LanguageId;
        END"""
        cursor.execute(query)
        print('Exec SP LanguageUpdate')

    def LanguageDelete(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Language_Delete"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Language_Delete(IN p_LanguageId INT)
        BEGIN
        Delete
        FROM Language 
        WHERE LanguageId = p_LanguageId;
        END"""
        cursor.execute(query)
        print('SP LanguageDelete executed')

    def RegistrationInsert(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Registration_Insert"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Registration_Insert
        (
        IN p_RegistrationId INT,
        IN p_EmailId NVARCHAR(500),
        IN p_Password NVARCHAR(250)
        )
        BEGIN
        INSERT INTO Registration (
        RegistrationId,
        EmailId,
        Password
        ) 
        VALUES (
        p_RegistrationId,
        p_EmailId,
        p_Password
        );
        END"""
        cursor.execute(query)
        print('Exec SP RegistrationInsert')

    def RegistrationGetById(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Registration_GetById"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Registration_GetById(IN p_RegistrationId INT)
        BEGIN
        SELECT RegistrationId,
        EmailId,
        Password
        FROM Registration 
        WHERE RegistrationId = p_RegistrationId;
        END"""
        cursor.execute(query)
        print('SP RegistrationGetById executed')

    def RegistrationUpdate(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Registration_Update"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Registration_Update
        (
        IN p_RegistrationId INT,
        IN p_EmailId NVARCHAR(500),
        IN p_Password NVARCHAR(250)
        )
        BEGIN
        Update Registration 
        SET 
        EmailId=p_EmailId,
        Password=p_Password
        WHERE RegistrationId=p_RegistrationId;
        END"""
        cursor.execute(query)
        print('Exec SP RegistrationUpdate')

    def AwardsInsert(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Awards_Insert"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Awards_Insert
        (
        IN p_ProfileId INT,
        IN p_AwardTitle NVARCHAR(250),
        IN p_AwardDescription NVARCHAR(500)
        )
        BEGIN
        INSERT INTO Awards (
        ProfileId,
        AwardTitle,
        AwardDescription
        ) 
        VALUES (
        p_ProfileId,
        p_AwardTitle,
        p_AwardDescription
        );
        END"""
        cursor.execute(query)
        print('Exec SP AwardsInsert')

    def AwardsGetById(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Awards_GetById"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Awards_GetById(IN p_ProfileId INT)
        BEGIN
        SELECT AwardId,
        ProfileId,
        AwardTitle,
        AwardDescription
        FROM Awards
        WHERE ProfileId = p_ProfileId;
        END"""
        cursor.execute(query)
        print('SP AwardsGetById executed')

    def AwardsUpdate(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Awards_Update"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Awards_Update
        (
        IN p_AwardId INT,
        IN p_ProfileId INT,
        IN p_AwardTitle NVARCHAR(250),
        IN p_AwardDescription NVARCHAR(500)
        )
        BEGIN
        Update Awards 
        SET ProfileId=p_ProfileId,
        AwardTitle=p_AwardTitle,
        AwardDescription=p_AwardDescription
        WHERE AwardId=p_AwardId;
        END"""
        cursor.execute(query)
        print('Exec SP AwardsUpdate')

    def AwardsDelete(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Awards_Delete"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Awards_Delete(IN p_AwardId INT)
        BEGIN
        Delete
        FROM Awards 
        WHERE AwardId = p_AwardId;
        END"""
        cursor.execute(query)
        print('SP AwardsDelete executed')






    