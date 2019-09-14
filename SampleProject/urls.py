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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^IdealWeight/', views.IdealWeight),
    url(r'^GetCountryById/', views.GetCountryById),
    url(r'^GetCountries/', views.GetCountries),
    url(r'^InsertCountry/', views.InsertCountry),
    url(r'^GetUserProfileById/', views.GetUserProfileById),
    url(r'^ExecuteDBScripts/', views.ExecuteDBScripts),
    url(r'^UserProfileInsert/', views.UserProfileInsert),
    url(r'^UserProfileUpdate/', views.UserProfileUpdate),
    url(r'^GetUserProfileAboutMeById/', userProfileView.GetUserProfileAboutMeById),
    url(r'^UserProfileUpdateAboutMe/', userProfileView.UserProfileUpdateAboutMe),
    url(r'^UploadFile/', views.UploadFile),
    url(r'^WorkHistoryInsert/', WorkHistoryView.WorkHistoryInsert),
    url(r'^WorkHistoryGetById/', WorkHistoryView.GetWorkHistoryById),
    url(r'^WorkHistoryUpdate/', WorkHistoryView.WorkHistoryUpdate),
    url(r'^CertificationInsert/', CertificationView.CertificationInsert),
    url(r'^CertificationUpdate/', CertificationView.CertificationUpdate),
    url(r'^CertificationDelete/', CertificationView.CertificationDelete),
    url(r'^CertificationGetByProfileId/', CertificationView.CertificationGetByProfileId),
    url(r'^CertificationGetByCertificationId/', CertificationView.CertificationGetByCertificationId),
    url(r'^ProjectHighlightsInsert/', WorkHistoryView.ProjectHighlightsInsert),
    url(r'^GetProjectHighlightsById/', WorkHistoryView.GetProjectHighlightsById),
    url(r'^ProjectHighlightsUpdate/', WorkHistoryView.ProjectHighlightsUpdate),
    url(r'^ResponsibilitiesInsert/', WorkHistoryView.ResponsibilitiesInsert),
    url(r'^GetResponsibilitiesById/', WorkHistoryView.GetResponsibilitiesById),
    url(r'^ResponsibilitiesUpdate/', WorkHistoryView.ResponsibilitiesUpdate),
    url(r'^EducationInsert/', EducationView.EducationInsert),
    url(r'^GetEducationById/', EducationView.GetEducationById),
    url(r'^EducationUpdate/', EducationView.EducationUpdate),
    url(r'^EducationDelete/', EducationView.EducationDelete),
    url(r'^LanguageInsert/', LanguageView.LanguageInsert),
    url(r'^GetLanguageById/', LanguageView.GetLanguageById),
    url(r'^LanguageUpdate/', LanguageView.LanguageUpdate),
    url(r'^LanguageDelete/', LanguageView.LanguageDelete),
     url(r'^RegistrationInsert/', RegistrationView.RegistrationInsert),
    url(r'^GetRegistrationById/', RegistrationView.GetRegistrationById),
    url(r'^RegistrationUpdate/', RegistrationView.RegistrationUpdate),
     url(r'^AwardsInsert/',AwardsView.AwardsInsert),
    url(r'^GetAwardsByProfileId/', AwardsView.GetAwardsByProfileId),
    url(r'^GetAwardsById/', AwardsView.GetAwardsById),
    url(r'^AwardsUpdate/', AwardsView.AwardsUpdate),
    url(r'^AwardsDelete/', AwardsView.AwardsDelete),
    
    


    
    
    
    
]
