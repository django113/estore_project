from django.contrib.auth import get_user_model

from rest_framework import serializers, status

from products.models import productsProductMainModel, productsBrandModel

User = get_user_model()


# <editor-fold desc="PRODUCT BRAND ">
class productsAdminBrandSerializer(serializers.ModelSerializer):

    def validate(self, data):
        title = data.get("title", None)
        brand = productsBrandModel.objects.filter(title__iexact=title)
        if brand.exists():
            raise serializers.ValidationError(
                {"errors": "This brand already exists", 'status': status.HTTP_400_BAD_REQUEST})
        else:
            return data

    class Meta:
        model = productsBrandModel
        fields = "__all__"


# </editor-fold>


# <editor-fold desc="PRODUCT MAIN MODEL">
class productsAdminProductMainCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = productsProductMainModel
        fields = "__all__"


# </editor-fold>


# <editor-fold desc="GET ALL PRODUCTS">
class productsAdminProductMainSerializer(serializers.ModelSerializer):
    brand = serializers.SerializerMethodField()

    def get_brand(self, obj):
        brand = obj.get_productbrand(obj)
        return brand

    class Meta:
        model = productsProductMainModel
        fields = ['name', 'brand', 'price', 'date_created', 'slug']

# </editor-fold>
