from django.db import models, transaction
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save

from cart.models import cartCartLineMainModel
from estore_core.utils import slug_pre_save_receiver
from order.signals import order_code_unique_code_generator
from order.uitls import orderStatusEnumTypes

User = get_user_model()
from django.utils.translation import gettext_lazy as _

"""
user = required
lines = required
status = required
date_created = required
slug = required
"""


# Create your models here.
# <editor-fold desc="ORDER MODEL">

class orderOrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orderOrderModel_user')
    order_code = models.CharField(_('Order ID'), max_length=13, unique=True, null=True, blank=True)
    lines = models.ManyToManyField(cartCartLineMainModel, related_name="orderOrderModel_lines")
    price = models.FloatField(default=0)
    status = models.CharField(max_length=16, choices=orderStatusEnumTypes.choices(), default="pending")
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    def __str__(self):
        return str(self.user)


pre_save.connect(slug_pre_save_receiver, sender=orderOrderModel)
pre_save.connect(order_code_unique_code_generator, sender=orderOrderModel)
# </editor-fold>
