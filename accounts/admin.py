from django.contrib import admin

from .models import Account

# admin.site.register(Account)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'account_type', 'type', 'account_id', 'balance']
