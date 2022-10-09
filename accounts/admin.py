from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ['id', 'slug', 'email', 'phone', 'dob', ]

    def save_model(self, request, obj, form, change):
        obj.set_password(obj.password)
        obj.save()
        super(User, self).save_model(request, obj, form, change)
