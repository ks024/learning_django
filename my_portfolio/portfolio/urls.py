from django.urls import path
from . import views


urlpatterns = [
    path("portfolio", views.main_page, name="main_page"),
]

