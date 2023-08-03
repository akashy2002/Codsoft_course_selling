from django.contrib import admin
from django.urls import path

from akash.views import home, coursePage, signup, login, logout, checkout, forgetpage

urlpatterns = [
    path('', home.index, name="home"),
    path('signup', signup, name="SignupPage"),
    path('login', login, name="LoginPage"),
    path('logout', logout, name="Logout"),
    path('forget', forgetpage, name="forgetpage"),
    path('checkout/<str:slug>', checkout, name="checkout"),
    path('course/<str:slug>', coursePage, name="coursePage")
]
