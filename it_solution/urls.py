
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
    path("cloud-computing/", views.cloudcomputing, name="cloudcomputing"),
    path("it-consultancy/", views.itconsultancy, name="it-consultancy"),
    path("custom-software/", views.customsoftware, name="custom-software"),
    path("news/<int:pk>/", views.newsdetailsview, name="news-details"),
    path("productdetails/", views.projectdetailsview, name="product-details"),





    path("admin-page/", views.adminview, name= "admin-page"),
    path("addnews/", views.addnewsview, name="addnews"),
    path('create/', views.latest_news_view, name='news_create'),

    path("newslist/", views.newslistview, name= "newslist"),
    path("addproject/", views.addprojectview, name= "addproject"),
    path("projectlist/", views.projectlistview, name= "projectlist"),
    
    
    
]