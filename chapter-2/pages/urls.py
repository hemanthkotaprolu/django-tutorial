# pages/urls.
from django.urls import path
from .views import homePageView

urlPatterns = [
        path("", homePageView, name="home")
        ]
