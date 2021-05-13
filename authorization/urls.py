from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

urlpatterns = [

    path('', include('django.contrib.auth.urls')),
    path('logout/', views.LogoutView.as_view(), name='logout'),

]