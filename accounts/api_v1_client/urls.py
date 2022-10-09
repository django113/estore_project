from django.urls import path

from .views import accountsClientUserCreateGenericsView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # <editor-fold desc="user register">
    path('user-create/', accountsClientUserCreateGenericsView.as_view(), name='accountsClientUserCreateGenericsViewURL'),
    # </editor-fold>

    # ACCOUNTS
    # <editor-fold desc="User LOGIN">
    path('login/api/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # </editor-fold>

    # <editor-fold desc="USER GET ACCESS AND REFRESH TOKEN BY USING PREVIOUS LOGIN TO REFRESH TOKEN">
    path('login/api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # </editor-fold>


]
