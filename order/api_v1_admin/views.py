
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import generics, status, filters
# from django_filters import rest_framework as dj_filters


from django.contrib.auth import get_user_model

from order.api_v1_admin.serilaizers import ordersAdminUserOrderUpdateSerializer, \
    ordersAdminUserOrderDetailsSerializer
from order.models import orderOrderModel

User = get_user_model()


# <editor-fold desc="GET ALL ORDER LIST  AND  CREATE ORDER">
class orderAdminUserOrderCreateGenericsView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = ordersAdminUserOrderDetailsSerializer
    permission_classes = (IsAuthenticated,)
    queryset = orderOrderModel.objects.all()
    authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    # pagination_class = LimitOffsetPagination
    search_fields = ["user", ]
    filter_backends = (filters.SearchFilter,)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True,
                                         context={"request": request})
        return self.get_paginated_response(serializer.data)
    def post(self, request):
        serializer = ordersAdminUserOrderDetailsSerializer(data=request.data,context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# </editor-fold>


# <editor-fold desc="ORDER STATUS BY USING ORDER SLUG AND DELETE ">
class orderAdminAdminUserOrderUpdateDetailsAPIView(APIView):
    serializer_class = ordersAdminUserOrderUpdateSerializer
    permission_classes = (IsAuthenticated,)
    authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    pagination_class = None

    def get(self, request, slug):
        data = orderOrderModel.objects.get(slug=slug)
        serializer = ordersAdminUserOrderUpdateSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        data = orderOrderModel.objects.get(slug=slug)
        serializer = ordersAdminUserOrderUpdateSerializer(data=request.data, instance=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        data = orderOrderModel.objects.get(slug=slug)
        data.delete()
        return Response({"data": "Objects Deleted Successfully"}, status=status.HTTP_202_ACCEPTED)
# </editor-fold>