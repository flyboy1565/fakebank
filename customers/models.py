from django.db import models
from localflavor.us.models import USStateField, USPostalCodeField
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = USStateField()
    zip_code = models.CharField(max_length=5)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=254)

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.fullname
    
