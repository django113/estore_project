from django.urls import path, include

urlpatterns = [

    # <editor-fold desc="user register">
    path('api/client/v1/', include('accounts.api_v1_client.urls')),
    # </editor-fold>

]
