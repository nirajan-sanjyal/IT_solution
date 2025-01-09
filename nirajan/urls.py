from django.urls import path

from nirajan import views

app_name = 'nirajan'

urlpatterns = [

    # path('admin_signup/', views.admin_login_view, name='signup'),
    path('login/admin_login/', views.login_view, name='admin_login'),
    path('admin/dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/',views.logout_view, name="logout")
]