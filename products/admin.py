from django.contrib import admin

# Register your models here.
from products.models import *


class productsAdminBrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'unique_code', 'title', 'description', 'date_created', ]


class productsAdminProductMainAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'brand', 'price', 'date_created', ]


admin.site.register(productsBrandModel,productsAdminBrandAdmin)
admin.site.register(productsProductMainModel,productsAdminProductMainAdmin)
