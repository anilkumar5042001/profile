
from django.db import connection

class MySqlTable:
    def CreateTest(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"test")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table test(
            test_id INT NOT NULL AUTO_INCREMENT,
            test_title VARCHAR(100) NOT NULL,
            PRIMARY KEY ( test_id )
            );"""
            cursor.execute(query)
            print('method executed')

    def CreateCountry(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"country")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table country(
            country_id INT NOT NULL AUTO_INCREMENT,
            country_code VARCHAR(100) NOT NULL,
            country_name VARCHAR(100) NOT NULL,
            PRIMARY KEY (country_id)
            );"""
            cursor.execute(query)
            print('method executed table CreateCountry')

    def CreateUserProfile(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"UserProfile")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table UserProfile(
            ProfileId INT NOT NULL AUTO_INCREMENT,
            FirstName VARCHAR(250) NULL,
            LastName VARCHAR(250) NULL,
            EmailId NVARCHAR(500) NULL,
            PhoneNumber NVARCHAR(250) NULL,
            Education NVARCHAR(250) NULL,
            Designation NVARCHAR(250) NULL,
            AboutMe NVARCHAR(500) NULL,
            PRIMARY KEY ( ProfileId )
            );"""
            cursor.execute(query)
            print('method executed')

    def CreateCertificationTable(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"Certification")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table Certification(
            CertificationId INT NOT NULL AUTO_INCREMENT,
            ProfileId INT NOT NULL,
            CertificationName VARCHAR(250) NULL,
            Description VARCHAR(500) NULL,
            PRIMARY KEY (CertificationId)
            );"""
            cursor.execute(query)
            print('Certification table created')
    
    def CreateProjects(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"Projects")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table Projects(
            ProfileId INT NOT NULL,
            ProjectId INT NOT NULL AUTO_INCREMENT,
            ProjectName NVARCHAR(250) NULL,
            ProjectDescription NVARCHAR(500) NULL,
            Role NVARCHAR(250) NULL,
            StartYear DATETIME NULL,
            EndYear DATETIME NULL,
            Responsibilities NVARCHAR(250) NULL,
            Awards NVARCHAR(250) NULL,
            PRIMARY KEY ( ProjectId )
            );"""
            cursor.execute(query)
            print('method executed')

    def CreateWorkHistory(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"WorkHistory")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table WorkHistory
            (
            WorkHistoryId INT NOT NULL AUTO_INCREMENT,
            ProfileId INT NOT NULL,
            CompanyName NVARCHAR(250) NULL,
            Role NVARCHAR(250) NULL,
            Description NVARCHAR(500),
            City VARCHAR(250),
            Country VARCHAR(250),
            StartMonth INT,
            StartYear INT,
            EndMonth INT,
            EndYear INT,
            CurrentlyWorking BOOLEAN,
            PRIMARY KEY (WorkHistoryId)
            );"""
            cursor.execute(query)
            print('method executed')
    
    def CreateProjectHighlights(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"ProjectHighlights")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table ProjectHighlights
            (
            ProjectHighlightsId INT NOT NULL AUTO_INCREMENT,
            WorkHistoryId INT NOT NULL,
            ProjectHighlightsDescription NVARCHAR(500) NULL,
            PRIMARY KEY (ProjectHighlightsId)
            );"""
            cursor.execute(query)
            print('method executed')

    def CreateResponsibilities(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"Responsibilities")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table Responsibilities
            (
            ResponsibilitiesId INT NOT NULL AUTO_INCREMENT,
            WorkHistoryId INT NOT NULL,
            ResponsibilitiesDescription NVARCHAR(500) NULL,
            PRIMARY KEY (ResponsibilitiesId)
            );"""
            cursor.execute(query)
            print('method executed')

    def CreateEducation(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"Education")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table Education
            (
            EducationId INT NOT NULL AUTO_INCREMENT,
            ProfileId INT NOT NULL,
            NameOfInstitution NVARCHAR(500) NULL,
            CourseName NVARCHAR(250) NULL,
            StartYear Int,
            EndYear Int,
            PRIMARY KEY (EducationId)
            );"""
            cursor.execute(query)
            print('method executed')


    def CheckTableExists(self,tableName):
        db_name = connection.settings_dict['NAME']
        cursor = connection.cursor()
        query = "SELECT * FROM information_schema.tables WHERE table_schema = '"+db_name+"' AND table_name = '"+tableName+"' LIMIT 1;"
        cursor.execute(query)
        res =  cursor.fetchall()
        count=cursor.rowcount
        if count>0:
            return True
        else:
            return False
        

  


