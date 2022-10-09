from django.contrib.auth import get_user_model
from django.db import models, transaction
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from cart.models import cartCartLineMainModel
from estore_core.utils import slug_pre_save_receiver

User = get_user_model()

"""
user = required
product =required
"""
# <editor-fold desc="WHISHLIST MODEL">
class whishlistUserWhishListModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="whishlistUserWhishListModel_user")
    product = models.ManyToManyField(cartCartLineMainModel, related_name="whishlistUserWhishListModel_product")
    price = models.FloatField(default=0)

    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        super(whishlistUserWhishListModel, self).save(*args, **kwargs)
        with transaction.atomic():
            transaction.on_commit(self.user_whishlist_product_price_update)

    def user_whishlist_product_price_update(self):
        total_final_price = 0
        for item in self.product.all():
            print(item.final_price)
            total_final_price += item.final_price
            print(item.status, 'user whish list---------status')
        self.price = total_final_price
        super(whishlistUserWhishListModel, self).save()

    def get_whishlist_products(self):
        return ",".join([str(p) for p in self.product.all()])


pre_save.connect(slug_pre_save_receiver, sender=whishlistUserWhishListModel)
# </editor-fold>


"""
siganls using for when user us created then whishlist user create.
"""

# <editor-fold desc="WHEN USER IS CREATED THEN WHISH LIST USER CREATEED BY INSTANCE USER">
@receiver(post_save, sender=User)
def user_post_save_receiver(sender, instance, created, *args, **kwargs):
    """
    after saved in the database
    """
    if created:
        # trigger pre_save
        if instance:
            # user whish list user create
            product_user_whish_list = whishlistUserWhishListModel.objects.create(user=instance)
            instance.save()
            # trigger post_save
# </editor-fold>
