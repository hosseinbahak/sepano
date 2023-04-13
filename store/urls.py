from django.urls import path
from .views import *

app_name = 'store'

urlpatterns = [
    path('create-product/', ProductCreateView.as_view(), name='product creator'),
    path('list-product/', ProductListView.as_view(), name='product creator')
]