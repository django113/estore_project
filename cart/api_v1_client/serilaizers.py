from django.db.models import Q
from rest_framework import serializers, status

from cart.models import cartCartLineMainModel, cartUserCartModel
from products.models import productsProductMainModel


# <editor-fold desc="CARTLINE MAIN MODEL UPDATE QUANTITY BY USING CART LINE MAIN MODEL SLUG">
class cartClientProductQuantityUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = cartCartLineMainModel
        # fields = "__all__"
        fields = ('quantity',)


# </editor-fold>


# <editor-fold desc=" ADD TO CART BY USING PRODUCT SLUG">
class cartClientAddToCartSerializer(serializers.Serializer):
    # user_slug = serializers.CharField(max_length=100, required=True)
    product_slug = serializers.CharField(max_length=100, required=True)

    def validate(self, data):
        # user_slug = data.get('user_slug')
        user = self.context['request'].user
        product_slug = data.get('product_slug')

        try:
            product = productsProductMainModel.objects.get(slug=product_slug)
        except Exception as e:
            raise serializers.ValidationError({"error": "Product DoseNot Exist In Product", 'status': status.HTTP_400_BAD_REQUEST})

        try:
            user_cart = cartUserCartModel.objects.get(user__slug=user.slug)
        except:
            return data

        existing_product = user_cart.cart_line.filter(Q(product=product) & Q(user__slug=user.slug))
        if existing_product.exists():
            raise serializers.ValidationError(
                {"error": "Product Already added to cart", 'status': status.HTTP_400_BAD_REQUEST})
        return data

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        # user_slug = validated_data['user_slug']
        user = self.context['request'].user
        product_slug = validated_data['product_slug']
        product = productsProductMainModel.objects.get(slug=product_slug)

        try:
            user_cart = cartUserCartModel.objects.get(user=user)
        except:
            user_cart = cartUserCartModel.objects.create(user=user)

        try:
            cart_Line = cartCartLineMainModel.objects.get(user=user, product=product)
        except:
            cart_Line = cartCartLineMainModel.objects.create(user=user, product=product)

        user_cart.cart_line.add(cart_Line)
        cart_Line.status='Cart'
        cart_Line.save()
        user_cart.save()
        return validated_data


# </editor-fold>

# <editor-fold desc="PRODUCT TO CART BY USING PRODUCT SLUG AND UPDATE CART LINE MAIN MODEL STATUS IS CART">
class cartClientAddtoCartSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField()
    product_slug = serializers.CharField(max_length=100, required=True)

    def validate(self, data):
        # user_slug = data.get('user_slug')
        user = self.context['request'].user
        product_slug = data.get('product_slug')

        try:
            product = productsProductMainModel.objects.get(slug=product_slug)
        except Exception as e:
            raise serializers.ValidationError({"error": "Product DoseNot Exist In Product", 'status': status.HTTP_400_BAD_REQUEST})

        try:
            user_cart = cartUserCartModel.objects.get(user__slug=user.slug)
        except:
            return data

        existing_product = user_cart.cart_line.filter(Q(product=product) & Q(user__slug=user.slug))
        if existing_product.exists():
            raise serializers.ValidationError(
                {"error": "Product Already added to cart", 'status': status.HTTP_400_BAD_REQUEST})
        return data

    class Meta:
        model = cartUserCartModel
        fields = "__all__"

    def create(self, validated_data):
        # user_slug = validated_data['user_slug']
        user = self.context['request'].user
        product_slug = validated_data['product_slug']
        product = productsProductMainModel.objects.get(slug=product_slug)

        try:
            user_cart = cartUserCartModel.objects.get(user=user)
        except:
            user_cart = cartUserCartModel.objects.create(user=user)

        # try:
        #     cart_Line = cartCartLineMainModel.objects.get(user=user, product=product)
        # except:
        cart_Line = cartCartLineMainModel.objects.create(user=user, product=product)

        user_cart.cart_line.add(cart_Line)
        cart_Line.status='Cart'
        cart_Line.save()
        user_cart.save()
        return validated_data

# </editor-fold>







































# # <editor-fold desc="PRODUCT TO CART BY USING PRODUCT SLUG AND UPDATE CART LINE MAIN MODEL STATUS IS CART">
# class cartClientAddtoCartSerializer(serializers.ModelSerializer):
#     user = serializers.ReadOnlyField()
#     product_slug = serializers.CharField(max_length=100, required=True)
#
#     def validate(self, data):
#         user = self.context['request'].user
#         product_slug = data.get('product_slug')
#
#         try:
#             product = productsProductMainModel.objects.get(slug=product_slug)
#         except Exception as e:
#             raise serializers.ValidationError("Not Available product")
#         try:
#             user_cart = cartUserCartModel.objects.get(user__slug=user.slug)
#         except:
#             return data
#         existing_product = user_cart.cart_line.filter(Q(product=product) & Q(user__slug=user.slug))
#         if existing_product.exists():
#             raise serializers.ValidationError(
#                 {"error": "Product Already added to cart", 'status': status.HTTP_400_BAD_REQUEST})
#         return data
#
#     class Meta:
#         model = cartUserCartModel
#         fields = "__all__"
#
#     def create(self, validated_data):
#
#         user_main = self.context['request'].user
#         product_slug = validated_data['product_slug']
#
#         # print(user_main)
#         # print(product_slug)
#
#         product = productsProductMainModel.objects.get(slug=product_slug)
#
#         user_cart = cartUserCartModel.objects.filter(user=user_main).last()
#
#         if user_cart == None:
#             cart_main = cartUserCartModel.objects.create(user=user_main)
#         else:
#             cart_main = user_cart
#
#         product_user = cartCartLineMainModel.objects.filter(user=user_main, product=product)
#
#         if len(product_user) == 0:
#             product_cart = cartCartLineMainModel.objects.create(user=user_main, product=product)
#         elif len(product_user) != 0:
#             product_cart = product_user.last()
#             # print(product_cart)
#         else:
#             product_cart = product_user.last()
#
#         cart_main.cart_line.add(product_cart)
#         product_user.update(status='Cart')
#         # cart_main.price = user_cart.cart_line.all().aggregate(Sum('final_price')).get('final_price__sum')
#         # cart_main.price = user_cart.price
#         cart_main.save()
#         return validated_data
#
# # </editor-fold>
