from django.contrib import admin
from .models import UserProfile


# Register your models here.
class AdminProfile(admin.ModelAdmin):
    list_display = ["user", "firstName", 'lastName', "loc"]


admin.site.register(UserProfile,AdminProfile)
