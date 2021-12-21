from rest_framework import serializers
from event_controller.models import EventMain, EventFeature, EventAttendant
from user.serializers import AddressGlobalSerializer, CustomUserSerializer



class EventFeatureSerializer(serializers.ModelSerializer):
    eventmain = serializers.CharField(read_only = True)
    eventmain_id = serializers.IntegerField(write_only =True)

    class Meta:
        model = EventFeature
        fields = '__all__'

class EventMainSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    author_id = serializers.IntegerField(write_only=True)
    address_info = AddressGlobalSerializer(read_only=True)
    address_info_id = serializers.IntegerField(write_only=True)
    event_features = EventFeatureSerializer(read_only=True, many=True)

    class Meta:
        model = EventMain
        fields = '__all__'

class EventAttendantSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    user = CustomUserSerializer(read_only=True)
    eventmain = serializers.CharField(read_only = True)
    eventmain_id = serializers.IntegerField(write_only =True)

    class Meta:
        model = EventAttendant
        fields = '__all__'