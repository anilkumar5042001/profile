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
from MyApp.AllViews import CertificationView

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
    url(r'^CertificationInsert/', CertificationView.CertificationInsert),
]
