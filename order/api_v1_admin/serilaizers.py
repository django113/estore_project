from rest_framework import serializers, status

from order.models import orderOrderModel


# <editor-fold desc="ORDER STATUS UPDATE BY USING ORDER SLUG">
class ordersAdminUserOrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = orderOrderModel
        fields = ['status']


# </editor-fold>


# <editor-fold desc="GET ALL ORDERS  ">
class ordersAdminUserOrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = orderOrderModel
        fields = '__all__'
# </editor-fold>
