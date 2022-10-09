from django.urls import path, include

urlpatterns = [

    # <editor-fold desc="CART LINE QUANTITY UPDATE BY USING CART LINE SLUG">
    path('api/client/v1/', include('cart.api_v1_client.urls')),
    # </editor-fold>

]
