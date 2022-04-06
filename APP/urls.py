from .views import Newton
from django.urls import path

urlpatterns = [
    path('', Newton),
]