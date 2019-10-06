from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model

from accounts.models import Account
from customers.models import Customer

def index(request):
    user = Customer.objects.first()
    accounts = Account.objects.filter(user=user)
    context = {'user': user, 'accounts': accounts}
    # context = None
    return render(request, 'base.html', context)
    # return HttpResponse("Test")