from django.urls import path

from order.api_v1_client.views import orderClientUserOrderCreateGenericsView, orderClientOrderCreateGenericsView

urlpatterns = [
    # <editor-fold desc="ORDER CREATE BY PASSING USER CART SLUG">
    path('order-create/', orderClientUserOrderCreateGenericsView.as_view(),
         name='orderClientUserOrderCreateGenericsViewURL'),
    # </editor-fold>

    # <editor-fold desc="ORDER CREATE BY AUTHENTICATION USER">
    path('product-order-create/', orderClientOrderCreateGenericsView.as_view(),
         name='orderClientOrderCreateGenericsViewURL'),
    # </editor-fold>

]
