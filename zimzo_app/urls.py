from django.urls import path
from zimzo_app import views
from zimzo_users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.index, name='index'),
    path('add_business/', views.add_business, name='add_business'),
    path('list_business/', views.list_business, name='list_business'),
    path('user_login/', auth_views.LoginView.as_view(
        template_name='zimzo_users/user_login.html'), name='user_login'),
    path('user_logout/', auth_views.LogoutView.as_view(
        template_name='zimzo_users/user_logout.html'), name='user_logout'),
    path('register_users/', user_views.register_users, name='register_users'),
]
