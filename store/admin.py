from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Product)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'count')
    list_filter = ('name', 'category', 'price',)
