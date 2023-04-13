from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics
from .serializers import *
from unidecode import unidecode
from rest_framework import status
from .models import *
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django.shortcuts import get_object_or_404
from account.models import UserProfile
from rest_framework.pagination import PageNumberPagination

class ProductCreateView(generics.GenericAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    throttle_classes = (AnonRateThrottle, UserRateThrottle,)

   
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            """
            we assume product with equal name, price and category
            are the same. user can increase quantity of products
            """  
            product_obj, product_bool = Product.objects.get_or_create(
                creator = self.request.user,
                name = serializer.validated_data.get("name"),
                price = serializer.validated_data.get("price"),
                category = serializer.validated_data.get("category")
            )
                        
            if product_bool:
                product_obj.description = serializer.validated_data.get("description")
                product_obj.image = serializer.validated_data.get("image")

                user_profile = get_object_or_404(UserProfile, user=request.user)
                
                if serializer.validated_data.get("category") not in user_profile.favorites:
                    user_profile.favorites.append(serializer.validated_data.get("category"))
                    user_profile.save()
                
            if not serializer.validated_data.get("count"):
                product_obj.counter()
                
            else:
                product_obj.count = product_obj.count + int(serializer.validated_data.get("count"))
            
            product_obj.save()
            
            return Response(
                            response_func(True, "product added successfully", {
                                'product': f"{product_obj.count} new '{product_obj.name}' are now available."
                                }),  
                            status=status.HTTP_201_CREATED
                        )

        except Exception as e:
            return Response(
                            response_func(False, str(e), {}),  
                            status=status.HTTP_400_BAD_REQUEST
                )
            
            
class ProductListView(generics.GenericAPIView):
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    throttle_classes = (AnonRateThrottle, UserRateThrottle,)

    def get(self, request):
        try:
            if request.user.is_authenticated:
                user_profile = UserProfile.objects.get(user=self.request.user)
                
                #all products
                all_products = Product.objects.all().order_by('-id')
                
                # Filter products based on user favorites
                favorite_products = Product.objects.filter(category__in=user_profile.favorites)
                
                # Combine all products and favorite products into one queryset
                queryset = all_products | favorite_products
                
                page = self.paginate_queryset(queryset)
                serializer = self.get_serializer(page, many=True)
                
                return Response(
                    response_func(True, "products returned based on favorite and latest", serializer.data),  
                    status=status.HTTP_200_OK
                )
            else:
                #all products
                all_products = Product.objects.all().order_by('-id')
                page = self.paginate_queryset(all_products)
                serializer = self.get_serializer(page, many=True)
                
                return Response(
                    response_func(True, "latest products returned ", serializer.data),  
                    status=status.HTTP_200_OK
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


