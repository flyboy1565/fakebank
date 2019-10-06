import datetime
from uuid import uuid4

from django.db import models
from decimal import Decimal
from django.utils import timezone
from djmoney.models.fields import MoneyField, Money

from customers.models import Customer
from accounts.models import Account

W = "Withdrawal"
D = "Deposit"
T = "Account Transfer"
P = "Purchase"
O = "Overdraft"

def TransactionChoices():
    return ( (W, W), (D, D) )

def AccountChoices():
    return (
        ("Savings", "Savings"),
        ("Checking", "Checking"),
        ("Credit", "Credit"),
        ("Personal Loan", "Personal Loan"),
        ("Car Loan", "Car Loan"),
        ("Mortage Loan", "Mortage Loan"),
    )


class Transaction(models.Model):
    previous_balance = MoneyField(max_digits=20,decimal_places=2, editable=False, default=0, default_currency='USD')
    current_balance = MoneyField(max_digits=20,decimal_places=2, editable=False, default=0, default_currency='USD')
    transaction_timestamp = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = MoneyField(max_digits=20,decimal_places=2, default=0, default_currency='USD')
    transaction_id = models.CharField(max_length=100, editable=False, unique=True, default=uuid4)
    type = models.CharField(max_length=50,choices=TransactionChoices())
    notes = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.transaction_id)

    def get_transaction_id(self):
        trans=str(self.user.username)+'_'+str(self.pk)
        return trans
    
    def save(self, *args, **kwargs):
        account = Account.objects.get(pk=self.account.pk)
        self.previous_balance = self.account.balance
        if self.type == W:
            account.balance -= self.amount
        elif self.type == D:
            account.balance += self.amount
        account.save()
        self.current_balance = account.balance
        super(Transaction, self).save(*args, **kwargs)
    
        
class Transfer(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    from_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="transfer_from")
    to_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="transfer_to")
    transfer_id = models.CharField(max_length=100, editable=False, unique=True, default=uuid4)
    amount = MoneyField(max_digits=20,decimal_places=2, default=0, default_currency='USD')
    
    def __str__(self):
        return "{}".format(self.transfer_id)
               
    def save(self, *args, **kwargs):
        fromAccount = Transaction()
        fromAccount.user = self.user
        fromAccount.account = self.from_account
        fromAccount.type = W
        fromAccount.amount = self.amount
        fromAccount.notes = "Transfer to Account: {}".format(self.to_account.account_id)
        fromAccount.save()
        toAccount = Transaction()
        toAccount.user = self.user
        toAccount.account = self.to_account
        toAccount.amount = self.amount
        toAccount.type = D
        toAccount.notes = "Transfer from Account: {}".format(self.from_account.account_id)
        toAccount.save()
        super(Transfer, self).save(*args, **kwargs)
    