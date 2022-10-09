from django.db import models, transaction
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save, post_delete, pre_delete, post_save
from django.dispatch import receiver

from cart.uitls import cartStatusEnumTypes
from estore_core.utils import slug_pre_save_receiver
from products.models import productsProductMainModel

User = get_user_model()

"""
signals pre save ,post save, pre delete,post delete using cart line model
"""
# <editor-fold desc="CART LINE MAIN MODEL PRODUCT UPDATED AND CART USER CART ALSO UPDATE AND WHEN DELETED CART LINE MODEL THEN UPDATE CART USER MODEL TRIGGERED">
def cart_pre_save_receiver(sender, instance, *args, **kwargs):
    """
    before saved in the database
    """
    if instance:
        instance.initial_price = instance.product.price
        instance.final_price = round(instance.initial_price * instance.quantity)
        try:
            instance.user.cartUserCartModel_user.save()
        except Exception as e:
            pass


def cart_post_save_receiver(sender, instance, created, *args, **kwargs):
    """
    after saved in the database
    """

    if created:
        instance.initial_price = instance.product.price
        instance.final_price = round(instance.initial_price * instance.quantity)
        instance.save()

    if instance:
        instance.initial_price = instance.product.price
        instance.final_price = round(instance.initial_price * instance.quantity)
        try:
            instance.user.cartUserCartModel_user.save()
        except Exception as e:
            pass


# pre delete
def productcart_pre_delete(sender, instance, *args, **kwargs):
    if instance:
        #   product user cart model price update
        product_price = cartCartLineMainModel.objects.all().filter(user_id=instance.user).values_list('final_price',
                                                                                                      flat=True)
        price = sum(product_price)
    if instance.user != None:
        cartUserCartModel.objects.filter(user=instance.user).update(price=price)


# post delete

def productcart_post_delete(sender, instance, *args, **kwargs):
    #   product user cart model price update
    product_price = cartCartLineMainModel.objects.all().filter(user_id=instance.user).values_list('final_price',
                                                                                                  flat=True)

    price = sum(product_price)
    if instance.user != None:
        cartUserCartModel.objects.filter(user=instance.user).update(price=price)


# </editor-fold>


"""
product = required
quantity =required
initalprice = required
finalprice = required
date_created = required
slug = required

"""


# <editor-fold desc="CART LINE MAIN MODEL">
class cartCartLineMainModel(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cartCartLineMainModel_user')
    product = models.ForeignKey(productsProductMainModel, on_delete=models.CASCADE,
                                related_name='cartCartLineMainModel_product')
    quantity = models.IntegerField(default=1)
    initial_price = models.FloatField(null=True, blank=True)  # initial price is product price
    final_price = models.FloatField(null=True, blank=True)  # quantity * initial price

    status = models.CharField(
        max_length=10,
        choices=cartStatusEnumTypes.choices()
    )

    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    def __str__(self):
        return str(self.product)

    # user whish list using purpose
    def save(self, *args, **kwargs):
        self.initial_price = self.product.price
        self.final_price = self.product.price * self.quantity
        super(cartCartLineMainModel, self).save(*args, **kwargs)
        try:
            self.user.whishlistUserWhishListModel_user.save()
        except Exception as e:
            pass

        try:
            self.user.orderOrderModel_lines.save()
        except Exception as e:
            pass


pre_save.connect(slug_pre_save_receiver, sender=cartCartLineMainModel)
# pre save using
pre_save.connect(cart_pre_save_receiver, sender=cartCartLineMainModel)
# post save using
post_save.connect(cart_post_save_receiver, sender=cartCartLineMainModel)

pre_delete.connect(productcart_pre_delete, sender=cartCartLineMainModel)
post_delete.connect(productcart_post_delete, sender=cartCartLineMainModel)


# </editor-fold>

"""
user = required
cart_line = required
date_created = required
slug = required
"""

# <editor-fold desc="USER CART MODEL">
class cartUserCartModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cartUserCartModel_user')
    cart_line = models.ManyToManyField(cartCartLineMainModel, blank=True, related_name='cartUserCartModel_cart_line')
    price = models.FloatField(default=0)

    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    def __str__(self):
        # return str(self.cart_line)
        return str(self.user) + " (" + str(self.id) + ")"

    def save(self, *args, **kwargs):
        super(cartUserCartModel, self).save(*args, **kwargs)
        with transaction.atomic():
            transaction.on_commit(self.price_update)

    def price_update(self):
        total_final_price = 0
        for item in self.cart_line.all():
            total_final_price += item.final_price
        self.price = total_final_price
        super(cartUserCartModel, self).save()

    def get_products(self):
        return ",".join([str(p) for p in self.cart_line.all()])


pre_save.connect(slug_pre_save_receiver, sender=cartUserCartModel)


# </editor-fold>


"""
siganls using for when user us created then user cart user create.
"""
# <editor-fold desc="WHEN USER CREATE THEN USER CART MODEL CREATE WITH INSTANCE USER">
@receiver(post_save, sender=User)
def user_post_save_receiver(sender, instance, created, *args, **kwargs):
    """
    after saved in the database
    """
    if created:
        # trigger pre_save
        if instance:
            # product user create
            product_user_cart = cartUserCartModel.objects.create(user=instance)
            instance.save()
        # trigger post_save
# </editor-fold>
