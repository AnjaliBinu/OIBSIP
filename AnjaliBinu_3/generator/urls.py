from django.urls import path
from . import views

# Routing within your generator app
urlpatterns = [
    path('', views.home, name='home'),
    path('password/', views.password, name='password'),
]