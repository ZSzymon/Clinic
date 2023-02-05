from django.urls import path
from . import views
from account import views as account_view

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile/', account_view.profile, name='account-profile'),
    path('register/', account_view.register, name='account-register'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html',
                                                redirect_field_name='account-profile'), name='account-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='account-logout'),
    path('notebook/', account_view.notebook, name='account-notebook'),
    path('notebook/update_note/<str:pk>', account_view.update_note, name='account-update_note'),
    path('notebook/delete_note/<str:pk>', account_view.delete_note, name='account-delete_note'),
]
