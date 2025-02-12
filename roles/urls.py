from django.urls import path
from . import views

urlpatterns = [
    path('', views.role_list, name='role_list'),
    path('create/', views.role_create, name='role_create'),
    path('update/<int:role_id>/', views.role_update, name='role_update'),
    path('delete/<int:role_id>/', views.role_delete, name='role_delete'),
    path('signup/', views.signup, name='signup'),
]
