from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from event_controller.models import EventAttendant, EventMain
from event_controller.serializers import EventMainSerializer, EventFeatureSerializer, EventAttendantSerializer
from user.models import AddressGlobal
from user.serializers import AddressGlobalSerializer
from rest_framework.response import Response

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

        e_serializer = self.serializer_class(data=data)
        if not e_serializer.is_valid():
            AddressGlobal.objects.filter(id=a_serializer.data["id"]).delete()
            raise Exception(e_serializer.errors)

        e_serializer.save()

        features = request.data.get("features", None)
        if not features:
            AddressGlobal.objects.filter(id=a_serializer.data["id"]).delete()
            raise Exception("features field is requird")

        if not isinstance(features, list):
            features = [features]

        data = []
        for f in features:
            if not isinstance(f, dict):
                AddressGlobal.objects.filter(id=a_serializer.data["id"]).delete()
                raise Exception("Feature instance must be an object")
            data.append({
                **f, "eventmain_id":e_serializer.data["id"]
            })
        f_serializer = EventFeatureSerializer(data=data, many=True)
        if not f_serializer.is_valid():
            AddressGlobal.objects.filter(id=a_serializer.data["id"]).delete()
            raise Exception(f_serializer.errors)

        f_serializer.save()

        return Response(self.serializer_class(self.get_queryset().get(id=e_serializer.data["id"])).data, status=201)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        evt_serializer = self.serializer_class(
            data=request.data, instance=instance, partial=True)
        evt_serializer.is_valid(raise_exception=True)
        evt_serializer.save()

        address_serializer = AddressGlobalSerializer(
            data=request.data, instance=instance.address_info, partial=True)
        address_serializer.is_valid(raise_exception=True)
        address_serializer.save()

        features = request.data.get("features", None)
        if features:
            if not isinstance(features, list):
                features = [features]

            data = []
            for f in features:
                if not isinstance(f, dict):
                    raise Exception("Feature instance must be an object")
                data.append({
                    **f, "eventmain_id": evt_serializer.data["id"]
                })

            f_serializer = EventFeatureSerializer(data=data, many=True)
            f_serializer.is_valid(raise_exception=True)
            f_serializer.save()

        return Response(self.serializer_class(self.get_object()).data)


class EventAttenderView(ModelViewSet):
    serializer_class = EventAttendantSerializer
    queryset = EventAttendant.objects.select_related("user","eventmain")

    def create(self, request, *args, **kwargs):
        at_serializer = self.serializer_class(data=request.data)
        at_serializer.is_valid(raise_exception=True)

        evt = EventMainView.queryset.filter(
            id=at_serializer.validated_data["eventmain_id"])
        if not evt:
            raise Exception("Event Does Not Exist")

        evt = evt[0]

        #check if user already exists
        is_user_reg = self.queryset.filter(
            eventmain_id=evt.id, user_id=at_serializer.validated_data["user_id"])

        if is_user_reg:
            raise Exception("You already registered for event")

        #check if maximum seat has not reached
        at_count = self.queryset.filter(eventmain_id=evt.id).count()

        if not at_count < evt.max_seat: #if at_count >= evt.max_seat: -----could also use this
            raise Exception("Maximum attenders taken")

        #check time
        at_time = at_serializer.validated_data["time"]
        if at_time < evt.time:
            raise Exception("You are too early")

        at_serializer.save()
        return Response(at_serializer.data, status=201)

