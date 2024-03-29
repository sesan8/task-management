from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('', views.dashboard, name='dashboard'),
    path('add_task/', views.add_task, name='add_task'),
]
