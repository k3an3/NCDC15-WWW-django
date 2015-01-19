from django.db import models
from django.contrib.auth.models import User

class BankAccount(models.Model):
    def __str__(self):
        return self.user
    balance = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    user = models.ForeignKey(User)

class Transaction(models.Model):
    def __str__(self):
        return self.typeof
    typeof=models.CharField(default='', max_length=100)
    balance = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    credit = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    debit = models.DecimalField(default=0, max_digits=10, decimal_places=2)
