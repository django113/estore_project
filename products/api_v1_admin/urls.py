from django.urls import path

from products.api_v1_admin.views import productsAdminBrandCreateGenericsView, productsAdminBrandDetailsAPIView, productsAdminProductMainCreateGenericsView, \
    productsAdminProductMainDetailsAPIView

urlpatterns = [

    # <editor-fold desc="PRODUCT BRAND CREATE">
    path('brand-create/', productsAdminBrandCreateGenericsView.as_view(),
         name='productsAdminBrandCreateGenericsViewURL'),
    # </editor-fold>

    # <editor-fold desc="PRODUCT BRAND DETAILS BY USING BRAND SLUG">
    path('brand-details/<slug>/', productsAdminBrandDetailsAPIView.as_view(),
         name='productsAdminBrandDetailsAPIViewURL'),
    # </editor-fold>


    # <editor-fold desc="PRODUCT CREATE">
    path('product-create/', productsAdminProductMainCreateGenericsView.as_view(),
         name='productsAdminProductMainCreateGenericsViewURL'),
    # </editor-fold>

    # <editor-fold desc="PRODUCT DETAILS BY USING PRODUCT SLUG">
    path('product-details/<slug>/', productsAdminProductMainDetailsAPIView.as_view(),
         name='productsAdminProductMainDetailsAPIViewURL'),
    # </editor-fold>


]
