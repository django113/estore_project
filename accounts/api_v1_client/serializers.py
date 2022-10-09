from django.contrib.auth import get_user_model
from rest_framework import serializers

from cart.models import cartUserCartModel
from whishlist.models import whishlistUserWhishListModel

User = get_user_model()


# <editor-fold desc="USER CREATE ">
class accountsClientUserCreateSerializer(serializers.ModelSerializer):
    dob = serializers.DateField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('phone', 'password', 'email', 'dob', 'slug')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        instance_user = User.objects.filter(slug=user.slug).values_list('id', flat=True)
        user_cart = cartUserCartModel.objects.filter(user=user).values_list('user_id', flat=True)
        user_whish = whishlistUserWhishListModel.objects.filter(user=user).values_list('user_id', flat=True)
        # now List Comprehension to Compare Two Lists
        # user cart checking user is existing or not? based on user id?.
        user1 = list(instance_user)
        user2 = list(user_cart)
        instance_user_cart = [x for x in user1 + user2 if x not in user1 or x not in user2]
        if instance_user_cart:
            instance_user.delete()
            user_cart.delete()

        # whish list checking user is existing or not?based on user id?.
        user3 = list(user_whish)
        instance_user_whish = [x for x in user1 + user3 if x not in user1 or x not in user3]

        if instance_user_whish:
            instance_user.delete()
            user_whish.delete()

        return user
# </editor-fold>
