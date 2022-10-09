from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, Sum
from rest_framework import serializers, status

from cart.models import cartCartLineMainModel
from products.models import productsProductMainModel
from whishlist.models import whishlistUserWhishListModel

User = get_user_model()


# <editor-fold desc="USER WHISH LIST CREATE AND ADDED OR REMOVE ITEMS PRODUCTS AND UPDATE PRICE IN BY USING PRODUCT SLUG">
class whishListClientUserWhishListSerializer(serializers.Serializer):
    product_slug = serializers.CharField(max_length=100, required=True, write_only=True)

    def validate(self, data):
        user = self.context['request'].user
        product_slug = data.get('product_slug')
        try:
            productsProductMainModel.objects.get(slug=product_slug)
        except Exception as e:
            raise serializers.ValidationError(
                {"error": "Product DoseNot Exist In Product", 'status': status.HTTP_400_BAD_REQUEST})
        return data

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        product_slug = validated_data['product_slug']
        product = productsProductMainModel.objects.get(slug=product_slug)

        try:
            user_wishlist = whishlistUserWhishListModel.objects.get(user=user)
        except:
            user_wishlist = whishlistUserWhishListModel.objects.create(user=user)

        try:
            cartLine = user_wishlist.product.get(product=product, user=user)
            user_wishlist.product.remove(cartLine)
            user_wishlist.save()
            return "Product removed from wishlist"

        except:
            try:
                cartLine = cartCartLineMainModel.objects.get(user=user, product=product, status='WhishList')
            except:
                cartLine = cartCartLineMainModel.objects.create(user=user, product=product, status='WhishList')
            user_wishlist.product.add(cartLine)
            user_wishlist.save()
            return "Product added to wishlist"


# </editor-fold>


# <editor-fold desc="USER WHISH LIST CREATE AND ADDED OR REMOVE ITEMS PRODUCTS AND UPDATE PRICE IN BY USING PRODUCT SLUG WITH AUTHENTICATED USER">
class whishlistClientAddToWhishListGenerateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField()
    product = serializers.ReadOnlyField()
    product_slug = serializers.CharField(max_length=100, required=True)

    # def validate(self, data):
    #     # user_slug = data.get('user_slug')
    #     user = self.context['request'].user
    #     product_slug = data.get('product_slug')
    #
    #     try:
    #         product = productsProductMainModel.objects.get(slug=product_slug)
    #     except Exception as e:
    #         raise serializers.ValidationError(
    #             {"error": "Product DoseNot Exist In Product", 'status': status.HTTP_400_BAD_REQUEST})
    #
    #     try:
    #         user_whish = whishlistUserWhishListModel.objects.get(user__slug=user.slug)
    #     except:
    #         return data
    #
    #     existing_product = user_whish.product.all()
    #     # existing_product = user_whish.product.filter(Q(product=product) & Q(user__slug=user.slug))
    #     if existing_product.exists():
    #         raise serializers.ValidationError(
    #             {"error": "Product Already added to whish", 'status': status.HTTP_400_BAD_REQUEST})
    #     return data

    class Meta:
        model = whishlistUserWhishListModel
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        # user = self.context.get("request").user
        product_slug = validated_data['product_slug']
        # print(user, product_slug)

        try:
            product = productsProductMainModel.objects.filter(slug=product_slug).last()
        except Exception as e:

            raise serializers.ValidationError("Not Available product")

        cartLine = cartCartLineMainModel.objects.filter(user=user, product=product, status='WhishList')

        if len(cartLine) == 0:
            cartLine_item = cartCartLineMainModel.objects.create(user=user, product=product, status='WhishList')
        elif len(cartLine) != 0:
            cartLine_item = cartLine.last()
            # print(cartLine_item)
        else:
            cartLine_item = cartLine.last()

        user_whish_list = whishlistUserWhishListModel.objects.filter(user=user).last()

        if user_whish_list == None:
            whish_list = whishlistUserWhishListModel.objects.create(user=user)
        else:
            whish_list = user_whish_list
        if cartLine_item in whish_list.product.all():

            whish_list.product.remove(cartLine_item)
            whish_list.save()

        else:
            whish_list.product.add(cartLine_item)
            whish_list.save()

        return validated_data
# </editor-fold>
