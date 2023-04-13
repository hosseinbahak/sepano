from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, help_text=("string"))
    price = serializers.CharField(required=True, help_text=("string"))
    count = serializers.IntegerField(required=False, default=1,help_text=("string"))
    category = serializers.IntegerField(required=False, default=0, help_text=("string"))
    description = serializers.CharField(required=False, default='', help_text=("string"))