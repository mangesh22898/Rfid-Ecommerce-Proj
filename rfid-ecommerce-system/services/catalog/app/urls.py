# app/urls.py
from django.urls import path
from .views import CatalogView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("api/catalog", CatalogView.as_view()),
]
