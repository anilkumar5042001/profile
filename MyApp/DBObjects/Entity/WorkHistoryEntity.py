class WorkHistoryEntity(object):
    ProfileId=0
    WorkHistoryId=""
    CompanyName=""
    ProjectName=""
    Role=""
    Description=""
    City=""
    Country=""
    StartMonth=""
    StartYear=""
    EndMonth=""
    EndYear=""
    CurrentlyWorking=""
    CompanyEmailId=""

class ProjectHighlightsEntity(object): 
    HighlightId=0
    WorkHistoryId=""
    Description=""

class ResponsibilitiesEntity(object):
    ResponsibilitiesId=0
    WorkHistoryId=""
    Description=""