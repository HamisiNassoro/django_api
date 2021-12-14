from django.contrib import admin
from event_controller.models import EventMain, EventFeature, EventAttendant

# Register your models here.
admin.site.register(EventMain)
admin.site.register(EventFeature)
admin.site.register(EventAttendant)