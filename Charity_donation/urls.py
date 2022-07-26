"""Charity_donation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from share.views import LandingPage, AddDonation, UserProfil, get_institution_by_category, donation_taken
from accounts.views import Register, Login
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage.as_view(), name="landing-page"),
    path('add-donation/', AddDonation.as_view(), name="add-donation"),
    path('profil/', UserProfil.as_view(), name="profil"),
    path('get_institution,_by_category/', get_institution_by_category, name="get_institution_by_category"),
    path('donation_taken/', donation_taken, name="donation_taken"),


    path('login/', Login.as_view(), name="login"),
    path('register/', Register.as_view(), name="register"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]