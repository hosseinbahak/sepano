from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'account'

urlpatterns = [
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sign-up/', UserRegister.as_view(), name='User_register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('custom-login/', UserLogin.as_view(), name='User_login'),
    path('logout/', Logout.as_view(), name='User_logout'),
]