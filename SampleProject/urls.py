"""SampleProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from MyApp import views
from MyApp import userProfileView
from MyApp import WorkHistoryView
from MyApp import EducationView
from MyApp.AllViews import CertificationView
from MyApp import LanguageView
from MyApp.AllViews import RegistrationView
from MyApp.AllViews import AwardsView
from MyApp.AllViews import InterestView
from MyApp.AllViews import TaskView
from MyApp.AllViews import SkillsCategoryView
from MyApp.AllViews import SkillsView
from MyApp.AllViews import FavouriteView
from MyApp.AllViews import EventsView
from MyApp.AllViews import PassionView
from MyApp.AllViews import ShareProfileView
from MyApp.AllViews import FavouriteCategoryView
from MyApp.AllViews import TaskCommentView

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^file/', include('MyApp.urls')),
    #path(r'^upload/', include('MyApp.urls')),
    url(r'^IdealWeight/', views.IdealWeight),
    url(r'^GetCountryById/', views.GetCountryById),
    url(r'^GetCountries/', views.GetCountries),
    url(r'^InsertCountry/', views.InsertCountry),
    url(r'^GetUserProfileById/', views.GetUserProfileById),
    url(r'^ExecuteDBScripts/', views.ExecuteDBScripts),
    url(r'^UserProfileInsert/', views.UserProfileInsert),
    url(r'^UserProfileUpdate/', views.UserProfileUpdate),
    url(r'^UserProfileUpdateDomainName/', views.UserProfileUpdateDomainName),
    url(r'^UserProfileGetByCompanyDomain/', views.UserProfileGetByCompanyDomain),
    url(r'^UserLoginCheckCredentials/', views.UserLoginCheckCredentials),
    url(r'^GetUserProfileAboutMeById/', userProfileView.GetUserProfileAboutMeById),
    url(r'^UserProfileUpdateAboutMe/', userProfileView.UserProfileUpdateAboutMe),
    url(r'^UploadFile/', views.UploadFile),
    url(r'^WorkHistoryInsert/', WorkHistoryView.WorkHistoryInsert),
    url(r'^WorkHistoryGetById/', WorkHistoryView.GetWorkHistoryById),
    url(r'^GetWorkHistoryByProfileId/', WorkHistoryView.GetWorkHistoryByProfileId),
    url(r'^GetWorkHistoryByProfileIdAndCompanyName/', WorkHistoryView.GetWorkHistoryByProfileIdAndCompanyName),
    url(r'^WorkHistoryUpdate/', WorkHistoryView.WorkHistoryUpdate),
    url(r'^WorkHistoryDelete/', WorkHistoryView.WorkHistoryDelete),
    url(r'^CertificationInsert/', CertificationView.CertificationInsert),
    url(r'^CertificationUpdate/', CertificationView.CertificationUpdate),
    url(r'^CertificationDelete/', CertificationView.CertificationDelete),
    url(r'^CertificationGetByProfileId/', CertificationView.CertificationGetByProfileId),
    url(r'^CertificationGetByCertificationId/', CertificationView.CertificationGetByCertificationId),
    url(r'^ProjectHighlightsInsert/', WorkHistoryView.ProjectHighlightsInsert),
    url(r'^GetProjectHighlightsById/', WorkHistoryView.GetProjectHighlightsById),
    url(r'^ProjectHighlightsUpdate/', WorkHistoryView.ProjectHighlightsUpdate),
    url(r'^ProjectHighlightsDelete/', WorkHistoryView.ProjectHighlightsDelete),
    url(r'^ProjectHighlightsDeleteByWorkHistoryId/', WorkHistoryView.ProjectHighlightsDeleteByWorkHistoryId),
    url(r'^ResponsibilitiesInsert/', WorkHistoryView.ResponsibilitiesInsert),
    url(r'^GetResponsibilitiesById/', WorkHistoryView.GetResponsibilitiesById),
    url(r'^ResponsibilitiesUpdate/', WorkHistoryView.ResponsibilitiesUpdate),
    url(r'^ResponsibilitiesDelete/', WorkHistoryView.ResponsibilitiesDelete),
    url(r'^ResponsibilitiesDeleteByWorkHistoryId/', WorkHistoryView.ResponsibilitiesDeleteByWorkHistoryId),
    url(r'^EducationInsert/', EducationView.EducationInsert),
    url(r'^GetEducationByProfileId/', EducationView.GetEducationByProfileId),
    url(r'^GetEducationById/', EducationView.GetEducationById),
    url(r'^EducationUpdate/', EducationView.EducationUpdate),
    url(r'^EducationDelete/', EducationView.EducationDelete),
    url(r'^LanguageInsert/', LanguageView.LanguageInsert),
    url(r'^GetLanguageById/', LanguageView.GetLanguageById),
    url(r'^GetLanguageByProfileId/', LanguageView.GetLanguageByProfileId),
    url(r'^LanguageUpdate/', LanguageView.LanguageUpdate),
    url(r'^LanguageDelete/', LanguageView.LanguageDelete),
    url(r'^ShareProfileInsert/', ShareProfileView.ShareProfileInsert),
    url(r'^ShareProfileGetProfileIdByProfileLink/', ShareProfileView.ShareProfileGetProfileIdByProfileLink),
    url(r'^RegistrationInsert/', RegistrationView.RegistrationInsert),
    url(r'^GetRegistrationById/', RegistrationView.GetRegistrationById),
    url(r'^RegistrationUpdate/', RegistrationView.RegistrationUpdate),
    url(r'^AwardsInsert/',AwardsView.AwardsInsert),
    url(r'^GetAwardsByProfileId/', AwardsView.GetAwardsByProfileId),
    url(r'^GetAwardsByAssignTo/', AwardsView.GetAwardsByAssignTo),
    url(r'^GetAwardsById/', AwardsView.GetAwardsById),
    url(r'^AwardsUpdate/', AwardsView.AwardsUpdate),
    url(r'^AwardsUpdateShowInProfile/', AwardsView.AwardsUpdateShowInProfile),
    url(r'^AwardsUpdateIsNew/', AwardsView.AwardsUpdateIsNew),
    url(r'^AwardsDelete/', AwardsView.AwardsDelete),
    url(r'^GetAwardsNew/', AwardsView.GetAwardsNew),
    url(r'^InterestInsert/', InterestView.InterestInsert),
    url(r'^GetInterestById/', InterestView.GetInterestById),
    url(r'^GetInterestByProfileId/', InterestView.GetInterestByProfileId),
    url(r'^InterestUpdate/', InterestView.InterestUpdate),
    url(r'^InterestDelete/', InterestView.InterestDelete),
    url(r'^TaskInsert/', TaskView.TaskInsert),
    url(r'^GetTaskByTaskId/', TaskView.GetTaskByTaskId),
    url(r'^GetTaskByProfileId/', TaskView.GetTaskByProfileId),
    url(r'^GetTaskByAssignTo/', TaskView.GetTaskByAssignTo),
    url(r'^TaskUpdate/', TaskView.TaskUpdate),
    url(r'^GetUserNameForAssignTo/', TaskView.GetUserNameForAssignTo),
    url(r'^SkillsCategoryInsert/', SkillsCategoryView.SkillsCategoryInsert),
    url(r'^GetSkillCategoryNameByProfileId/', SkillsCategoryView.GetSkillCategoryNameByProfileId),
    url(r'^GetSkillsCategoryById/', SkillsCategoryView.GetSkillsCategoryById),
    url(r'^SkillsCategoryUpdate/', SkillsCategoryView.SkillsCategoryUpdate),
    url(r'^SkillsCategoryDelete/', SkillsCategoryView.SkillsCategoryDelete),
    url(r'^SkillsInsert/', SkillsView.SkillsInsert),
    url(r'^GetSkillsByProfileId/', SkillsView.GetSkillsByProfileId),
    url(r'^GetSkillsById/', SkillsView.GetSkillsById),
    url(r'^SkillsUpdate/', SkillsView.SkillsUpdate),
    url(r'^SkillsDelete/', SkillsView.SkillsDelete),
    url(r'^FavouriteInsert/', FavouriteView.FavouriteInsert),
    url(r'^GetFavouriteById/', FavouriteView.GetFavouriteById),
    url(r'^GetFavouriteByProfileId/', FavouriteView.GetFavouriteByProfileId),
    url(r'^FavouriteUpdate/', FavouriteView.FavouriteUpdate),
    url(r'^FavouriteDelete/', FavouriteView.FavouriteDelete),
    url(r'^EventInsert/',EventsView.EventInsert),
    url(r'^GetEventByProfileId/', EventsView.GetEventByProfileId),
    url(r'^GetEventById/', EventsView.GetEventById),
    url(r'^EventUpdate/', EventsView.EventUpdate),
    url(r'^EventDelete/', EventsView.EventDelete),
    url(r'^PassionInsert/', PassionView.PassionInsert),
    url(r'^GetPassionByProfileId/', PassionView.GetPassionByProfileId),
    url(r'^GetPassionById/', PassionView.GetPassionById),
    url(r'^PassionUpdate/', PassionView.PassionUpdate),
    url(r'^PassionDelete/', PassionView.PassionDelete),
    url(r'^FavouriteCategoryInsert/', FavouriteCategoryView.FavouriteCategoryInsert),
    url(r'^GetFavouriteCategoryByProfileId/', FavouriteCategoryView.GetFavouriteCategoryByProfileId),
    url(r'^GetFavouriteCategoryById/', FavouriteCategoryView.GetFavouriteCategoryById),
    url(r'^FavouriteCategoryUpdate/', FavouriteCategoryView.FavouriteCategoryUpdate),
    url(r'^FavouriteCategoryDelete/', FavouriteCategoryView.FavouriteCategoryDelete),
    url(r'^TaskCommentInsert/',TaskCommentView.TaskCommentInsert),
    url(r'^GetTaskCommentByProfileId/',TaskCommentView.GetTaskCommentByProfileId),
    url(r'^GetTaskCommentByTaskId/',TaskCommentView.GetTaskCommentByTaskId),
    url(r'^TaskCommentDelete/',TaskCommentView.TaskCommentDelete),
    url(r'^TaskCommentUpdateIsNew/',TaskCommentView.TaskCommentUpdateIsNew),
    
    


    
    
    
    
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)