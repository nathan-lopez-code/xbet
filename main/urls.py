from django.urls import path
from .views import index

app_name = "mainApp"

urlpatterns = [
    path('', index, name="home")
]