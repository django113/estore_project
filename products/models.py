from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save

from estore_core.utils import slug_pre_save_receiver
from products.signals import brand_unique_code_generator

User = get_user_model()

"""

unique_code = required

title = required

date_created = required

slug = required

"""

# Create your models here.
# <editor-fold desc="PRODUCT BRAND MODEL">
class productsBrandModel(models.Model):
    unique_code = models.CharField(max_length=250, null=True, unique=True, blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


pre_save.connect(slug_pre_save_receiver, sender=productsBrandModel)
pre_save.connect(brand_unique_code_generator, sender=productsBrandModel)
# </editor-fold>

"""
name    = required
brand   = required
price   = required
date_created    = required
slug    = required
"""

# <editor-fold desc="PRODUCT MAIN MODEL">
class productsProductMainModel(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(productsBrandModel, on_delete=models.CASCADE,
                              related_name='productsProductMainModel_brand')
    price = models.FloatField()

    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    def __str__(self):
        return self.name

    def get_productbrand(self, obj):
        try:
            brand = obj.brand.title
        except:
            brand = ""
        return brand


pre_save.connect(slug_pre_save_receiver, sender=productsProductMainModel)
# </editor-fold>
