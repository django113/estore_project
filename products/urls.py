from django.urls import path, include

urlpatterns = [

    # <editor-fold desc="PRODUCT BRAND AND PRODUCTS CREATE  ">
    path('api/admin/v1/', include('products.api_v1_admin.urls')),
    # </editor-fold>

]
