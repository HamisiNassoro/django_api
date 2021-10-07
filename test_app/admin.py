from django.contrib import admin
from test_app.models import Blog,Car

admin.site.register((Blog,Car))








# from .models import TestModel, ModelX, ModelY

# # Register your models here.
# admin.site.register((TestModel,ModelX,ModelY))
# #admin.site.register(ModelX)