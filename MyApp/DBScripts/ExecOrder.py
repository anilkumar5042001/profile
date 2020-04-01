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
        objMySqlTable.CreateProjectHighlights('self')
        objMySqlTable.CreateResponsibilities('self')
        objMySqlTable.CreateEducation('self')
        objMySqlTable.CreateLanguage('self') 
        objMySqlTable.CreateRegistration('self') 
        objMySqlTable.CreateAwards('self')
        objMySqlTable.CreateInterest('self') 
        objMySqlTable.CreateTask('self') 
        objMySqlTable.CreateSkillsCategory('self')
        objMySqlTable.CreateSkills('self')
        objMySqlTable.CreateFavourite('self')
        objMySqlTable.CreateEvent('self')
        objMySqlTable.CreatePassion('self')
        objMySqlTable.CreateShareProfile('self')
        objMySqlTable.CreateFavouriteCategory('self')
        objMySqlTable.CreateTaskComment('self')
        objMySqlTable.CreateTaskCategory('self')
        objMySqlTable.CreateCompany('self')

        #Stored Procedures
        objStoredProcedures=StoredProcedures
        objStoredProcedures.CountryGetAll('self')        
        objStoredProcedures.CountryGetById('self')        
        objStoredProcedures.CountryInsert('self')  
        objStoredProcedures.UserProfileGetById('self')
        objStoredProcedures.UserProfileInsert('self') 
        objStoredProcedures.UserProfileUpdate('self')    
        objStoredProcedures.UserProfileUpdateDomainName('self') 
        objStoredProcedures.UserProfileGetByCompanyDomain('self')
        objStoredProcedures.UserProfileUpdateAboutMe('self')
        objStoredProcedures.CertificationInsert('self')
        objStoredProcedures.CertificationUpdate('self')
        objStoredProcedures.CertificationDelete('self')
        objStoredProcedures.CertificationGetByProfileId('self')
        objStoredProcedures.CertificationGetByCertificationId('self')
        objStoredProcedures.WorkHistoryInsert('self')
        objStoredProcedures.GetWorkHistoryByProfileId('self')
        objStoredProcedures.WorkHistoryGetById('self')
        objStoredProcedures.GetWorkHistoryByProfileIdAndCompanyName('self')
        objStoredProcedures.WorkHistoryUpdate('self')
        objStoredProcedures.WorkHistoryDelete('self')
        objStoredProcedures.ProjectHighlightsInsert('self')
        objStoredProcedures.ProjectHighlightsGetById('self')
        objStoredProcedures.ProjectHighlightsUpdate('self')
        objStoredProcedures.ProjectHighlightsDelete('self')
        objStoredProcedures.ProjectHighlightsDeleteByWorkHistoryId('self')
        objStoredProcedures.ResponsibilitiesInsert('self')
        objStoredProcedures.ResponsibilitiesGetById('self')
        objStoredProcedures.ResponsibilitiesUpdate('self')
        objStoredProcedures.ResponsibilitiesDelete('self')
        objStoredProcedures.ResponsibilitiesDeleteByWorkHistoryId('self')
        objStoredProcedures.EducationInsert('self')
        objStoredProcedures.GetEducationByProfileId('self')
        objStoredProcedures.EducationGetById('self')
        objStoredProcedures.EducationUpdate('self')
        objStoredProcedures.EducationDelete('self')
        objStoredProcedures.LanguageInsert('self')
        objStoredProcedures.GetLanguageByProfileId('self')
        objStoredProcedures.LanguageGetById('self')
        objStoredProcedures.LanguageUpdate('self')
        objStoredProcedures.LanguageDelete('self')
        objStoredProcedures.RegistrationInsert('self')
        objStoredProcedures.RegistrationGetById('self')
        objStoredProcedures.RegistrationUpdate('self')
        objStoredProcedures.AwardsInsert('self')
        objStoredProcedures.GetAwardsById('self')
        objStoredProcedures.GetAwardsNew('self')
        objStoredProcedures.GetAwardsNew('self')
        objStoredProcedures.AwardsUpdateIsNew('self')
        objStoredProcedures.GetAwardsByProfileId('self')
        objStoredProcedures.GetAwardsByAssignTo('self')
        objStoredProcedures.AwardsUpdate('self')
        objStoredProcedures.AwardsUpdateShowInProfile('self')
        objStoredProcedures.AwardsDelete('self')
        objStoredProcedures.InterestInsert('self')
        objStoredProcedures.InterestGetById('self')
        objStoredProcedures.GetInterestByProfileId('self')
        objStoredProcedures.InterestUpdate('self')
        objStoredProcedures.InterestDelete('self')
        objStoredProcedures.CheckLoginCredentials('self')
        objStoredProcedures.TaskInsert('self')
        objStoredProcedures.GetTaskByTaskId('self')
        objStoredProcedures.GetTaskByProfileId('self')
        objStoredProcedures.GetTaskByAssignTo('self')
        objStoredProcedures.TaskUpdate('self')
        objStoredProcedures.TaskDelete('self')
        objStoredProcedures.GetAllTasks('self')
        objStoredProcedures.GetUsers('self')
        objStoredProcedures.SkillsCategoryInsert('self')
        objStoredProcedures.GetSkillCategoryById('self')
        objStoredProcedures.GetSkillCategoryByProfileId('self')
        objStoredProcedures.SkillCategoryUpdate('self')
        objStoredProcedures.SkillCategoryDelete('self')
        objStoredProcedures.SkillsInsert('self')
        objStoredProcedures.GetSkillsByProfileId('self')
        objStoredProcedures.GetSkillsById('self')
        objStoredProcedures.SkillsUpdate('self')
        objStoredProcedures.SkillsDelete('self')
        objStoredProcedures.FavouriteInsert('self')
        objStoredProcedures.GetFavouriteById('self')
        objStoredProcedures.GetFavouriteByProfileId('self')
        objStoredProcedures.FavouriteUpdate('self')
        objStoredProcedures.FavouriteDelete('self')
        objStoredProcedures.EventInsert('self')
        objStoredProcedures.GetEventById('self')
        objStoredProcedures.GetEventByProfileId('self')
        objStoredProcedures.EventUpdate('self')
        objStoredProcedures.EventDelete('self')
        objStoredProcedures.PassionInsert('self')
        objStoredProcedures.GetPassionById('self')
        objStoredProcedures.GetPassionByProfileId('self')
        objStoredProcedures.PassionUpdate('self')
        objStoredProcedures.PassionDelete('self')
        objStoredProcedures.ShareProfileInsert('self')
        objStoredProcedures.ShareProfileGetProfileIdByProfileLink('self')
        objStoredProcedures.FavouriteCategoryInsert('self')
        objStoredProcedures.GetFavouriteCategoryById('self')
        objStoredProcedures.GetFavouriteCategoryByProfileId('self')
        objStoredProcedures.FavouriteCategoryUpdate('self')
        objStoredProcedures.FavouriteCategoryDelete('self')
        objStoredProcedures.TaskCommentInsert('self')
        objStoredProcedures.GetTaskCommentByProfileId('self')
        objStoredProcedures.TaskCommentDelete('self')
        objStoredProcedures.GetTaskCommentByTaskId('self')
        objStoredProcedures.TaskCommentUpdateIsNew('self')
        objStoredProcedures.UserProfileUpdateRegCode('self')
        objStoredProcedures.CompanyGetAll('self')
        objStoredProcedures.WorkHistoryUpdateVerificationCode('self')




#objExecOrder=ExecOrder
#objExecOrder.scriptsOrder('self')
