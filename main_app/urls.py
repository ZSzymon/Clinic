from django.contrib.auth import views as auth_views
from django.urls import path

from account import views as account_view

from . import views

urlpatterns = [
    path("", views.home, name="main_app-home"),
    path("about/", views.about, name="main_app-about"),
]
