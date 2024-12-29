
from django.urls import path

from it_solution import views

app_name = 'it_solution'

urlpatterns = [
    path("", views.homeview, name="home"),
    path("about/", views.aboutview, name="about"),
    path("services/", views.servicesview, name="services"),
    path("project/", views.projectview, name="project"),
    path("news/", views.newsview, name="news"),
    path("contact/", views.contactview, name="contact"),
    
    
]