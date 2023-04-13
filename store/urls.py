from django.urls import path
from .views import *

app_name = 'store'

urlpatterns = [
    path('product/', ProductView.as_view(), name=''),
]