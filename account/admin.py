from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)
    list_filter = ('user',)
