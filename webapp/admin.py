from django.contrib import admin
from webapp.models import UserProfile


# Register your models here.
class AdminProfile(admin.ModelAdmin):
    list_display = ["email", "password"]


admin.site.register(UserProfile, AdminProfile)
