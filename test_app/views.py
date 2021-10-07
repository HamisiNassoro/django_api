from test_app.models import Blog
from django_seed import Seed

seeder = Seed.seeder()

seeder.add_entity(Blog, 20) # we can specify the model you want from the models and the number of times you want to generate the model

def execute():
    seeder.execute()
    print("seeding completed")
















# from django.db.models import manager
# from django.shortcuts import render
# from django.http import JsonResponse, response
# from rest_framework.views import APIView
# from rest_framework import generics
# from test_app.models import TestModel
# from .serializers import SimpleSerializer
# from rest_framework import viewsets

# Create your views here.
#class based views

# class Simple(APIView):

#     def get(self,request):
#         content = TestModel.objects.all()     #you can specify by .objects.first()
#         return JsonResponse({"data":SimpleSerializer(content, many = True).data})
#     def post(self, request):
#         serializer = SimpleSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # print(new_test_content)
#         return JsonResponse({"data":serializer.data})

#     def put(self, request, *args, **kwargs): #args is where your non key word arguments are held while kwargs is where key word arguments are held
#         model_id = kwargs.get("id",None)
#         if not model_id:
#             return JsonResponse({"error":"method /PUT/ not allowed"})
#         try:
#             instance = TestModel.objects.get(id=model_id)
#         except:
#             return JsonResponse({"error":"Object does not exist"})

#         serializer = SimpleSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return JsonResponse({"data":serializer.data})


# class SimpleGenerics(generics.ListCreateAPIView):
#       queryset = TestModel.objects.all()
#       serializer_class = SimpleSerializer

# class SimpleGenericsUpdate(generics.UpdateAPIView):
#     queryset = TestModel.objects.all()
#     serializer_class = SimpleSerializer
#     lookup_field = "id" #this works for the path url <int:id>

# class SimpleViewset(viewsets.ModelViewSet):
#       queryset = TestModel.objects.all()
#       serializer_class = SimpleSerializer