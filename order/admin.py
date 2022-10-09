from django.contrib import admin

# Register your models here.
from cart.models import cartCartLineMainModel
from order.models import orderOrderModel


class orderAdminOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'price', 'date_created', 'slug']

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        try:
            object_id = request.resolver_match.kwargs['object_id']
            instance = orderOrderModel.objects.get(id=object_id)
            if db_field.name == "lines":
                kwargs["queryset"] = cartCartLineMainModel.objects.filter(user__id=instance.user.id, status="Cart")
            return super(orderAdminOrderAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
        except Exception as e:
            kwargs["queryset"] = cartCartLineMainModel.objects.filter(user=request.POST.get('user'))
            return super(orderAdminOrderAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(orderOrderModel, orderAdminOrderAdmin)
