from django.urls import path
from . import views  # Imports the math logic from your calculator/views.py

urlpatterns = [
    path('', views.bmi_calculator, name='bmi_calculator'),  # Runs your calculator on the homepage!
]