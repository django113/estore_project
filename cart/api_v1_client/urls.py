from django.urls import path

from cart.api_v1_client.views import cartClientProductCartDetailsAPIView, cartClientAddToCartGenericsView, \
    cartClientProductToCartGenericsView

urlpatterns = [


    # <editor-fold desc="CARTLINE MAIN MODEL QUANTITY INCREASES AND DECREASES BY USING CARTLINE MAIN MODEL SLUG">
    path('cart-line-quantity-update/<slug>/', cartClientProductCartDetailsAPIView.as_view(),
         name='cartClientProductCartDetailsAPIViewURL'),
    # </editor-fold>

    # <editor-fold desc="ADD TO CART BY USING PRODUCT SLUG WITH REQUEST USER">
    path('add-to-cart/', cartClientAddToCartGenericsView.as_view(),
         name='cartClientAddToCartGenericsViewURL'),
    # </editor-fold>


    # <editor-fold desc="ADD TO CART BY USING AUTHENTICATION USER">
    path('product-to-cart/', cartClientProductToCartGenericsView.as_view(),
         name='cartClientProductToCartGenericsViewURL'),
    # </editor-fold>

]
