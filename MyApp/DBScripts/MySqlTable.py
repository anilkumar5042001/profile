
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

    def CreateShareProfile(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"ShareProfile")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table ShareProfile(
            ShareProfileId INT NOT NULL AUTO_INCREMENT,
            ProfileId INT NOT NULL,
            EmailId  NVARCHAR(250) NULL,
            ProfileLink NVARCHAR(1000) NULL,
            ExpiryDate DATETIME NULL,
            SharedWith NVARCHAR(250) NULL,
            Message NVARCHAR(1000) NULL,
            PRIMARY KEY (ShareProfileId)
            );"""
            cursor.execute(query)
            print('ShareProfile table created')

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
            City VARCHAR(250) NULL,
            Country VARCHAR(250) NULL,
            AboutMe NVARCHAR(500) NULL,
            Password NVARCHAR(250) NULL,
            CompanyDomain NVARCHAR(250) NULL,
            ProfileImageName NVARCHAR(300) NULL,
            RegGuid NVARCHAR(250) NULL,
            ActivationCode NVARCHAR(10) NULL,
            IsActivated BOOLEAN,
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
            ProjectName NVARCHAR(250) NULL,
            Role NVARCHAR(250) NULL,
            Description NVARCHAR(500),
            City VARCHAR(250),
            Country VARCHAR(250),
            StartMonth INT,
            StartYear INT,
            EndMonth INT,
            EndYear INT,
            CurrentlyWorking BOOLEAN ,
            CompanyEmailId NVARCHAR(250),
            WHGuid NVARCHAR(250) NULL,
            VerificationCode NVARCHAR(10) NULL,
            IsVerified BOOLEAN,
            CompanyId INT NOT NULL,
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
            HighlightId INT NOT NULL AUTO_INCREMENT,
            WorkHistoryId INT NOT NULL,
            Description NVARCHAR(500) NULL,
            PRIMARY KEY (HighlightId)
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
            Description NVARCHAR(500) NULL,
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
            Degree NVARCHAR(250) NULL,
            StartYear Int,
            EndYear Int,
            EducationDescription NVARCHAR(500) NULL,
            PRIMARY KEY (EducationId)
            );"""
            cursor.execute(query)
            print('method executed')

    def CreateLanguage(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"Language")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table Language
            (
            LanguageId INT NOT NULL AUTO_INCREMENT,
            ProfileId INT NOT NULL,
            LanguageName NVARCHAR(250) NULL,
            LanguageLevel NVARCHAR(250) NULL,
            PRIMARY KEY (LanguageId)
            );"""
            cursor.execute(query)
            print('method executed')



    def CreateRegistration(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"Registration")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table Registration
            (
            RegistrationId INT NOT NULL AUTO_INCREMENT,           
            EmailId NVARCHAR(500) NULL,
            Password NVARCHAR(250) NULL,
            PRIMARY KEY (RegistrationId)
            );"""
            cursor.execute(query)
            print('method executed')

    def CreateAwards(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"Awards")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table Awards
            (
            AwardId INT NOT NULL AUTO_INCREMENT,
            ProfileId INT NOT NULL,
            AwardTitle NVARCHAR(250) NULL,
            AwardDescription NVARCHAR(500) NULL,
            AssignTo INT NULL,
            CreatedOn DATETIME NOT NULL ON UPDATE CURRENT_TIMESTAMP,
            CompanyDomain NVARCHAR(250) NULL,
            CompanyName NVARCHAR(250) NULL,
            ShowInProfile BOOLEAN,
            IsNew BOOLEAN,
            PRIMARY KEY (AwardId)
            );"""
            cursor.execute(query)
            print('method executed')

    def CreateInterest(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"Interest")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table Interest
            (
            InterestId INT NOT NULL AUTO_INCREMENT,
            ProfileId INT NOT NULL,
            InterestName NVARCHAR(250) NULL,
            PRIMARY KEY (InterestId)
            );"""
            cursor.execute(query)
            print('method executed')
    
    def CreateTask(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"Task")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table Task
            (
            TaskId INT NOT NULL AUTO_INCREMENT,
            TaskCategoryId INT NOT NULL,
            ProfileId INT NOT NULL,
            TaskTitle NVARCHAR(250) NULL,
            Description NVARCHAR(500) NULL,
            DueDate DATETIME,
            AssignTo INT,
            CreatedBy INT,
            TaskStatus VARCHAR(250) NULL,
            TaskDuration DECIMAL(6,2),
            TaskOrder INT NOT NULL,
            PRIMARY KEY (TaskId)
            );"""
            cursor.execute(query)
            print('method executed')
    
    def CreateTaskCategory(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"TaskCategory")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table TaskCategory
            (
            TaskCategoryId INT NOT NULL AUTO_INCREMENT,
            ProfileId INT NOT NULL,
            TaskCategoryName NVARCHAR(250) NULL,
            PRIMARY KEY (TaskCategoryId)
            );"""
            cursor.execute(query)
            print('method executed')

    def CreateSkillsCategory(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"SkillsCategory")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table SkillsCategory
            (
            SkillCategoryId INT NOT NULL AUTO_INCREMENT,
            ProfileId INT NOT NULL,
            SkillCategoryName NVARCHAR(250) NULL,
            PRIMARY KEY (SkillCategoryId)
            );"""
            cursor.execute(query)
            print('method executed')

    def CreateSkills(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"Skills")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table Skills
            (
            SkillId INT NOT NULL AUTO_INCREMENT,
            ProfileId INT NOT NULL,
            SkillCategoryId INT NOT NULL,
            SkillName NVARCHAR(250) NULL,
            PRIMARY KEY (SkillId)
            );"""
            cursor.execute(query)
            print('method executed')

    def CreateFavourite(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"Favourite")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table Favourite
            (
            FavouriteId INT NOT NULL AUTO_INCREMENT,
            ProfileId INT NOT NULL,
            FavouriteCategoryId INT NOT NULL,
            FavouriteName NVARCHAR(250) NULL,
            FavouriteLink NVARCHAR(250) NULL,           
            PRIMARY KEY (FavouriteId)
            );"""
            cursor.execute(query)
            print('Favourite table created')

    def CreateEvent(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"Event")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table Event(
            EventId INT NOT NULL AUTO_INCREMENT,
            ProfileId INT NOT NULL,
            EventCategoryId INT NOT NULL,
            EventName NVARCHAR(250) NULL,
            Description NVARCHAR(500) NULL,
            StartDate DATETIME  NULL,
            EndDate DATETIME NULL,
            PRIMARY KEY (EventId)
            );"""
            cursor.execute(query)
            print('Event table created')

    def CreatePassion(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"Passion")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table Passion(
            PassionId INT NOT NULL AUTO_INCREMENT,
            ProfileId INT NOT NULL,
            PassionName NVARCHAR(250) NULL,
            Description NVARCHAR(500) NULL,
            PRIMARY KEY (PassionId)
            );"""
            cursor.execute(query)
            print('Passion table created')

    def CreateFavouriteCategory(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"FavouriteCategory")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table FavouriteCategory(
            FavouriteCategoryId INT NOT NULL AUTO_INCREMENT,
            ProfileId INT NOT NULL,
            FavouriteCategoryName VARCHAR(250) NULL,
            PRIMARY KEY (FavouriteCategoryId)
            );"""
            cursor.execute(query)
            print('FavouriteCategory table created')

    def CreateTaskComment(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"TaskComment")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table TaskComment(
            TaskCommentId INT NOT NULL AUTO_INCREMENT,
            TaskId INT NOT NULL,
            ProfileId INT NOT NULL,
            Comment VARCHAR(500)  NULL,
            CommentedBy INT  NULL,
            CommentedOn DATETIME  NULL,
            IsNew BOOLEAN,
            PRIMARY KEY (TaskCommentId)
            );"""
            cursor.execute(query)
            print('TaskComment table created')

    def CreateCompany(self):
        objMySqlTable=MySqlTable
        tblExists=objMySqlTable.CheckTableExists(self,"Company")
        if tblExists==False:
            cursor = connection.cursor()
            query = """create table Company
            (
            CompanyId INT NOT NULL AUTO_INCREMENT,
            CompanyName NVARCHAR(250) NULL,
            DomainName NVARCHAR(250) NULL,
            Logo NVARCHAR(250) NULL,
            PRIMARY KEY (CompanyId)
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
        

  



