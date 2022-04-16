from django.contrib import admin
from django.urls import path, include   
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/<int:portfolio_id>/', views.portfolio_details,   name='portfolio_details'),
]
