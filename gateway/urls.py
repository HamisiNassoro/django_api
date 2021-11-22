from django.urls import path, include
from gateway.views import LoginView,RegisterView, RefreshView, TestException

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('refresh/', RefreshView.as_view()),
    path('secure-info/', TestException.as_view())
]