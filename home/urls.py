from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('register/', views.register, name='register'),
    # path('login/', auth_views.login, {'template_name': 'infor/login.html'}, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name="infor/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]