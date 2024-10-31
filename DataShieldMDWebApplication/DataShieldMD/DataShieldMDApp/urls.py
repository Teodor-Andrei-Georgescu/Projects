from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('how-we-do-it/', views.how_we_do_it, name='how_we_do_it'),
    path('api-token-auth/',obtain_auth_token),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]