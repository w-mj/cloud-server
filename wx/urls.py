from django.urls import path
from .views import checksignature
urlpatterns = [
    path('checksignature/', checksignature)
]