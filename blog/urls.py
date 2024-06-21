from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('all/', views.BlogView.as_view(), name='blog_all'),
    path('create-post/', views.AddPostView.as_view(), name='create_post'),
    path('delete/<int:pk>/', views.DeletePostView.as_view(), name='delete_post')
]
