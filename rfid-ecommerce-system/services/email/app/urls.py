from django.urls import path
from .views import EmailView

urlpatterns = [
    path("api/email", EmailView.as_view()),
]
