from django.urls import path, include

urlpatterns = [

    # <editor-fold desc="ORDER CREATE AND DETAILS ">
    path('api/admin/v1/', include('order.api_v1_admin.urls')),
    # </editor-fold>
    # <editor-fold desc="ORDER CREATE AND DETAILS ">
    path('api/client/v1/', include('order.api_v1_client.urls')),
    # </editor-fold>

]
