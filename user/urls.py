from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [

    path('admin_login/', views.admin_login_view, name='admin_login'),
    path('admin/dashboard/', views.dashboard_view, name='dashboard'),
]