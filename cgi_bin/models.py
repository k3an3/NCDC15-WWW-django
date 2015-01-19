from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    def __str__(self):
        return self.typeof
    typeof=models.CharField(default='', max_length=100)
    balance = models.IntegerField(default=0)
    credit = models.IntegerField(default=0)
    debit = models.IntegerField(default=0)

class BankUser(models.Model):
    user = models.OneToOneField(User)
    balance = models.IntegerField(default=0)
