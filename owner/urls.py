from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_details_view, name='detail'),
    path('create/', views.product_create_view, name='create'),
    path('details/<int:id>/', views.product_details_view, name='details'),
    path('delete/<int:my_id>/', views.product_delete_view, name='delete'),
    path('details/', views.product_list_view, name='list'),
     path('login/', views.login_view, name='login_view'),
     path('logout/', views.logout_request, name='logout'),
    #path('login/', auth_views.login, {'template_name': 'product/login.html'}, name='login')
]