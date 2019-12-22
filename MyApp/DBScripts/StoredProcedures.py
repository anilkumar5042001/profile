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
        City,
        Country,
        AboutMe,
        CompanyDomain
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
        IN p_City VARCHAR(250),
        IN p_Country VARCHAR(250),
        IN p_AboutMe NVARCHAR(500),
        IN p_Password NVARCHAR(250),
        IN p_CompanyDomain NVARCHAR(250)
        )
        BEGIN
        INSERT INTO UserProfile (
        FirstName,
        LastName,
        EmailId,
        PhoneNumber,
        Education,
        Designation,
        City,
        Country,
        AboutMe,
        Password,
        CompanyDomain) 
        VALUES (
        p_FirstName,
        p_LastName,
        p_EmailId,
        p_PhoneNumber,
        p_Education,
        p_Designation,
        p_City,
        p_Country,
        p_AboutMe,
        p_Password,
        p_CompanyDomain);
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
        IN p_Designation NVARCHAR(250),
        IN p_City VARCHAR(250),
        IN p_Country VARCHAR(250),
        IN p_AboutMe NVARCHAR(500),
        IN p_CompanyDomain NVARCHAR(250)
        )
        BEGIN
        UPDATE UserProfile SET 
        FirstName=p_FirstName,
        LastName=p_LastName,
        EmailId=p_EmailId,
        PhoneNumber=p_PhoneNumber,
        Education=p_Education,
        Designation=p_Designation,
        City=p_City,
        Country=p_Country,
        AboutMe = p_AboutMe,
        CompanyDomain=p_CompanyDomain
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
        IN p_ProjectName NVARCHAR(250),
        IN p_Role NVARCHAR(250),
        IN p_Description NVARCHAR(500),
        IN p_City VARCHAR(250),
        IN p_Country VARCHAR(250),
        IN p_StartMonth INT,
        IN p_StartYear INT,
        IN p_EndMonth INT,
        IN p_EndYear INT,
        IN p_CurrentlyWorking BOOLEAN,
        IN p_CompanyEmailId NVARCHAR(250)
        )
        BEGIN
        INSERT INTO WorkHistory (
        ProfileId,
        CompanyName,
        ProjectName,
        Role,
        Description,
        City,
        Country,
        StartMonth,
        StartYear,
        EndMonth,
        EndYear,
        CurrentlyWorking,
        CompanyEmailId) 
        VALUES (
        p_ProfileId,
        p_CompanyName,
        p_ProjectName,
        p_Role,
        p_Description,
        p_City,
        p_Country,
        p_StartMonth,
        p_StartYear,
        p_EndMonth,
        p_EndYear,
        p_CurrentlyWorking,
        p_CompanyEmailId);
        select LAST_INSERT_ID();
        END"""
        cursor.execute(query)
        print('Exec SP WorkHistoryInsert')

    def GetWorkHistoryByProfileId(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS GetWorkHistory_ByProfileId"""
        cursor.execute(query)
        query = """CREATE PROCEDURE GetWorkHistory_ByProfileId(IN p_ProfileId INT)
        BEGIN
        SELECT ProfileId,
        WorkHistoryId,
        CompanyName,
        ProjectName,
        Role,
        Description,
        City,
        Country,
        StartMonth,
        StartYear,
        EndMonth,
        EndYear,
        CurrentlyWorking,
        CompanyEmailId
        FROM WorkHistory 
        WHERE ProfileId = p_ProfileId;
        END"""
        cursor.execute(query)
        print('SP GetWorkHistoryByProfileId executed')
    
    def GetWorkHistoryByProfileIdAndCompanyName(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS GetWorkHistory_ByProfileIdAndCompanyName"""
        cursor.execute(query)
        query = """CREATE PROCEDURE GetWorkHistory_ByProfileIdAndCompanyName(IN p_ProfileId INT,IN p_CompanyName VARCHAR(250))
        BEGIN
        SELECT ProfileId,
        WorkHistoryId,
        CompanyName,
        ProjectName,
        Role,
        Description,
        City,
        Country,
        StartMonth,
        StartYear,
        EndMonth,
        EndYear,
        CurrentlyWorking,
        CompanyEmailId
        FROM WorkHistory 
        WHERE ProfileId = p_ProfileId
        AND
        CompanyName=p_CompanyName;
        END"""
        cursor.execute(query)
        print('SP GetWorkHistoryByProfileIdAndCompanyName executed')

    def WorkHistoryGetById(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS WorkHistory_GetById"""
        cursor.execute(query)
        query = """CREATE PROCEDURE WorkHistory_GetById(IN p_WorkHistoryId INT)
        BEGIN
        SELECT ProfileId,
        WorkHistoryId,
        CompanyName,
        ProjectName,
        Role,
        Description,
        City,
        Country,
        StartMonth,
        StartYear,
        EndMonth,
        EndYear,
        CurrentlyWorking,
        CompanyEmailId
        FROM WorkHistory 
        WHERE WorkHistoryId = p_WorkHistoryId;
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
        IN p_ProjectName NVARCHAR(250),
        IN p_Role NVARCHAR(250),
        IN p_Description NVARCHAR(500),
        IN p_City VARCHAR(250),
        IN p_Country VARCHAR(250),
        IN p_StartMonth INT,
        IN p_StartYear INT,
        IN p_EndMonth INT,
        IN p_EndYear INT,
        IN p_CurrentlyWorking BOOLEAN,
        IN p_CompanyEmailId NVARCHAR(250)
        )
        BEGIN
        Update WorkHistory 
        SET ProfileId=p_ProfileId,
        CompanyName=p_CompanyName,
        ProjectName=p_ProjectName,
        Role=p_Role,
        Description=p_Description,
        City=p_City,
        Country=p_Country,
        StartMonth=p_StartMonth,
        StartYear=p_StartYear,
        EndMonth=p_EndMonth,
        EndYear=p_EndYear,
        CurrentlyWorking=p_CurrentlyWorking,
        CompanyEmailId=p_CompanyEmailId
        WHERE WorkHistoryId=p_WorkHistoryId;
        END"""
        cursor.execute(query)
        print('Exec SP WorkHistoryUpdate')

    def WorkHistoryDelete(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS WorkHistory_Delete"""
        cursor.execute(query)
        query = """CREATE PROCEDURE WorkHistory_Delete(IN p_WorkHistoryId INT)
        BEGIN
        Delete
        FROM WorkHistory 
        WHERE WorkHistoryId = p_WorkHistoryId;
        END"""
        cursor.execute(query)
        print('SP WorkHistoryDelete executed')

    def ProjectHighlightsInsert(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS ProjectHighlights_Insert"""
        cursor.execute(query)
        query = """CREATE PROCEDURE ProjectHighlights_Insert
        (
        IN p_WorkHistoryId INT,
        IN p_ProjectHighlightsDescription NVARCHAR(500)
        )
        BEGIN
        INSERT INTO ProjectHighlights (
        WorkHistoryId,
        Description
        ) 
        VALUES (
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
        SELECT HighlightId,
        WorkHistoryId,
        Description
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
        IN p_HighlightId INT,
        IN p_WorkHistoryId INT,
        IN p_Description NVARCHAR(500)
        )
        BEGIN
        Update ProjectHighlights 
        SET WorkHistoryId=p_WorkHistoryId,
        Description=p_Description
        WHERE HighlightId=p_HighlightId;
        END"""
        cursor.execute(query)
        print('Exec SP ProjectHighlightsUpdate')

    def ProjectHighlightsDelete(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS ProjectHighlights_Delete"""
        cursor.execute(query)
        query = """CREATE PROCEDURE ProjectHighlights_Delete(IN p_HighlightId INT)
        BEGIN
        Delete
        FROM ProjectHighlights 
        WHERE HighlightId = p_HighlightId;
        END"""
        cursor.execute(query)
        print('SP ProjectHighlightsDelete executed')

    def ProjectHighlightsDeleteByWorkHistoryId(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS ProjectHighlightsDelete_ByWorkHistoryId"""
        cursor.execute(query)
        query = """CREATE PROCEDURE ProjectHighlightsDelete_ByWorkHistoryId(IN p_WorkHistoryId INT)
        BEGIN
        Delete
        FROM ProjectHighlights 
        WHERE WorkHistoryId = p_WorkHistoryId;
        END"""
        cursor.execute(query)
        print('SP ProjectHighlightsDeleteByWorkHistoryId executed')

    def ResponsibilitiesInsert(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Responsibilities_Insert"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Responsibilities_Insert
        (
        IN p_WorkHistoryId INT,
        IN p_Description NVARCHAR(500)
        )
        BEGIN
        INSERT INTO Responsibilities (
        WorkHistoryId,
        Description
        ) 
        VALUES (
        p_WorkHistoryId,
        p_Description
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
        Description
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
        IN p_Description NVARCHAR(500)
        )
        BEGIN
        Update Responsibilities 
        SET WorkHistoryId=p_WorkHistoryId,
        Description=p_Description
        WHERE ResponsibilitiesId=p_ResponsibilitiesId;
        END"""
        cursor.execute(query)
        print('Exec SP ResponsibilitiesUpdate')

    def ResponsibilitiesDelete(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Responsibilities_Delete"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Responsibilities_Delete(IN p_ResponsibilitiesId INT)
        BEGIN
        Delete
        FROM Responsibilities 
        WHERE ResponsibilitiesId = p_ResponsibilitiesId;
        END"""
        cursor.execute(query)
        print('SP ResponsibilitiesDelete executed')

    def ResponsibilitiesDeleteByWorkHistoryId(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS ResponsibilitiesDelete_ByWorkHistoryId"""
        cursor.execute(query)
        query = """CREATE PROCEDURE ResponsibilitiesDelete_ByWorkHistoryId(IN p_WorkHistoryId INT)
        BEGIN
        Delete
        FROM Responsibilities 
        WHERE WorkHistoryId = p_WorkHistoryId;
        END"""
        cursor.execute(query)
        print('SP ResponsibilitiesDeleteByWorkHistoryId executed')

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

    def GetEducationByProfileId(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS GetEducation_ByProfileId"""
        cursor.execute(query)
        query = """CREATE PROCEDURE GetEducation_ByProfileId(IN p_ProfileId INT)
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
        print('SP GetEducationByProfileId executed')

    def EducationGetById(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Education_GetById"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Education_GetById(IN p_EducationId INT)
        BEGIN
        SELECT EducationId,
        ProfileId,
        NameOfInstitution,
        Degree,
        StartYear,
        EndYear,
        EducationDescription
        FROM Education 
        WHERE EducationId = p_EducationId;
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

    def GetLanguageByProfileId(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS GetLanguage_ByProfileId"""
        cursor.execute(query)
        query = """CREATE PROCEDURE GetLanguage_ByProfileId(IN p_ProfileId INT)
        BEGIN
        SELECT LanguageId,
        ProfileId,
        LanguageName,
        LanguageLevel
        FROM Language 
        WHERE ProfileId = p_ProfileId;
        END"""
        cursor.execute(query)
        print('SP GetLanguageByProfileId executed')

    def LanguageGetById(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Language_GetById"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Language_GetById(IN p_LanguageId INT)
        BEGIN
        SELECT LanguageId,
        ProfileId,
        LanguageName,
        LanguageLevel
        FROM Language 
        WHERE LanguageId = p_LanguageId;
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
        IN p_EmailId NVARCHAR(500),
        IN p_Password NVARCHAR(250)
        )
        BEGIN
        INSERT INTO Registration (
        EmailId,
        Password
        ) 
        VALUES (
        p_EmailId,
        p_Password
        );
        select LAST_INSERT_ID();
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

    def GetAwardsByProfileId(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS GetAwards_ByProfileId"""
        cursor.execute(query)
        query = """CREATE PROCEDURE GetAwards_ByProfileId(IN p_ProfileId INT)
        BEGIN
        SELECT AwardId,
        ProfileId,
        AwardTitle,
        AwardDescription
        FROM Awards
        WHERE ProfileId = p_ProfileId;
        END"""
        cursor.execute(query)
        print('SP GetAwardsByProfileId executed')

    def GetAwardsById(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Awards_GetById"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Awards_GetById(IN p_AwardId INT)
        BEGIN
        SELECT AwardId,
        ProfileId,
        AwardTitle,
        AwardDescription
        FROM Awards
        WHERE AwardId = p_AwardId;
        END"""
        cursor.execute(query)
        print('SP GetAwardsById executed')

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

    def InterestInsert(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Interest_Insert"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Interest_Insert
        (
        IN p_ProfileId INT,
        IN p_InterestName NVARCHAR(250)
        )
        BEGIN
        INSERT INTO Interest (
        ProfileId,
        InterestName
        ) 
        VALUES (
        p_ProfileId,
        p_InterestName
        );
        END"""
        cursor.execute(query)
        print('Exec SP InterestInsert')

    def InterestGetById(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Interest_GetById"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Interest_GetById(IN p_InterestId INT)
        BEGIN
        SELECT InterestId,
        ProfileId,
        InterestName
        FROM Interest 
        WHERE InterestId = p_InterestId;
        END"""
        cursor.execute(query)
        print('SP InterestGetById executed')

    def GetInterestByProfileId(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS GetInterest_ByProfileId"""
        cursor.execute(query)
        query = """CREATE PROCEDURE GetInterest_ByProfileId(IN p_ProfileId INT)
        BEGIN
        SELECT InterestId,
        ProfileId,
        InterestName
        FROM Interest 
        WHERE ProfileId = p_ProfileId;
        END"""
        cursor.execute(query)
        print('SP GetInterestByProfileId executed')

    def InterestUpdate(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Interest_Update"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Interest_Update
        (
        IN p_InterestId INT,
        IN p_ProfileId INT,
        IN p_InterestName NVARCHAR(250)
        )
        BEGIN
        Update Interest 
        SET ProfileId=p_ProfileId,
        InterestName=p_InterestName
        WHERE InterestId=p_InterestId;
        END"""
        cursor.execute(query)
        print('Exec SP InterestUpdate')

    def InterestDelete(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Interest_Delete"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Interest_Delete(IN p_InterestId INT)
        BEGIN
        Delete
        FROM Interest 
        WHERE InterestId = p_InterestId;
        END"""
        cursor.execute(query)
        print('SP InterestDelete executed')

    def CheckLoginCredentials(self): 
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS CheckLoginCredentials"""
        cursor.execute(query)
        query = """CREATE PROCEDURE CheckLoginCredentials
        (
        IN p_EmailId NVARCHAR(500),
        IN p_Password NVARCHAR(250)
        )
        BEGIN
        Declare p_ProfileIdValue INT;
        Declare p_Result INT;
        set p_ProfileIdValue = (SELECT ProfileId from UserProfile where EmailId=p_EmailId and Password=p_Password);
        IF p_ProfileIdValue>0 THEN
        set  p_Result=p_ProfileIdValue;
        else
        set p_Result=0;
        END IF;
        select p_Result as output;
        END"""
        cursor.execute(query)
        print('SP CheckLoginCredentials executed')

    def TaskInsert(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Task_Insert"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Task_Insert
        (
        IN p_ProfileId INT,
        IN p_TaskTitle NVARCHAR(250),
        IN p_Description NVARCHAR(500),
        IN p_DueDate DATETIME,
        IN p_AssignTo INT,
        IN p_CreatedBy INT,
        IN p_TaskStatus VARCHAR(250)
        )
        BEGIN
        INSERT INTO Task (
        ProfileId,
        TaskTitle,
        Description,
        DueDate,
        AssignTo,
        CreatedBy,
        TaskStatus
        ) 
        VALUES (
        p_ProfileId,
        p_TaskTitle,
        p_Description,
        p_DueDate,
        p_AssignTo,
        p_CreatedBy,
        p_TaskStatus
        );
        select LAST_INSERT_ID();
        END"""
        cursor.execute(query)
        print('Exec SP TaskInsert')

    def GetTaskByTaskId(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS GetTask_ByTaskId"""
        cursor.execute(query)
        query = """CREATE PROCEDURE GetTask_ByTaskId(IN p_TaskId INT)
        BEGIN
        SELECT TaskId,
        ProfileId,
        TaskTitle,
        Description,
        DueDate,
        AssignTo,
        CreatedBy,
        TaskStatus
        FROM Task 
        WHERE TaskId = p_TaskId;
        END"""
        cursor.execute(query)
        print('SP GetTaskByTaskId executed')

    def GetTaskByProfileId(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS GetTask_ByProfileId"""
        cursor.execute(query)
        query = """CREATE PROCEDURE GetTask_ByProfileId(IN p_ProfileId INT)
        BEGIN
        SELECT TaskId,
        ProfileId,
        TaskTitle,
        Description,
        DueDate,
        AssignTo,
        CreatedBy,
        TaskStatus
        FROM Task 
        WHERE ProfileId = p_ProfileId;
        END"""
        cursor.execute(query)
        print('SP GetTaskByProfileId executed')
    

    def GetTaskByAssignTo(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS GetTask_ByAssignTo"""
        cursor.execute(query)
        query = """CREATE PROCEDURE GetTask_ByAssignTo(IN p_AssignTo INT)
        BEGIN
        SELECT TaskId,
        ProfileId,
        TaskTitle,
        Description,
        DueDate,
        AssignTo,
        CreatedBy,
        TaskStatus
        FROM Task 
        WHERE AssignTo = p_AssignTo;
        END"""
        cursor.execute(query)
        print('SP GetTaskByAssignTo executed')

    def TaskUpdate(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Task_Update"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Task_Update
        (
        IN p_TaskId INT,
        IN p_ProfileId INT,
        IN p_TaskTitle NVARCHAR(250),
        IN p_Description NVARCHAR(500),
        IN p_DueDate DATETIME,
        IN p_AssignTo INT,
        IN p_CreatedBy INT,
        IN p_TaskStatus VARCHAR(250)
        )
        BEGIN
        Update Task 
        SET 
        ProfileId=p_ProfileId,
        TaskTitle=p_TaskTitle,
        Description=p_Description,
        DueDate=p_DueDate,
        AssignTo=p_AssignTo,
        CreatedBy=p_CreatedBy,
        TaskStatus=p_TaskStatus
        WHERE TaskId=p_TaskId;
        END"""
        cursor.execute(query)
        print('Exec SP TaskUpdate')

    def GetUsers(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Get_Users"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Get_Users()
        BEGIN
        SELECT ProfileId,FirstName,LastName  FROM UserProfile;
        END """
        cursor.execute(query)
        print('Exec SP GetUsers')

    def UserProfileGetByCompanyDomain(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS UserProfile_GetByCompanyDomain"""
        cursor.execute(query)
        query = """CREATE PROCEDURE UserProfile_GetByCompanyDomain
        (
        IN p_CompanyDomain VARCHAR(250)
        )
        BEGIN
        SELECT ProfileId,FirstName,LastName,EmailId,
        PhoneNumber,
        Education,
        Designation,
        City,
        Country,
        AboutMe,
        CompanyDomain
        FROM UserProfile 
        WHERE CompanyDomain=p_CompanyDomain;
        END """
        cursor.execute(query)
        print('Exec SP UserProfileGetByCompanyDomain')

    def UserProfileUpdateDomainName(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS UserProfile_UpdateDomainName"""
        cursor.execute(query)
        query = """CREATE PROCEDURE UserProfile_UpdateDomainName
        (
        IN p_ProfileId INT,
        IN p_CompanyDomain VARCHAR(250)
        )
        BEGIN
        Update UserProfile 
        SET 
        CompanyDomain=p_CompanyDomain
        WHERE ProfileId=p_ProfileId;
        END"""
        cursor.execute(query)
        print('Exec SP UserProfile_UpdateDomainName')


    def SkillsCategoryInsert(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS SkillsCategory_Insert"""
        cursor.execute(query)
        query = """CREATE PROCEDURE SkillsCategory_Insert
        (
        IN p_ProfileId INT,
        IN p_SkillCategoryName NVARCHAR(250)
        )
        BEGIN
        INSERT INTO SkillsCategory (
        ProfileId,
        SkillCategoryName
        ) 
        VALUES (
        p_ProfileId,
        p_SkillCategoryName
        );
        select LAST_INSERT_ID();
        END"""
        cursor.execute(query)
        print('Exec SP SkillsCategoryInsert')

    def GetSkillCategoryByProfileId(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS GetSkillsCategory_ByProfileId"""
        cursor.execute(query)
        query = """CREATE PROCEDURE GetSkillsCategory_ByProfileId(IN p_ProfileId INT)
        BEGIN
        SELECT SkillCategoryId,
        ProfileId,
        SkillCategoryName
        FROM SkillsCategory
        WHERE ProfileId = p_ProfileId;
        END"""
        cursor.execute(query)
        print('SP GetSkillsCategoryByProfileId executed')

    def GetSkillCategoryById(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS SkillsCategory_GetById"""
        cursor.execute(query)
        query = """CREATE PROCEDURE SkillsCategory_GetById(IN p_SkillCategoryId INT)
        BEGIN
        SELECT SkillCategoryId,
        ProfileId,
        SkillCategoryName
        FROM SkillsCategory
        WHERE SkillCategoryId = p_SkillCategoryId;
        END"""
        cursor.execute(query)
        print('SP GetSkillCategoryById executed')

    def SkillCategoryUpdate(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS SkillsCategory_Update"""
        cursor.execute(query)
        query = """CREATE PROCEDURE SkillsCategory_Update
        (
        IN p_SkillCategoryId INT,
        IN p_ProfileId INT,
        IN p_SkillCategoryName NVARCHAR(250)
        )
        BEGIN
        Update SkillsCategory 
        SET
        ProfileId=p_ProfileId,
        SkillCategoryName=p_SkillCategoryName
        WHERE SkillCategoryId=p_SkillCategoryId;
        END"""
        cursor.execute(query)
        print('Exec SP SkillsCategoryUpdate')

    def SkillCategoryDelete(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS SkillsCategory_Delete"""
        cursor.execute(query)
        query = """CREATE PROCEDURE SkillsCategory_Delete(IN p_SkillCategoryId INT)
        BEGIN
        Delete
        FROM SkillsCategory 
        WHERE SkillCategoryId = p_SkillCategoryId;
        END"""
        cursor.execute(query)
        print('SP SkillsCategoryDelete executed')

    def SkillsInsert(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Skills_Insert"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Skills_Insert
        (
        IN p_ProfileId INT,
        IN p_SkillCategoryId INT,
        IN p_SkillName NVARCHAR(250)
        )
        BEGIN
        INSERT INTO Skills (
        ProfileId,
        SkillCategoryId,
        SkillName
        ) 
        VALUES (
        p_ProfileId,
        p_SkillCategoryId,
        p_SkillName
        );
        select LAST_INSERT_ID();
        END"""
        cursor.execute(query)
        print('Exec SP SkillsInsert')

    def GetSkillsByProfileId(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS GetSkills_ByProfileId"""
        cursor.execute(query)
        query = """CREATE PROCEDURE GetSkills_ByProfileId(IN p_ProfileId INT)
        BEGIN
        SELECT SkillId,
        ProfileId,
        SkillCategoryId,
        SkillName
        FROM Skills
        WHERE ProfileId = p_ProfileId;
        END"""
        cursor.execute(query)
        print('SP GetSkillsByProfileId executed')

    def GetSkillsById(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Skills_GetById"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Skills_GetById(IN p_SkillId INT)
        BEGIN
        SELECT SkillId,
        ProfileId,
        SkillCategoryId,
        SkillName
        FROM Skills
        WHERE SkillId = p_SkillId;
        END"""
        cursor.execute(query)
        print('SP GetSkillsById executed')

    def SkillsUpdate(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Skills_Update"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Skills_Update
        (
        IN p_SkillId INT,
        IN p_ProfileId INT,
        IN p_SkillCategoryId INT,
        IN p_SkillCategoryName NVARCHAR(250)
        )
        BEGIN
        Update Skills 
        SET
        ProfileId=p_ProfileId,
        SkillCategoryId=p_SkillCategoryId,
        SkillName=p_SkillName
        WHERE SkillId=p_SkillId;
        END"""
        cursor.execute(query)
        print('Exec SP SkillsUpdate')

    def SkillsDelete(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Skills_Delete"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Skills_Delete(IN p_SkillId INT)
        BEGIN
        Delete
        FROM Skills 
        WHERE SkillsId = p_SkillsId;
        END"""
        cursor.execute(query)
        print('SP SkillsDelete executed')

    def FavouriteInsert(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Favourite_Insert"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Favourite_Insert
        (            
        IN p_ProfileId INT,
        IN p_FavouriteCategoryId INT,
        IN p_FavouriteName NVARCHAR(250),
        IN p_FavouriteLink NVARCHAR(250)
        )
        BEGIN
        INSERT INTO Favourite (
        ProfileId,
        FavouriteCategoryId,
        FavouriteName,
        FavouriteLink       
        ) 
        VALUES (
        p_ProfileId,
        p_FavouriteCategoryId,
        p_FavouriteName,
        p_FavouriteLink       
        );
        select LAST_INSERT_ID();
        END"""
        cursor.execute(query)
        print('Exec SP FavouriteInsert')

    def GetFavouriteByProfileId(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS GetFavourite_ByProfileId"""
        cursor.execute(query)
        query = """CREATE PROCEDURE GetFavourite_ByProfileId(IN p_ProfileId INT)
        BEGIN
        SELECT 
        FavouriteId,        
        ProfileId,
        FavouriteCategoryId,
        FavouriteName,
        FavouriteLink       
        FROM Favourite
        WHERE ProfileId = p_ProfileId;
        END"""
        cursor.execute(query)
        print('SP GetFavouriteByProfileId executed')

    def GetFavouriteById(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS GetFavourite_ById"""
        cursor.execute(query)
        query = """CREATE PROCEDURE GetFavourite_ById(IN p_FavouriteId INT)
        BEGIN
        SELECT 
        FavouriteId,
        ProfileId,
        FavouriteCategoryId,
        FavouriteName,
        FavouriteLink       
        FROM Favourite
        WHERE FavouriteId = p_FavouriteId;
        END"""
        cursor.execute(query)
        print('SP GetFavouriteById executed')

    def FavouriteUpdate(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Favourite_Update"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Favourite_Update
        (
        IN p_FavouriteId INT,
        IN p_ProfileId INT,
        IN p_FavouriteCategoryId INT,
        IN p_FavouriteName NVARCHAR(250),
        IN p_FavouriteLink NVARCHAR(250)
        )
        BEGIN
        Update Favourite 
        SET
        FavouriteId=p_FavouriteId,
        ProfileId=p_ProfileId,
        FavouriteCategoryId=p_FavouriteCategoryId,
        FavouriteName=p_FavouriteName,
        FavouriteLink=p_FavouriteLink       
        WHERE FavouriteId=p_FavouriteId;
        END"""
        cursor.execute(query)
        print('Exec SP FavouriteUpdate')

    def FavouriteDelete(self):
        cursor = connection.cursor()
        query = """DROP PROCEDURE IF EXISTS Favourite_Delete"""
        cursor.execute(query)
        query = """CREATE PROCEDURE Favourite_Delete(IN p_FavouriteId INT)
        BEGIN
        Delete
        FROM Favourite 
        WHERE FavouriteId = p_FavouriteId;
        END"""
        cursor.execute(query)
        print('SP FavouriteDelete executed')











    