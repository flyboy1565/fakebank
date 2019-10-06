from django.db import models

import datetime
from uuid import uuid4

from django.db import models
from decimal import Decimal
from django.utils import timezone
from djmoney.models.fields import MoneyField, Money

from customers.models import Customer

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

class Account(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    account_type = models.CharField(choices=AccountChoices(), max_length=50)
    type = models.CharField(choices=(('P', 'Personal'), ('L', 'Loans'), ('C', 'Credit')), max_length=5)
    account_id = models.PositiveIntegerField()
    balance = MoneyField(max_digits=20,decimal_places=2, editable=False, default=0, default_currency='USD')
    
    def __str__(self):
        return "{} - {} - {} - ({})".format(
            self.user.fullname,
            self.account_type,
            self.account_id,
            self.balance
        )
        
    @property
    def payment_amount(self):
        if self.balance.amount > -100 * 1.0:
            return self.balance
        return Money(self.balance.amount * Decimal(-.26), 'USD')
    
    @property
    def last_statement(self):
        if self.balance.amount > -100:
            return self.balance
        return self.balance + Money(self.balance.amount * Decimal(.025), 'USD')
        