from django.urls import path, include

urlpatterns = [

    # <editor-fold desc="ADD TO WHISH LIST ADD OR REMOVE PRODUCT BY USING PRODUCT SLUG">
    path('api/client/v1/', include('whishlist.api_v1_client.urls')),
    # </editor-fold>

]
