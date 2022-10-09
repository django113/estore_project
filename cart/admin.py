from django.contrib import admin

# Register your models here.
from cart.models import cartUserCartModel, cartCartLineMainModel


class cartAdminCartLineMainAdmin(admin.ModelAdmin):
    list_display = ['user','slug', 'product', 'quantity', 'initial_price', 'final_price', 'status', 'date_created', ]

    # # # list of items display only logged user records display
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     if request.user.is_admin:
    #         return qs
    #     return qs.filter(user=request.user)

    # specific user only visible or login user only except superuser
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "user":
    #         # print(User.objects.filter(email=request.user), 'user id--------------admin')
    #         kwargs["queryset"] = User.objects.filter(email=request.user)
    #     # if request.user.is_superuser:
    #     #     qs = super().get_queryset(request)
    #     #     return qs
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)


class cartAdminUserCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'slug', 'price', 'get_products']

    # # # list of items display only logged user records display
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     if request.user.is_admin:
    #         return qs
    #     return qs.filter(user=request.user)

    # specific user only visible or login user only except superuser
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "user":
    #         # print(User.objects.filter(email=request.user), 'user id--------------admin')
    #         kwargs["queryset"] = User.objects.filter(email=request.user)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # show records for respective user only
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        try:
            object_id = request.resolver_match.kwargs['object_id']
            instance = cartUserCartModel.objects.get(id=object_id)
            if db_field.name == "cart_line":
                kwargs["queryset"] = cartCartLineMainModel.objects.filter(user__id=instance.user.id, status="Cart")
            return super(cartAdminUserCartAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
        except Exception as e:
            kwargs["queryset"] = cartCartLineMainModel.objects.filter(user=request.POST.get('user'))
            return super(cartAdminUserCartAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(cartCartLineMainModel, cartAdminCartLineMainAdmin)
admin.site.register(cartUserCartModel, cartAdminUserCartAdmin)
