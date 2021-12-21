from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from event_controller.views import EventMainView,EventAttenderView

router = DefaultRouter()
router.register("event", EventMainView)
router.register("event-attender", EventAttenderView)

urlpatterns = [
    path("", include(router.urls))
]