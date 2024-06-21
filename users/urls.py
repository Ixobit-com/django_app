from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('sign-in/', views.LoginView.as_view(), name='login'),
    path('sign-up/', views.RegistrationView.as_view(), name='register'),
    path('user-details/', views.CurrentUserView.as_view(), name='user_details'),
]