from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status, filters
from cart.api_v1_client.serilaizers import cartClientProductQuantityUpdateSerializer, cartClientAddToCartSerializer, \
    cartClientAddtoCartSerializer
from cart.models import cartCartLineMainModel


# <editor-fold desc="CART LINE MAIN MODEL QUANTITY UPDATE BY USING CART LINE MAIN MODEL SLUG">

class cartClientProductCartDetailsAPIView(APIView):
    serializer_class = cartClientProductQuantityUpdateSerializer
    permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    pagination_class = None

    def get(self, request, slug):
        data = cartCartLineMainModel.objects.get(slug=slug)
        serializer = cartClientProductQuantityUpdateSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        data = cartCartLineMainModel.objects.get(slug=slug)
        serializer = cartClientProductQuantityUpdateSerializer(data=request.data, instance=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Quantity is Updated sSuccessfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# </editor-fold>


# <editor-fold desc="ADD TO CART BY USING PRODUCT SLUG WITHOUT AUTHENTICATION">
class cartClientAddToCartGenericsView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    authenticate_class = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

    def post(self, request):
        serializer = cartClientAddToCartSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# </editor-fold>

# <editor-fold desc="PRODUCT TO CART BY USING PRODUCT SLUG WITH AUTHENTICATION USER">
class cartClientProductToCartGenericsView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    authenticate_class = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

    def post(self, request):
        serializer = cartClientAddtoCartSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Product To Cart is Successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# </editor-fold>
