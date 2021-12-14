from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from event_controller.models import EventMain
from event_controller.serializers import EventMainSerializer, EventFeatureSerializer, EventAttendantSerializer
from user.models import AddressGlobal
from user.serializers import AddressGlobalSerializer

# Create your views here.

class EventMainView(ModelViewSet):
    serializer_class = EventMainSerializer
    queryset = EventMain.objects.select_related(
        "author","address_info").prefetch_related("event_features")

    def create(self, request, *args, **kwargs):
        a_serializer = AddressGlobalSerializer(data=request.data)
        a_serializer.is_valid(raise_exception=True)
        a_serializer.save()

        data = {**request.data, "address_info_id": a_serializer.data["id"]}
        return super().create(request, *args, **kwargs)