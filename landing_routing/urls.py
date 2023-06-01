from django.urls import path
from . import views  # import views from main app

urlpatterns = [
    path('', views.home, name='home')
]