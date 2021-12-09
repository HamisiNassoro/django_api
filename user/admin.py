from django.contrib import admin
from user.models import CustomUser, UserProfile, AddressGlobal

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(AddressGlobal)

