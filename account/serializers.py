from django.contrib.auth.models import Group, User
from rest_framework import serializers
from rest_framework.response import Response
from .models import *
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\d{11}$', 
    message = "Phone number must be entered in '0913 123 4567' format also 11 digits allowed."
)

password_regex = RegexValidator(
    regex=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',
    message="Your password must be at least 8 characters and contain at least one letter and one digit."
)

email_regex = RegexValidator(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

class UserRegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True, help_text=("string") )
    last_name = serializers.CharField(required=True, help_text=("string"))
    mobile = serializers.CharField(required=True, validators=[phone_regex], help_text=("string"))
    password = serializers.CharField(required=True, validators=[password_regex], help_text=("string"))
    gender = serializers.CharField(required=False, help_text=("int"))
    birth_date = serializers.DateField(required=False, help_text=("Date field"))
    email = serializers.EmailField(required=False, validators=[email_regex], allow_blank=True, help_text=("string"))
    
 
    @staticmethod
    def get_user(mobile: str):
        """Fetche user object"""
        try:
            user = User.objects.filter(mobile=mobile)
        except UserProfile.DoesNotExist:
            if user.mobile != mobile:
                raise serializers.ValidationError(
                (
                    "Your account as {mobile} does not "
                    "registered."
                )
            )
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, help_text=("string"))
    password = serializers.CharField(required=True, help_text=("string"))
