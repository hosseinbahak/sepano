from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics
from .serializers import *
from unidecode import unidecode
from rest_framework import status
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView

class UserRegister(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        #try:
        user_obj, user_bool = User.objects.get_or_create(
            username = unidecode(serializer.validated_data.get("mobile"))
        )
        if user_bool:
            password = unidecode(serializer.validated_data.get("password"))
            hashed_password = make_password(password)
            user_obj.password = hashed_password
            user_obj.first_name = serializer.validated_data.get("first_name")
            user_obj.last_name = serializer.validated_data.get("last_name")
            user_obj.email = serializer.validated_data.get("email")
            user_obj.save()
            

        user_profile_obj, user_profile_bool = UserProfile.objects.get_or_create(
            user = user_obj,   
        )
        if user_profile_bool:
            user_profile_obj.gender = serializer.validated_data.get("gender")
            user_profile_obj.birth_date = serializer.validated_data.get("birth_date")
            user_profile_obj.save()
        
        user = authenticate(
            username = unidecode(serializer.validated_data.get("mobile")),
            password = unidecode(serializer.validated_data.get("password"))
        )

        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            token = str(refresh.access_token)
            return Response(
                            response_func(True, "user registered successfully", {'access': token, 'refresh': str(refresh)}),  
                            status=status.HTTP_200_OK
                        )
        else:
            return Response(
                            response_func(True, "login failed", {'user_exist': False}),  
                            status=status.HTTP_401_UNAUTHORIZED
                        )

        # except Exception as e:
        #     return Response(
        #                     response_func(False, str(e), {'user_exist': False}),  
        #                     status=status.HTTP_400_BAD_REQUEST
        #         )

class UserLogin(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            
            user = authenticate(
                username = unidecode(serializer.validated_data.get("username")),
                password = unidecode(serializer.validated_data.get("password"))
            )

            if user is not None:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                token = str(refresh.access_token)
                return Response(
                                response_func(True, "user registered successfully", {'access': token, 'refresh': str(refresh)}),  
                                status=status.HTTP_200_OK
                            )
            else:
                return Response(
                                response_func(True, "wrong username or password", {'user_exist': False}),  
                                status=status.HTTP_401_UNAUTHORIZED
                            )

        except Exception as e:
            return Response(
                            response_func(False, str(e), {'user_exist': False}),  
                            status=status.HTTP_400_BAD_REQUEST
                )
    
class Logout(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            
            #token can be put in block list or remove from client side
            
            if self.request.user is not None:
                return Response(
                                response_func(True, "user logged out", {'user': str(self.request.user)}),  
                                status=status.HTTP_200_OK
                            )
            else:
                return Response(
                                response_func(True, "user not found", {}),  
                                status=status.HTTP_401_UNAUTHORIZED
                            )

        except Exception as e:
            return Response(
                            response_func(False, str(e), {}),  
                            status=status.HTTP_400_BAD_REQUEST
                )

def response_func(status: bool ,msg: str, data: dict):
    return {
        'status': status,
        'message': msg,
        'data': data
    } 


