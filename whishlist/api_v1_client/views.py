from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from whishlist.api_v1_client.serializers import whishListClientUserWhishListSerializer, \
    whishlistClientAddToWhishListGenerateSerializer

User = get_user_model()


# <editor-fold desc="Add To WHISH LIST CREATE AND ADDED OR REMOVE ITEMS PRODUCTS AND UPDATE PRICE IN BY USING PRODUCT SLUG">
class whishListClientUserWhishListCreateGenericsView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    authenticate_class = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

    def post(self, request):
        serializer = whishListClientUserWhishListSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            data = serializer.save()
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# </editor-fold>


# <editor-fold desc="Add To WHISH LIST AND UPDATE PRICE IN BY USING PRODUCT SLUG WITH AUTHENTICATION USER">
class whishListClientAddToWhishListCreateGenericsView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    authenticate_class = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

    def post(self, request):
        serializer = whishlistClientAddToWhishListGenerateSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Product To WishList Successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# </editor-fold>
