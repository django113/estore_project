from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError

from cart.models import cartUserCartModel
from order.models import orderOrderModel

User = get_user_model()


# <editor-fold desc="ORDER IS CREATE BY USING USER CART SLUG">
class ordersClientUserOrderSerializer(serializers.Serializer):
    user_cart_slug = serializers.CharField(max_length=100, required=True)

    def validate(self, data):
        user_cart_slug = data.get('user_cart_slug')
        try:
            cart = cartUserCartModel.objects.get(slug=user_cart_slug)
        except:
            raise ValidationError({"error": "Something is Wrong", 'status': status.HTTP_400_BAD_REQUEST})

        existing_product = cart.cart_line.all()
        if not existing_product.exists():
            raise ValidationError(
                {"error": "Your Cart Is Empty", 'status': status.HTTP_400_BAD_REQUEST})
        return data



    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        user_cart = cartUserCartModel.objects.get(user__slug=user.slug)

        order_items = user_cart.cart_line.all()
        total_final_price = 0

        for item in order_items:
            total_final_price += (item.initial_price * item.quantity)

        orders = orderOrderModel.objects.create(user=user, price=total_final_price)

        orders.lines.set(order_items)
        orders.save()

        user_cart.cart_line.clear()
        user_cart.save()

        return validated_data


# </editor-fold>


# <editor-fold desc="ORDER IS CREATE BY USING AUTH USER">
class ordersClientUserOrderCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField()
    lines = serializers.ReadOnlyField()

    """
        Write Validation for User Cart is empty or not, before placing Order.
    
    """

    def validate(self, data):

        user = self.context['request'].user
        try:
            cart = cartUserCartModel.objects.get(user=user)
        except:
            raise ValidationError({"error": "Something is Wrong", 'status': status.HTTP_400_BAD_REQUEST})

        existing_product = cart.cart_line.all()
        if not existing_product.exists():
            raise ValidationError(
                {"error": "Your Cart Is Empty", 'status': status.HTTP_400_BAD_REQUEST})
        return data

    class Meta:
        model = orderOrderModel
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        user_cart = cartUserCartModel.objects.get(user=user)

        order_items = user_cart.cart_line.all()
        total_final_price = 0

        for item in order_items:
            total_final_price += (item.initial_price * item.quantity)

        orders = orderOrderModel.objects.create(user=user, price=total_final_price)

        orders.lines.set(order_items)
        orders.save()

        user_cart.cart_line.clear()
        user_cart.save()

        return validated_data

        # user = self.context['request'].user
        # user_cart = cartUserCartModel.objects.all().filter(user__slug=user.slug)
        #
        # if user_cart.exists():
        #     order = user_cart[0]
        #     order_items = order.cart_line.all()
        #     total_final_price = 0
        #
        #     for item in order_items:
        #         total_final_price += (item.initial_price * item.quantity)
        #
        #     orders = orderOrderModel.objects.create(user=user, price=total_final_price)
        #
        #     orders.lines.add(*list(order_items))
        #     orders.save()
        #
        # # user cart delete this item price is zero
        # if user_cart.exists():
        #     instance_user_cart = user_cart[0]
        #     items = instance_user_cart.cart_line.all()
        #     final_price = 0
        #     for item in items:
        #         instance_order = instance_user_cart.cart_line.remove(item)
        #         final_price += (item.initial_price * item.quantity)
        #
        # user_cart.update(price=0)
        #
        # return validated_data
# </editor-fold>
