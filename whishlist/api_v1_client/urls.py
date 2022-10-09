from django.urls import path

from whishlist.api_v1_client.views import whishListClientUserWhishListCreateGenericsView, \
    whishListClientAddToWhishListCreateGenericsView

urlpatterns = [
    # <editor-fold desc="ADD TO  WHISH LIST ADD OR REMOVE PRODUCT BY USING PRODUCT SLUG WITH REQUEST USER">
    path('add-to-whishlist/', whishListClientUserWhishListCreateGenericsView.as_view(),
         name='whishListClientUserWhishListCreateGenericsViewURL'),
    # </editor-fold>

    # <editor-fold desc="ADD TO  WHISH LIST BY USING PRODUCT SLUG WITH AUTHENTICATION USER">
    path('added-to-whishlist/', whishListClientAddToWhishListCreateGenericsView.as_view(),
         name='whishListClientAddToWhishListCreateGenericsViewURL'),
    # </editor-fold>
]
