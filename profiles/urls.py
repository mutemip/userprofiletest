from django.urls import path
from .views import ProfileListAPIView


urlpatterns = [
    path('profile/', ProfileListAPIView.as_view()),
]
