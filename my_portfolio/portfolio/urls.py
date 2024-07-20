from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('sidemenu/', views.sidemenu_page, name='sidemenu_page'),
    path('skill/', views.skill_page, name='skill_page'),
    path('project/', views.project_page, name='project_page'),
    path('certification/', views.certification_page, name='certification_page'),
]
