from rest_framework import serializers
from .models import *


class ProductCreateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, help_text=("string"))
    price = serializers.CharField(required=True, help_text=("string"))
    count = serializers.IntegerField(required=False, default=1,help_text=("string"))
    category = serializers.IntegerField(required=False, default=0, help_text=("string"))
    description = serializers.CharField(required=False, default='', help_text=("string"))
    image = serializers.ImageField(required=False, help_text=("file"))


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, help_text=("string"))
    price = serializers.CharField(required=True, help_text=("string"))
    category = serializers.SerializerMethodField()
    count = serializers.IntegerField(required=False, default=1,help_text=("string"))
    description = serializers.CharField(required=False, default='', help_text=("string"))
    image = serializers.ImageField(required=False, help_text=("file"))

    class Meta:
        model = Product
        fields = '__all__'
        
    def get_category(self, obj):
        return dict(CATEGORY_CHOICES).get(obj.category)
