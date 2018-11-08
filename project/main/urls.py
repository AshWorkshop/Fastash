from django.urls import path, include
from project.main.views import index


urlpatterns = [
    path('', index),
]