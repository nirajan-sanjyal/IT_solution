
from django.urls import path

from it_solution import views

urlpatterns = [
    path("", views.homeview, name="home"),
    
    
]