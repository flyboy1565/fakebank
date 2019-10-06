from django.contrib import admin

from .models import *

# admin.site.register(Transaction)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = [
        'transaction_id', 'account_id', 'transaction_timestamp', 'type', 
        'previous_balance', 'amount', 'current_balance'
    ]

    def account_id(self, obj):
        return '*********{}'.format(obj.account.account_id)

@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = [
        'transfer_id', 'get_from_account', 'get_to_account', 'amount'
    ]

    def get_from_account(self, obj):
        return '*********{}'.format(obj.from_account.account_id)

    get_from_account.short_description = 'From Account'

    def get_to_account(self, obj):
        return '*********{}'.format(obj.to_account.account_id)

    get_to_account.short_description = 'To Account'