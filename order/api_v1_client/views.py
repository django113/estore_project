from django.contrib.auth import get_user_model
from rest_framework import status, generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from order.api_v1_client.serializers import ordersClientUserOrderSerializer, ordersClientUserOrderCreateSerializer

User = get_user_model()


# <editor-fold desc="CREATE ORDER BY USING USER CART SLUG">
class orderClientUserOrderCreateGenericsView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    authenticate_class = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    def post(self, request):
        serializer = ordersClientUserOrderSerializer(data=request.data,context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Your Order is Successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# </editor-fold>


# <editor-fold desc="CREATE ORDER BY USING AUTHENTICATED">
class orderClientOrderCreateGenericsView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    def post(self, request):
        serializer = ordersClientUserOrderCreateSerializer(data=request.data,context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Your Order is Successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# </editor-fold>
