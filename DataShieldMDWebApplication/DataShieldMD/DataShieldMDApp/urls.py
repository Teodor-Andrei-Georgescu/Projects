from django.urls import path,include
from . import views
#from rest_framework.authtoken.views import obtain_auth_token
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('how-we-do-it/', views.how_we_do_it, name='how_we_do_it'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
]