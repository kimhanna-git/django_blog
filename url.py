from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about') ##empty path.
    # home view views.home and name is blog_home
]