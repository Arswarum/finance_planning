from django.contrib import admin
from django.urls import path, include
from . import views

# Maybe have to refactor in the future

urlpatterns = [
    path('', views.project_list, name='list'),
    path('<slug:project_slug>', views.project_detail, name='detail'),
]