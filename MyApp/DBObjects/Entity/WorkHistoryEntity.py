class WorkHistoryEntity(object):
    ProfileId=0
    WorkHistoryId=""
    CompanyName=""
    Role=""
    Description=""
    City=""
    Country=""
    StartMonth=""
    StartYear=""
    EndMonth=""
    EndYear=""
    CurrenltyWorking=""

class ProjectHighlightsEntity(object): 
    HighlightId=0
    WorkHistoryId=""
    Description=""

class ResponsibilitiesEntity(object):
    ResponsibilitiesId=0
    WorkHistoryId=""
    Description=""