from django.urls import path, include
from gateway.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view()),
]