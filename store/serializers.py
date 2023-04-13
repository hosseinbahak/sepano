from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, help_text=("string"))
    price = serializers.CharField(required=True, help_text=("string"))
    count = serializers.IntegerField(required=False, help_text=("string"))
    category = serializers.IntegerField(required=False, help_text=("string"))
    description = serializers.CharField(required=False, help_text=("string"))