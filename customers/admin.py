from django.contrib import admin

from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'city', 'state', 'zip_code', 'phone_number', 'email', 'number_of_accounts']

    def number_of_accounts(self, obj):
        return obj.account_set.select_related().count()

    def fullname(self, obj):
        return obj.fullname

