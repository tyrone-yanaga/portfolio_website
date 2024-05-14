from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('c', views.project_list, name='index'),
    path('<int:pk>/', views.full_view, name='full_view'),
]