from django.urls import path
from . import views

# URL CONFIGURATION
urlpatterns = [
    path('', views.admin_homepage)
]
