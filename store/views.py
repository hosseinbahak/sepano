from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics
from .serializers import *
from unidecode import unidecode
from rest_framework import status
from .models import *
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class ProductView(generics.GenericAPIView):
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
            
            
            
def response_func(status: bool ,msg: str, data: dict):
    return {
        'status': status,
        'message': msg,
        'data': data
    } 


