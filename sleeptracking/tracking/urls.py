from django.contrib import admin
from django.urls import path

from tracking import views

urlpatterns = [
    path('index/', views.index),
    path('event/<int:id>/', views.tracking_details),
    path('data/', views.tracking_data)
]
