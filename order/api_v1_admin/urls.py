from django.urls import path

from order.api_v1_admin.views import orderAdminUserOrderCreateGenericsView, orderAdminAdminUserOrderUpdateDetailsAPIView

urlpatterns = [
    # <editor-fold desc="ORDER CREATE AND GET ALL ORDERS LIST">
    path('order-create/', orderAdminUserOrderCreateGenericsView.as_view(),
         name='orderAdminUserOrderCreateGenericsViewURL'),
    # </editor-fold>

    # <editor-fold desc="ORDER STATUS CAHNGE BY USING ORDER SLUG">
    path('order-status-update-details/<slug>/', orderAdminAdminUserOrderUpdateDetailsAPIView.as_view(),
         name='orderAdminAdminUserOrderUpdateDetailsAPIViewURL'),
    # </editor-fold>
]
