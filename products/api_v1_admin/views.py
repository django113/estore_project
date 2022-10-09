from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import generics, status, filters
# from django_filters import rest_framework as dj_filters


from django.contrib.auth import get_user_model

from products.api_v1_admin.serilaizers import productsAdminProductMainSerializer, \
    productsAdminProductMainCreateSerializer, productsAdminBrandSerializer
from products.models import productsProductMainModel, productsBrandModel

User = get_user_model()

"""
product brand model
"""
# <editor-fold desc="GET ALL PRODUCT BRANDS AND CREATE PRODUCT BRAND">
class productsAdminBrandCreateGenericsView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = productsAdminBrandSerializer
    queryset = productsBrandModel.objects.all()
    permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    # pagination_class = LimitOffsetPagination
    search_fields = ["title", ]
    filter_backends = (filters.SearchFilter,)

    def list(self, request, *args, **kwargs):
        # s_name_brand = productsBrandModel.objects.filter(title__startwith="s")
        serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True,
                                         context={"request": request})
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = productsAdminBrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# </editor-fold>


# <editor-fold desc="PRODUCT BRAND DETAILS">
class productsAdminBrandDetailsAPIView(APIView):
    serializer_class = productsAdminBrandSerializer
    # permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    pagination_class = None

    def get(self, request, slug):
        data = productsBrandModel.objects.get(slug=slug)
        serializer = productsAdminBrandSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        data = productsBrandModel.objects.get(slug=slug)
        serializer = productsAdminBrandSerializer(data=request.data, instance=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        data = productsBrandModel.objects.get(slug=slug)
        data.delete()
        return Response({"data": "Objects Deleted Successfully"}, status=status.HTTP_202_ACCEPTED)
# </editor-fold>


"""
productsProductMainModel

"""


# <editor-fold desc="GET ALL PRODUCTS AND CREATE PRODUCTS">
class productsAdminProductMainCreateGenericsView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = productsAdminProductMainSerializer
    queryset = productsProductMainModel.objects.all()
    permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    # pagination_class = LimitOffsetPagination
    search_fields = ["brand", ]
    filter_backends = (filters.SearchFilter,)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True,
                                         context={"request": request})
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = productsAdminProductMainCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# </editor-fold>


# <editor-fold desc="PRODUCT DETAILS BY USING PRODUCT SLUG">
class productsAdminProductMainDetailsAPIView(APIView):
    serializer_class = productsAdminProductMainSerializer
    # permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    pagination_class = None

    def get(self, request, slug):
        data = productsProductMainModel.objects.get(slug=slug)
        serializer = productsAdminProductMainSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        data = productsProductMainModel.objects.get(slug=slug)
        serializer = productsAdminProductMainSerializer(data=request.data, instance=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        data = productsProductMainModel.objects.get(slug=slug)
        data.delete()
        return Response({"data": "Objects Deleted Successfully"}, status=status.HTTP_202_ACCEPTED)
# </editor-fold>


