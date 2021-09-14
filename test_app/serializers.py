from rest_framework import serializers
from test_app.models import TestModel



class SimpleSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    phone_number = serializers.IntegerField()
    is_active = serializers.BooleanField()
    amount = serializers.FloatField()
    extra_name = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True) 
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data): #validated_data is the data you obtained after being able to validate data
        return TestModel.objects.create(**validated_data)