from django.contrib import admin

# Register your models here.
from cart.models import cartCartLineMainModel
from whishlist.models import whishlistUserWhishListModel


class whsishlistAdminUserWhishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'slug', 'get_whishlist_products', 'price', 'date_created', ]

    # # list of items display only logged user records display
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=request.user)

    # specific user only visible or login user only except superuser
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "user":
    #         # print(User.objects.filter(email=request.user), 'user id--------------admin')
    #         kwargs["queryset"] = User.objects.filter(email=request.user)
    #     # if request.user.is_superuser:
    #
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # show records for respective user only
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        try:
            object_id = request.resolver_match.kwargs['object_id']
            instance = whishlistUserWhishListModel.objects.get(id=object_id)
            if db_field.name == "product":
                kwargs["queryset"] = cartCartLineMainModel.objects.filter(user__id=instance.user.id, status="WhishList")
            return super(whsishlistAdminUserWhishlistAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
        except Exception as e:
            kwargs["queryset"] = cartCartLineMainModel.objects.filter(user=request.POST.get('user'))
            return super(whsishlistAdminUserWhishlistAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(whishlistUserWhishListModel, whsishlistAdminUserWhishlistAdmin)
