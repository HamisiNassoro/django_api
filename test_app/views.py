from django.db.models import manager
from django.shortcuts import render
from django.http import JsonResponse, response
from rest_framework.views import APIView
from test_app.models import TestModel
from .serializers import SimpleSerializer

# Create your views here.
#class based views

class Simple(APIView):

    def get(self,request):
        content = TestModel.objects.all()     #you can specify by .objects.first()
        return JsonResponse({"data":SimpleSerializer(content, many = True).data})
    def post(self, request):
        serializer = SimpleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # print(new_test_content)
        return JsonResponse({"data":serializer.data})