from django.urls import path, include
from . import views

urlpatterns = [
    path('tutorial/', views.tutorial, name="tutorial" ),
    path('dashboard/', views.dashboard, name='dashboard')
]
