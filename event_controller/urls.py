from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from event_controller.views import EventMainView

router = DefaultRouter()
router.register("event", EventMainView)

urlpatterns = [
    path("", include(router.urls))
]